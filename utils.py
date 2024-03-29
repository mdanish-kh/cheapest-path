# Description: This file contains utility functions for the main program.

# For deserializing json data
import json

# For priority queue implementation
import heapq


def get_airports(path):
    """ Get airport data from a local JSON file.
    This implementation can be updated if we are receiving data from an actual API endpoint.
    """
    with open(path) as data_file:
        data = json.load(data_file)
        return data


def generate_airports_graph(airports: list):
    """ Builds a directed airport graph in adjacency list representation format.
    Sample output:
    {
        'ISB': [('LHR', 1000), ('CBS', 575)],
        'LHR': [('NYC', 750)],
    }
    """
    graph = {}

    # Each node in the list is represented in the following JSON format:
    #  {"start": "ISB","end": "LHR","cost": 1000}
    for connection in airports:
        start = connection['start']
        end = connection['end']
        cost = connection['cost']

        # If the starting node does not exist in the graph, add a new graph node
        if start not in graph:
            graph[start] = [(end, cost)]

        # Append the connection to the existing graph node if starting node exists
        else:
            # Prevent duplicate connections
            if end not in graph[start]:
                graph[start].append((end, cost))

        # Add leaf or end nodes to the graph with empty lists
        if end not in graph:
            graph[end] = []

    return graph


def cheapest_graph_path(graph: dict, start: str, end: str):
    """Implements the Dijkstra's algorithm to find single source
    shortest path on a weighted graph
    """
    # Early return if start and end nodes are the same
    if start == end:
        return [start], 0

    # Initialize the costs of all nodes to infinity
    costs = {node: float('infinity') for node in graph}

    # Set the cost of the starting node to 0
    costs[start] = 0

    # Initialize the priority queue with the starting node
    # Priority queue is a min heap that stores the nodes in the order of their cost from the starting node
    # It is needed to get the node with the minimum cost in O(log n) time
    priority_queue = [(0, start)]

    # Initialize dictionary to keep track of previous nodes in the shortest path
    previous_nodes = {}

    # While the priority queue is not empty
    while priority_queue:

        # Pop the node with the minimum cost from the priority queue
        current_cost, current_node = heapq.heappop(priority_queue)

        # If the current node is the end node, return the cheapest path and its cost
        if current_node == end:
            break

        # If the current node is not the end node
        # Iterate through its neighbors and update their costs if a cheaper path is found
        for neighbor, weight in graph[current_node]:
            cost = current_cost + weight

            # If the cost to reach neighbor is cheaper than the previous cost
            if cost < costs[neighbor]:

                # Perform the relaxation operation (update the cost of the neighbor)
                costs[neighbor] = cost
                heapq.heappush(priority_queue, (cost, neighbor))

                # Update previous nodes dictionary
                previous_nodes[neighbor] = current_node

    # If no path exists from start to end, return None, None
    if end not in previous_nodes:
        return None, None

    # Construct the cheapest path from the starting node to the end node
    shortest_path = []
    current_node = end
    while current_node != start:
        shortest_path.append(current_node)
        current_node = previous_nodes[current_node]
    shortest_path.append(start)
    shortest_path.reverse()

    return shortest_path, costs[end]
