import flask
import pymongo
import flask_restful
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from databases.db_mongo import MongoDB
from scripts import accelerators
from data_models.models import Vehicle
app = Flask(__name__)

# version numbers
print("Hyperspace v0.1.0")


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb:27017"
api = Api(app)
Mongo = MongoDB(app.config["MONGO_URI"], "hyperspace")


# Start the stargate dududu
stargate = accelerators.start_accelerator(Mongo)

# create some vehicles
PT = Vehicle("Personal Transport",
             0.30,
             1,
             True)

HTC = Vehicle("HTC Transport",
              0.45,
              5,
              False)
vehicles = [PT, HTC]


class CheapestVehicle(Resource):
    def get(self) -> str:
        distance = request.args.get('distance', None)
        passengers = request.args.get('passengers', None)
        parking_days = request.args.get('parking', None)

        if not passengers or not parking_days or not distance:
            return {"message": "Missing query parameters, passengers/parking"}, 400

        try:
            passengers = int(passengers)
            parking_days = int(parking_days)
            distance = int(distance)
        except ValueError:
            return {"message": "Invalid query parameter values: passengers/parking must be integers"}, 400


        cheapest = {}
        for x in vehicles:
            if int(passengers) > x.capacity:
                continue

            dist_cost = x.journey_cost(distance)
            parking_cost = x.parking_cost(int(parking_days))
            total = dist_cost + parking_cost
            cheapest[x.name] = total

        data = get_cheapest_vehicle(cheapest)
        if not cheapest:
            return {"message": "No vehicles available for the given number of passengers"}, 404

        return data

class Accelerators(Resource):
    def get(self) -> str:
        return stargate.graph

class GetAccelerator(Resource):
    def get(self, accelerator_id) -> str:
        data = stargate.get_graph_node(accelerator_id)
        if not data:
            return {"message": "Accelerator not found"}, 404
        return data

class GetShortestRoute(Resource):
    def get(self, start, end ) -> str:
        output = stargate.find_journey(start.upper(), end.upper())
        if not output:
            return {"message": "No route found"}, 404
        return {"distance": output[0], "path": output[1], 'cost': output[0] * 0.1}


def get_cheapest_vehicle(data: dict):
    min_val = min(data.values())
    key = list(data.keys())[list(data.values()).index(min_val)]
    return key


api.add_resource(CheapestVehicle, '/transport/')
api.add_resource(Accelerators, "/accelerators")
api.add_resource(GetAccelerator, "/accelerators/<string:accelerator_id>")
api.add_resource(GetShortestRoute, "/accelerators/<string:start>/to/<string:end>")

if __name__ == "__main__":
    app.run(host="0.0.0.0",
            debug=True)
