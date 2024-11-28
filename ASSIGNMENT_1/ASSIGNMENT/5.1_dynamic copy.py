def knapsack_dp(weights, values, capacity):
    # Number of items
    n = len(values)

    # Create a 2D DP table with (n+1) rows and (capacity+1) columns, initialized to 0
    # dp[i][w] represents the maximum value achievable with the first i items and a capacity of w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Iterate through each item (1-based index for items in dp table)
    for i in range(1, n + 1):
        # Iterate through each weight capacity from 1 up to the total capacity
        for w in range(1, capacity + 1):
            # If the weight of the current item (weights[i-1]) is less than or equal to the current capacity `w`
            if weights[i - 1] <= w:
                # Calculate the maximum value by either:
                # 1. Including the current item: value of current item (values[i-1]) + best value for remaining capacity (dp[i-1][w - weights[i-1]])
                # 2. Excluding the current item: take the best value without this item (dp[i-1][w])
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # If the current item's weight exceeds the current capacity `w`, skip it
                # Use the best value achievable without this item (dp[i-1][w])
                dp[i][w] = dp[i - 1][w]

    # Return the maximum value achievable with all items and the full capacity (bottom-right corner of the DP table)
    return dp[n][capacity]

# Example usage
weights = [1, 2, 3, 5]     # Weights of each item
values = [1, 6, 10, 16]    # Values of each item
capacity = 7               # Maximum capacity of the knapsack

# Print the maximum value achievable with the given weights and values
print(f"Maximum value using Dynamic Programming: {knapsack_dp(weights, values, capacity)}")
