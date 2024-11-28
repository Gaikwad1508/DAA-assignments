def tsp(graph, v, n, current_pos, cost, count, ans):
    # Base case: If all nodes have been visited and there is an edge back to the starting node
    if count == n and graph[current_pos][0] > 0:
        # Update the answer with the minimum cost to complete the tour
        ans = min(ans, cost + graph[current_pos][0])
        return ans
    
    # Try visiting all the vertices
    for i in range(n):
        # If vertex 'i' is unvisited and there's an edge from current_pos to 'i'
        if not v[i] and graph[current_pos][i] > 0:
            # Mark vertex 'i' as visited
            v[i] = True

            # Recur with updated cost, count, and current position
            ans = tsp(graph, v, n, i, cost + graph[current_pos][i], count + 1, ans)

            # Backtrack: Unmark vertex 'i' as visited
            v[i] = False
    
    return ans

def main():
    # Number of nodes in the graph
    n = 4

    # Define the adjacency matrix for the graph
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    # Initialize a list to keep track of visited nodes
    v = [False] * n
    # Initialize the answer with a large value representing infinity
    ans = float('inf')

    # Start the tour from the first vertex, marking it as visited
    v[0] = True

    # Call the tsp function to find the minimum cost Hamiltonian Cycle
    ans = tsp(graph, v, n, 0, 0, 1, ans)

    # Print the minimum cost found
    print(ans)

if __name__ == "__main__":
    main()
