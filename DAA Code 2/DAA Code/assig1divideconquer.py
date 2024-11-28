def binary_search(arr, left, right, key):
    while left <= right:
        mid = left + (right - left) // 2

        # Debug: Print the current middle value being compared
        print(f"Comparing with middle element at index {mid}: {arr[mid]}")

        # Check if the key is present at mid
        if arr[mid] == key:
            return mid

        # If key is greater, ignore the left half
        if arr[mid] < key:
            left = mid + 1
        # If key is smaller, ignore the right half
        else:
            right = mid - 1

    # Key not found
    return -1

def main():
    # Get the size of the array from the user
    size = int(input("Enter the size of the array: "))

    # Input validation for array size
    if size <= 0:
        print("Array size must be positive.")
        return

    # Get all elements in a single line, split them, and convert each to an integer
    arr = list(map(int, input(f"Enter {size} elements of the array: ").split()))

    # Check if the correct number of elements was entered
    if len(arr) != size:
        print(f"Error: Expected {size} elements, but got {len(arr)}.")
        return

    # Sort the array before performing binary search
    arr.sort()

    # Display the sorted array for verification
    print("Sorted array:", " ".join(map(str, arr)))

    # Get the key element from the user
    key = int(input("Enter the element you want to search for: "))

    # Debug: Print the key to be searched
    print(f"Searching for the key: {key}")

    # Perform binary search
    result = binary_search(arr, 0, len(arr) - 1, key)

    # Output the result
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array.")

if __name__ == "__main__":
    main()