import sys  # Importing sys to use sys.maxsize for the initial large value

def tsp_dynamic_programming(graph):
    """
    Finds the minimum cost of the traveling salesman problem using dynamic programming.

    Args:
        graph: A 2D list representing the distances between cities.

    Returns:
        The minimum cost of the traveling salesman problem.
    """

    n = len(graph)  # Number of cities
    all_points_set = set(range(n))  # A set of all cities (0 to n-1)
    memo = {}  # Dictionary to store subproblem solutions (memoization)

    def tsp_helper(curr, visited_set):
        """
        Recursive helper function for dynamic programming.

        Args:
            curr: The current city.
            visited_set: A set of visited cities.

        Returns:
            The minimum cost of traveling from the current city to all unvisited cities and returning to the starting city.
        """

        # Base case: if all cities have been visited, return to the starting city (0)
        if not visited_set:
            return graph[curr][0]  # Return the distance from the current city back to city 0

        # Convert the visited set to a tuple to use it as a key for memoization
        visited_tuple = tuple(sorted(visited_set))

        # If the result has already been computed for this state, return it from the memo
        if (curr, visited_tuple) in memo:
            return memo[(curr, visited_tuple)]

        # Initialize min_cost to a very large number to find the minimum cost path
        min_cost = sys.maxsize

        # Explore each unvisited city and compute the cost recursively
        for next_city in visited_set:
            # Calculate the cost to travel from curr to next_city and continue the tour
            cost = graph[curr][next_city] + tsp_helper(next_city, visited_set - {next_city})
            # Update the minimum cost
            min_cost = min(min_cost, cost)

        # Store the result in memo for future use
        memo[(curr, visited_tuple)] = min_cost
        return min_cost

    # Start the tour from city 0 and exclude it from the set of unvisited cities
    return tsp_helper(0, all_points_set - {0})

# Example usage
graph_example = [
    [0, 10, 15, 20],  # Distances from city 0 to others
    [10, 0, 35, 25],  # Distances from city 1 to others
    [15, 35, 0, 30],  # Distances from city 2 to others
    [20, 25, 30, 0]   # Distances from city 3 to others
]

# Call the function and print the minimum cost for the given graph
result = tsp_dynamic_programming(graph_example)
print("Minimum Cost:", result)
