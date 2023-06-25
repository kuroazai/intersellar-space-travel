import json
import os
import heapq

class AcceleratorGraph:
    def __init__(self, accelerator_data):
        self.graph = accelerator_data

    def find_shortest_path(self, start: str, end : str) -> list:
        distances = {start: 0}
        previous = {}
        queue = [(0, start)]

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_node == end:
                path = []
                while current_node in previous:
                    path.append(current_node)
                    current_node = previous[current_node]
                path.append(start)
                path.reverse()
                return path

            if current_node in self.graph:
                connections = self.graph[current_node]
                for neighbor, distance in connections.items():
                    new_distance = current_distance + distance
                    if neighbor not in distances or new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        previous[neighbor] = current_node
                        heapq.heappush(queue, (new_distance, neighbor))

        return None

    def calculate_total_distance(self, path: list):
        total_distance = 0
        for i in range(len(path) - 1):
            start = path[i]
            end = path[i + 1]
            total_distance += self.graph[start][end]

        return total_distance

    def find_journey(self, start: str, end: str) -> tuple:
        path = self.find_shortest_path(start, end)
        if path is None:
            return None

        distance = self.calculate_total_distance(path)
        return distance, path

    def get_graph_node(self, node: str):
        return self.graph[node]


def download_from_mongo(Mongo):
    unique_id = "accelerators"
    result = Mongo.find_one("test", {"_id": unique_id})
    if result:
        # Document with the unique ID exists
        print("Document exists")
        return result
    else:
        # Document with the unique ID does not exist
        print("Document does not exist")
        return None

def load_accelerator_data(path):
    with open(path, "r") as file:
        return json.load(file)

def start_accelerator(Mongo):
    data = download_from_mongo(Mongo)
    return AcceleratorGraph(data)

