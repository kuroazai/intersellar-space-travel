import unittest
import requests

class TestApp(unittest.TestCase):
    url = "http://127.0.0.1:5000"

    def test_shortest_route(self):
        params = {"start": "SOL", "end": "VEG"}
        route = f"/accelerators/{params['start']}/to/{params['end']}"
        print(self.url + route)
        response = requests.get(self.url + route, params=params)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        print(response.json())

    def test_shortest_route_no_start(self):
        params = {"end": "VEG"}
        route = f"/accelerators/to/{params['end']}"
        response = requests.get(self.url + route, params=params)
        self.assertEqual(response.status_code, 404)

    def test_get_accelerators(self):
        route = "/accelerators"
        response = requests.get(self.url + route)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_get_accelerator(self):
        route = "/accelerators/SOL"
        response = requests.get(self.url + route)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_cheapest_vehicle(self):
        params = {'distance': 1000,
                  'passengers': 5,
                  'parking': 10}
        route = "/transport/"
        response = requests.get(self.url + route, params=params)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), str)


if __name__ == "__main__":

    unittest.main()