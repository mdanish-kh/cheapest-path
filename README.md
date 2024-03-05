# Cheapest path problem

The problem is described in [Problem.md](/Problem.md).

## How to run

The solution is implemented in Python 3. The main file is [cheapest_path.py](/cheapest_path.py). To run the solution, execute the following command:

### Windows

Interactively fill out the airports

```powershell
python cheapest_path.py
```

OR

Provide airports as CLI arguments

```powershell
python cheapest_path.py <start_airport> <end_airport>
```

e.g., `python cheapest_path.py ISB NYC`

### Linux

Replace `python` with `python3` in the above commands.

## Approach and Assumptions

The problem is a classic example of graph traversal. The solution uses Dijkstra's algorithm to find the cheapest path from the start airport to the end airport. The airports are retrieved from a local `.json` file. The graph is built using a python dictionary where the keys are the airports and the values are the connections from that airport. The connections are stored as a list of tuples, where each tuple contains the destination airport and the cost of the connection. The representation follows the adjacency list representation of a graph. Sample graph representation is as follows:

```python
{
    'ISB': [('LHR', 1000), ('CBS', 575)],
    'LHR': [('NYC', 750)],
    'CBS': [('NYC', 775), ('GRC', 731)],
    'NYC': [('GRC', 459)]
}
```

The solution assumes that airports are uni-directional. For example, if there is a connection from `ISB` to `LHR`, it does not assume that there is a connection from `LHR` to `ISB`. This is consistent with the fact that if a direct flight is available from `ISB` to `NYC`, it does not necessarily mean that a direct flight is available from `NYC` to `ISB` (airports tend to change routes based on various conditions). The solution also assumes that the cost of the connection is **non-negative**. (Dijkstra's algorithm does not work with negative weights).
