# Get user's choice for knapsack method
i = int(input("Enter the choice: 1- dynamic programming // 2 - Back Tracking // 3 - Branch & bound // 0 - exit"))
while(i != 0):
    # Dynamic Programming approach
    if(i == 1):
        def knapsack_dp(weights, values, capacity):
            n = len(weights)
            # Initialize a DP table with 0 values
            dp = [[0] * (capacity + 1) for _ in range(n + 1)]

            # Fill the DP table
            for i in range(1, n + 1):
                for w in range(1, capacity + 1):
                    # If the item can be included
                    if weights[i - 1] <= w:
                        dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
                    else:
                        dp[i][w] = dp[i - 1][w]

            # Reconstruct the selected items from the DP table
            selected_items = []
            w = capacity
            for i in range(n, 0, -1):
                if dp[i][w] != dp[i - 1][w]:
                    selected_items.append(i)
                    w -= weights[i - 1]
            return dp[n][capacity], selected_items

        # Example usage
        weights = [1, 3, 4, 5]
        values = [1, 4, 5, 7]
        capacity = 7
        max_value, selected_items = knapsack_dp(weights, values, capacity)
        print("Maximum value:", max_value)
        print("Selected items:", selected_items)

    # Backtracking approach
    if(i == 2):
        def knapsack_backtracking(weights, values, capacity, n):
            # Base case: no items left or no remaining capacity
            if n == 0 or capacity == 0:
                return 0, []
            
            # If the weight of the current item is greater than the remaining capacity, skip it
            if weights[n - 1] > capacity:
                return knapsack_backtracking(weights, values, capacity, n - 1)
            else:
                # Include the current item
                include_value, include_items = knapsack_backtracking(weights, values, capacity - weights[n - 1], n - 1)
                include_value += values[n - 1]

                # Exclude the current item
                exclude_value, exclude_items = knapsack_backtracking(weights, values, capacity, n - 1)

                # Choose the option with the higher value
                if include_value > exclude_value:
                    include_items.append(n)
                    return include_value, include_items
                else:
                    return exclude_value, exclude_items

        # Example usage
        weights = [1, 3, 4, 5]
        values = [1, 4, 5, 7]
        capacity = 7
        max_value, selected_items = knapsack_backtracking(weights, values, capacity, len(weights))
        print("Maximum value:", max_value)
        print("Selected items:", selected_items)

    # Branch and Bound approach
    if(i == 3):
        def knapsack_branch_and_bound(weights, values, capacity):
            n = len(weights)
            bound = [0] * n  # Upper bound array to store potential maximum value for each item

            def dfs(level, current_weight, current_value, selected_items):
                nonlocal max_value, best_selected_items
                # If we've considered all items
                if level == n:
                    # Update maximum value if current solution is better
                    if current_value > max_value:
                        max_value = current_value
                        best_selected_items = selected_items.copy()
                    return
                
                # Include the current item if it doesn't exceed the capacity
                if current_weight + weights[level] <= capacity:
                    dfs(level + 1, current_weight + weights[level], current_value + values[level], selected_items + [level + 1])

                # Exclude the current item
                dfs(level + 1, current_weight, current_value, selected_items)

            # Precompute upper bounds for each item
            for i in range(n):
                bound[i] = values[i] + sum(values[i + 1:])

            # Initialize the maximum value and best selection
            max_value = 0
            best_selected_items = []
            # Start the depth-first search with level 0
            dfs(0, 0, 0, [])
            return max_value, best_selected_items

        # Example usage
        weights = [1, 3, 4, 5]
        values = [1, 4, 5, 7]
        capacity = 7
        max_value, selected_items = knapsack_branch_and_bound(weights, values, capacity)
        print("Maximum value:", max_value)
        print("Selected items:", selected_items)

    # Get the next choice from the user
    i = int(input("Enter the choice: 1- dynamic programming // 2 - Back Tracking // 3 - Branch & bound // 0 - exit"))

print("You have successfully Exited!!")
#backtracking is used to miltiple solution to solve the problem