def knapSack(W, wt, val, n, memo={}):
    # Base case: If no items are left or capacity is 0, no value can be obtained
    if n == 0 or W == 0:
        return 0

    # Check if the result for this subproblem is already calculated (memoized)
    if (n, W) in memo:
        return memo[(n, W)]

    # If the weight of the current item is greater than the remaining capacity, we cannot include it
    if wt[n - 1] > W:
        # Skip the current item and solve for the remaining items with the same capacity
        result = knapSack(W, wt, val, n - 1, memo)
    else:
        # Otherwise, we have two choices:
        # 1. Include the current item and solve for the remaining items with reduced capacity (W - wt[n-1])
        # 2. Exclude the current item and solve for the remaining items with the same capacity W
        result = max(
            val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1, memo),  # Including the current item
            knapSack(W, wt, val, n - 1, memo)  # Excluding the current item
        )

    # Store the result of the subproblem in the memoization table
    memo[(n, W)] = result
    
    # Return the result for this subproblem
    return result

# Example usage
val = [60, 100, 120]  # Values of the items
wt = [10, 20, 30]     # Weights of the items
W = 50                # Maximum weight capacity of the knapsack
n = len(val)          # Number of items

# Call the knapSack function to calculate the maximum value
result = knapSack(W, wt, val, n)

# Output the result
print("Maximum value that can be obtained:", result)
