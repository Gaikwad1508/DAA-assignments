import sys 

# Function to perform Floyd's Algorithm (Floyd-Warshall Algorithm)
# This algorithm finds the shortest paths between all pairs of nodes in a graph.
def floyds_algorithm(a):
    # k is the intermediate node, i is the source, and j is the destination.
    for k in range(0, 4):  # Iterating over intermediate nodes
        for i in range(0, 4):  # Iterating over source nodes
            for j in range(0, 4):  # Iterating over destination nodes
                # Update the shortest path between i and j using node k as an intermediate point.
                a[i][j] = min(a[i][j], a[i][k] + a[k][j])

    # After updating the matrix with shortest paths, print the result
    for i in range(0, 4):  
        print("\n")  
        for j in range(0, 4):  
            if a[i][j] == sys.maxsize:
                print("INF", end="\t")  # If the distance is infinity, print 'INF'
            else:
                print(a[i][j], end="\t")

# Define the adjacency matrix representing the graph.
a = [
    [0, 3, sys.maxsize, 7],  # Distances from node 0 to other nodes
    [8, 0, 2, sys.maxsize],  # Distances from node 1 to other nodes
    [5, sys.maxsize, 0, 1],  # Distances from node 2 to other nodes
    [2, sys.maxsize, sys.maxsize, 0]  # Distances from node 3 to other nodes
]

# Call the floyds_algorithm function to update the graph with the shortest paths
floyds_algorithm(a)
