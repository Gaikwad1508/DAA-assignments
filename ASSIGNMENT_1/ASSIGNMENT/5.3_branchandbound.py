import heapq

# Class to store item information (weight, value, and index)
class Item:
    def __init__(self, weight, value, index):
        self.weight = weight  # Weight of the item
        self.value = value    # Value of the item
        self.index = index    # Index of the item
        # Value-to-weight ratio, used for sorting items by efficiency
        self.ratio = value / weight

# Function to solve the knapsack problem using Branch and Bound
def knapsack_branch_and_bound(weights, values, capacity):
    n = len(weights)  # Number of items
    
    # Create a list of items with weight, value, and their index
    items = [Item(weights[i], values[i], i) for i in range(n)]
    
    # Sort items by value-to-weight ratio in descending order for efficiency
    items.sort(key=lambda x: x.ratio, reverse=True)

    # Class to represent a node in the search tree
    class Node:
        def __init__(self, level, value, weight, bound):
            self.level = level  # Index of the item in the list
            self.value = value  # Total value accumulated so far
            self.weight = weight  # Total weight accumulated so far
            self.bound = bound  # Upper bound on the maximum value achievable from this node
        
        # Comparison operator for priority queue, based on the bound (higher bound = higher priority)
        def __lt__(self, other):
            return self.bound > other.bound

    # Function to calculate the upper bound of the maximum possible profit from a node
    def bound(node):
        # If the accumulated weight exceeds the knapsack's capacity, the bound is 0
        if node.weight >= capacity:
            return 0
        
        # Start with the current node's value
        profit_bound = node.value
        # Start from the next item in line
        j = node.level + 1
        tot_weight = node.weight

        # Greedily add items while staying within the capacity
        while j < n and tot_weight + items[j].weight <= capacity:
            tot_weight += items[j].weight
            profit_bound += items[j].value
            j += 1

        # Add a fraction of the next item, if there's remaining capacity
        if j < n:
            profit_bound += (capacity - tot_weight) * items[j].ratio

        return profit_bound

    # Priority queue (max-heap) to explore the search tree based on bound values
    priority_queue = []
    
    # Start with a dummy node (root) with level -1, zero value, and zero weight
    v = Node(-1, 0, 0, 0)
    v.bound = bound(v)  # Calculate bound for the root node
    max_profit = 0  # Track the maximum profit found so far

    # Insert the root node into the priority queue
    heapq.heappush(priority_queue, v)

    # Process nodes in the priority queue
    while priority_queue:
        # Remove the node with the highest bound
        v = heapq.heappop(priority_queue)

        # Explore further only if bound is greater than max profit and it's not the last item
        if v.bound > max_profit and v.level < n - 1:
            # Create a node for including the next item
            u = Node(v.level + 1, v.value + items[v.level + 1].value, v.weight + items[v.level + 1].weight, 0)

            # Update max profit if the current node's weight is within capacity and has higher value
            if u.weight <= capacity and u.value > max_profit:
                max_profit = u.value

            # Calculate and set the bound for including the item
            u.bound = bound(u)

            # If the bound is greater than max profit, add the node to the queue
            if u.bound > max_profit:
                heapq.heappush(priority_queue, u)

            # Create a node for excluding the next item
            u = Node(v.level + 1, v.value, v.weight, 0)
            u.bound = bound(u)

            # If the bound for excluding the item is greater than max profit, add it to the queue
            if u.bound > max_profit:
                heapq.heappush(priority_queue, u)

    # Return the maximum profit found
    return max_profit

# Example usage
weights = [1, 2, 3, 5]     # Weights of each item
values = [1, 6, 10, 16]    # Values of each item
capacity = 7               # Maximum capacity of the knapsack

# Print the maximum value achievable with the given weights and values
print(f"Maximum value using Branch and Bound: {knapsack_branch_and_bound(weights, values, capacity)}")
