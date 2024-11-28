import random
import time

# Merge Sort Functions
def merge(arr, start, end):
    # Find the midpoint of the array
    mid = start + (end - start) // 2
    # Calculate lengths of the two halves
    len1 = mid - start + 1
    len2 = end - mid

    # Split the array into two subarrays
    first = arr[start:mid + 1]
    second = arr[mid + 1:end + 1]

    # Initialize indices for merging
    index1 = 0
    index2 = 0
    mainArrayIndex = start

    # Merge elements from both halves into the main array
    while index1 < len(first) and index2 < len(second):
        if first[index1] < second[index2]:
            arr[mainArrayIndex] = first[index1]
            index1 += 1
        else:
            arr[mainArrayIndex] = second[index2]
            index2 += 1
        mainArrayIndex += 1

    # Copy any remaining elements from the first half
    while index1 < len(first):
        arr[mainArrayIndex] = first[index1]
        index1 += 1
        mainArrayIndex += 1

    # Copy any remaining elements from the second half
    while index2 < len(second):
        arr[mainArrayIndex] = second[index2]
        index2 += 1
        mainArrayIndex += 1

def mergeSort(arr, start, end):
    # Base case: if the array has one or zero elements, it's already sorted
    if start >= end:
        return

    # Calculate the midpoint
    mid = start + (end - start) // 2
    # Recursively sort the first half
    mergeSort(arr, start, mid)
    # Recursively sort the second half
    mergeSort(arr, mid + 1, end)
    # Merge the two halves together
    merge(arr, start, end)

# Quick Sort Functions
def swap(arr, i, j):
    # Swap elements at indices i and j
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, low, high):
    # Select the last element as the pivot
    pivot = arr[high]
    # Index for the smaller element
    i = low - 1

    # Rearrange elements based on the pivot
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    # Place the pivot in its correct position
    swap(arr, i + 1, high)
    return i + 1

def quickSort(arr, low, high):
    # Recursive quicksort function
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(arr, low, high)
        # Recursively sort elements before and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

# Utility Functions
def printArray(arr):
    # Print the array elements as a space-separated string
    print(" ".join(map(str, arr)))

# Main Function
if __name__ == "__main__":
    # Set random seed for reproducibility
    random.seed(time.time())

    # Generate a random array of integers
    size = 300
    arr1 = [random.randint(1, 1000) for _ in range(size)]
    # Copy the array for the second sorting algorithm
    arr2 = arr1[:]

    print("Original array:")
    printArray(arr1)

    # Measure and print time taken by Merge Sort
    start_time = time.time()
    mergeSort(arr1, 0, size - 1)
    merge_sort_duration = time.time() - start_time

    print("\nSorted array with Merge Sort:")
    printArray(arr1)
    print(f"Merge Sort Time: {merge_sort_duration:.6f} seconds")

    # Measure and print time taken by Quick Sort
    start_time = time.time()
    quickSort(arr2, 0, size - 1)
    quick_sort_duration = time.time() - start_time

    print("\nSorted array with Quick Sort:")
    printArray(arr2)
    print(f"Quick Sort Time: {quick_sort_duration:.6f} seconds")
