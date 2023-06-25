class Vehicle:

    parking_fee: float = 5

    def __init__(self, name: str, fuel_cost: float, capacity: int, parking: bool):
        self.name = name
        self.fuel_cost = fuel_cost
        self.capacity = capacity
        self.parking = parking

    def __str__(self):
        return f"{self.name} - {self.fuel_cost} - {self.capacity}"

    def journey_cost(self, distance):
        return self.fuel_cost * distance

    def parking_cost(self, days):
        if self.parking_fee:
            return self.parking_fee * days
        else:
            return 0
