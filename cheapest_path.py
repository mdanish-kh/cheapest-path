from utils import get_airports, generate_airports_graph, cheapest_graph_path
import sys

# Entry point of the program
def main():
    start_airport = None
    end_airport = None

    # Interactively ask for start and end airports
    if len(sys.argv) == 1:
        start_airport = input("Enter the start airport: ")
        end_airport = input("Enter the end airport: ")

    # Show usage if the number of arguments is not correct
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        print("Usage:")
        print("- python cheapest_path.py (to interactively provide start and end airports)")
        print("- python cheapest_path.py <start_airport> <end_airport>")
        exit(1)

    # Get start and end airports from command line arguments
    if not start_airport and not end_airport:
        start_airport = sys.argv[1]
        end_airport = sys.argv[2]

    # Get airports from local json file
    airports_data = get_airports('./airports.json')

    # Get cheapest path and related cost for user-provided start and end airports
    cheapest_path, cost = find_cheapest_path(airports_data, start_airport, end_airport)

    if not cheapest_path:
        print(f"No path found between {start_airport} and {end_airport}.")
        exit(1)

    print("Cheapest path: ", cheapest_path)
    print("Cost: ", cost)


def find_cheapest_path(airports: list, start: str, end: str):
    # Build the airport graph
    airports_graph: dict = generate_airports_graph(airports)

    # Get all airports from the data
    all_airports = [airport['start'] for airport in airports] + [airport['end'] for airport in airports]

    # Validate input
    if start not in all_airports:
        print(f"'{start}' is not a valid value for a starting airport.")
        exit()

    if end not in all_airports:
        print(f"'{end}' is not a valid value for an ending airport.")
        exit()

    return cheapest_graph_path(airports_graph, start, end)


if __name__ == '__main__':
    main()
