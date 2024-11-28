# Function to find all unique subsets of 'nums' that sum to 'target'
def find_subset(nums, target):
    # Sort the input array to handle duplicates and enable early termination if the sum exceeds the target
    nums.sort()
    
    # List to store the current subset being considered
    possible_ans = []
    
    # Start the recursive search from the first index, with a current sum of 0
    helper(nums, target, 0, 0, possible_ans)

# Recursive helper function to find subsets that sum up to the target
def helper(nums, target, index, current_sum, possible_ans):
    # Base case: if current_sum equals the target, we found a valid subset
    if current_sum == target:
        print(possible_ans)  # Print the current valid subset
        return

    # Variable to keep track of the last element used to avoid duplicate subsets
    prev_element = -1

    # Iterate through elements in nums starting from the given index
    for i in range(index, len(nums)):
        # Skip duplicates: Only process the element if it is different from the previous one
        if prev_element != nums[i]:
            # Stop the search early if adding nums[i] exceeds the target
            # (since the array is sorted, all subsequent elements will also exceed the target)
            if nums[i] + current_sum > target:
                break
            
            # Add nums[i] to the current subset and update the current sum
            possible_ans.append(nums[i])
            
            # Set the previous element to the current one to handle duplicates in the next iterations
            prev_element = nums[i]
            
            # Recursive call with the next index and the updated sum
            helper(nums, target, i + 1, current_sum + nums[i], possible_ans)
            
            # Backtrack by removing the last element from the subset after exploring that branch
            possible_ans.pop()

# Driver code to test the function
if __name__ == "__main__":
    # Define the input list and the target sum
    nums = [1, 2, 5, 6, 8]
    
    # Call the function to find and print all subsets that sum up to 9
    find_subset(nums, 9)
