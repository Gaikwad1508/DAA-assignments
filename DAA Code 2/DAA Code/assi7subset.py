def find_subset(nums, target):
    # Sort the list to handle combinations in a sorted manner
    nums.sort()
    
    # Initialize an empty list to store the current combination of numbers
    possible_ans = []
    
    # Call the helper function to find subsets
    helper(nums, target, 0, 0, possible_ans)

def helper(nums, target, index, current_sum, possible_ans):
    # If the current sum matches the target, print the current combination
    if current_sum == target:
        print(possible_ans)
        return

    # Variable to keep track of the last element added to avoid duplicates
    prev_element = -1

    # Iterate over the remaining numbers in the list starting from the current index
    for i in range(index, len(nums)):
        # Only proceed if the current number is different from the previous one
        if prev_element != nums[i]:
            # If adding nums[i] to the current_sum exceeds target, exit the loop
            if nums[i] + current_sum > target:
                break
            
            # Include the current number in the combination
            possible_ans.append(nums[i])
            # Update prev_element to current number to avoid duplicates in this level
            prev_element = nums[i]
            
            # Recursively call helper to try the next numbers
            helper(nums, target, i + 1, current_sum + nums[i], possible_ans)
            
            # Remove the last number from the combination to backtrack
            possible_ans.pop()

if __name__ == "__main__":
    # Define a list of numbers and the target sum
    nums = [1, 2, 5, 6, 8]
    # Call the function to find subsets that sum up to the target
    find_subset(nums, 9)
