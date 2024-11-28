# Function to solve the Traveling Salesman Problem (TSP) using recursion and backtracking
# Parameters:
# - graph: 2D list representing distances between cities
# - v: list to track visited cities
# - n: total number of cities
# - current_pos: the current city position
# - cost: the total cost incurred so far
# - count: number of cities visited so far
# - ans: the minimum cost found for a complete tour
def tsp(graph, v, n, current_pos, cost, count, ans):
    # Base case: if all cities are visited and there's a path back to the starting city
    if count == n and graph[current_pos][0] > 0:
        # Update the answer with the minimum cost of completing the tour
        ans = min(ans, cost + graph[current_pos][0])
        return ans

    # Try visiting all cities from the current city position
    for i in range(n):
        # Check if city i is not visited and there's a path from current_pos to i
        if not v[i] and graph[current_pos][i] > 0:
            # Mark city i as visited
            v[i] = True

            # Recursively call tsp to explore further paths and update the minimum cost
            ans = tsp(graph, v, n, i, cost + graph[current_pos][i], count + 1, ans)

            # Backtrack: unmark city i to try other possibilities
            v[i] = False

    # Return the minimum cost found for completing the tour
    return ans

# Main function to set up the problem and call the tsp function
def main():
    # Number of cities
    n = 4

    # Distance matrix representing the graph where graph[i][j] is the distance from city i to city j
    graph = [
        [0, 10, 15, 20],  # Distances from city 0 to other cities
        [10, 0, 35, 25],  # Distances from city 1 to other cities
        [15, 35, 0, 30],  # Distances from city 2 to other cities
        [20, 25, 30, 0]   # Distances from city 3 to other cities
    ]

    # Boolean list to track visited cities (initialize all as False)
    v = [False] * n

    # Initialize the minimum cost answer to infinity
    ans = float('inf')

    # Mark the starting city (city 0) as visited
    v[0] = True

    # Start the TSP function from city 0, with an initial cost of 0 and one city visited
    ans = tsp(graph, v, n, 0, 0, 1, ans)

    # Print the minimum cost of completing the tour
    print(ans)

# Driver code to run the main function
if __name__ == "__main__":
    main()
