# Helper functions to find the cheapest path between two airports
from utils import get_airports, generate_airports_graph, cheapest_graph_path

# For reading command line arguments
import sys

"""Entry point of the program
"""


def main():
    start_airport = None
    end_airport = None

    # Interactively ask for start and end airports
    if len(sys.argv) == 1:
        start_airport = input("Enter the start airport: ").upper()
        end_airport = input("Enter the end airport: ").upper()

    # Show usage if the number of arguments is not correct
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        print("Usage:")
        print("- python cheapest_path.py (to interactively provide start and end airports)")
        print("- python cheapest_path.py <start_airport> <end_airport>")
        exit(1)

    # Get start and end airports from command line arguments
    if not start_airport and not end_airport:
        start_airport = sys.argv[1].upper()
        end_airport = sys.argv[2].upper()

    # Get airports from local json file
    airports_list = get_airports('./data/airports.json')

    # Get cheapest path and related cost for user-provided start and end airports
    cheapest_path, cost = find_cheapest_path(
        airports_list, start_airport, end_airport)

    if not cheapest_path:
        print(f"No path found between {start_airport} and {end_airport}.")
        exit(1)

    print("Cheapest path: ", cheapest_path)
    print("Cost: ", cost)


def find_cheapest_path(airports: list, start: str, end: str):
    """Find the cheapest path between two airports
    Function to be considered as the solution to the given problem
    Takes in a list of airports and the start and end airports and returns
    the cheapest path and the cost.
    """
    # Build the airport graph
    airports_graph: dict = generate_airports_graph(airports)

    # Get all airports from the data
    all_airports = [airport['start'] for airport in airports] + \
        [airport['end'] for airport in airports]

    # Validate input
    if start not in all_airports:
        print(f"'{start}' is not a valid value for a starting airport.")
        exit(1)

    if end not in all_airports:
        print(f"'{end}' is not a valid value for an ending airport.")
        exit(1)

    return cheapest_graph_path(airports_graph, start, end)


if __name__ == '__main__':
    main()
