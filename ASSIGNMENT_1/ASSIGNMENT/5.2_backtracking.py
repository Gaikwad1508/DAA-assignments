def knapsack_backtracking(weights, values, capacity, n):
    # Recursive helper function to explore all combinations of including/excluding items
    def helper(i, cur_weight, cur_value):
        # Base case: if all items have been considered
        if i == n:
            return cur_value  # Return the accumulated value

        # Case 1: If adding the current item exceeds the capacity, skip it
        # Proceed without including the current item in the knapsack
        if cur_weight + weights[i] > capacity:
            return helper(i + 1, cur_weight, cur_value)

        # Case 2: Two possibilities:
        # 1. Include the current item in the knapsack
        include = helper(i + 1, cur_weight + weights[i], cur_value + values[i])

        # 2. Exclude the current item from the knapsack
        exclude = helper(i + 1, cur_weight, cur_value)

        # Return the maximum value obtained by either including or excluding the current item
        return max(include, exclude)

    # Start recursion from the 0th item with 0 current weight and 0 current value
    return helper(0, 0, 0)

# Example usage
weights = [1, 2, 3, 5]     # Weights of each item
values = [1, 6, 10, 16]    # Values of each item
capacity = 7               # Maximum capacity of the knapsack
n = len(values)            # Number of items

# Print the maximum value achievable with the given weights and values
print(f"Maximum value using Backtracking: {knapsack_backtracking(weights, values, capacity, n)}")
