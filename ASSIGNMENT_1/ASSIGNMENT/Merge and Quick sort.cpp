#include <iostream>
#include <vector>
#include <chrono>

// Function to merge two halves of an array for Merge Sort
void merge(std::vector<int>& arr, int left, int mid, int right) {
    // Calculate the sizes of two subarrays to be merged
    int n1 = mid - left + 1;
    int n2 = right - mid;

    // Create temporary arrays to hold the left and right halves
    std::vector<int> L(n1), R(n2);

    // Copy data into the temporary arrays L[] and R[]
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int i = 0; i < n2; i++)
        R[i] = arr[mid + 1 + i];

    // Merge the two halves back into the main array arr[left..right]
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        // Compare elements and place the smaller one into the main array
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Copy any remaining elements of L[] (if any) into the main array
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copy any remaining elements of R[] (if any) into the main array
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

// Recursive function to perform Merge Sort on the array
void mergeSort(std::vector<int>& arr, int left, int right) {
    if (left < right) {
        // Calculate the midpoint to divide the array
        int mid = left + (right - left) / 2;

        // Recursively sort the first half
        mergeSort(arr, left, mid);
        // Recursively sort the second half
        mergeSort(arr, mid + 1, right);

        // Merge the two sorted halves
        merge(arr, left, mid, right);
    }
}

// Function to swap two elements (used in Quick Sort)
void swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

// Function to partition the array for Quick Sort
int partition(std::vector<int>& arr, int low, int high) {
    // Choose the last element as pivot
    int pivot = arr[high];
    int i = (low - 1); // Index of smaller element

    // Rearrange elements based on the pivot
    for (int j = low; j <= high - 1; j++) {
        // If current element is smaller than the pivot
        if (arr[j] < pivot) {
            i++; // Increment index of the smaller element
            swap(arr[i], arr[j]); // Swap current element with the smaller element
        }
    }
    swap(arr[i + 1], arr[high]); // Place pivot at the correct position
    return (i + 1); // Return the partitioning index
}

// Recursive function to perform Quick Sort on the array
void quickSort(std::vector<int>& arr, int low, int high) {
    if (low < high) {
        // pi is the partitioning index, arr[pi] is now at the correct position
        int pi = partition(arr, low, high);

        // Recursively sort elements before and after partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main() {
    int n;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;

    // Read the elements of the array from the user
    std::vector<int> arr(n);
    std::cout << "Enter the elements:\n";
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }

    // Copy the original array to use for Quick Sort
    std::vector<int> arrCopy = arr;

    // Measure the time taken for Merge Sort
    auto start = std::chrono::high_resolution_clock::now();
    mergeSort(arr, 0, n - 1);
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsedMerge = end - start;

    // Print the sorted array after Merge Sort
    std::cout << "Sorted array with Merge Sort: ";
    for (int i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
    std::cout << "Elapsed time for Merge Sort: " << elapsedMerge.count() << " seconds\n";

    // Measure the time taken for Quick Sort
    start = std::chrono::high_resolution_clock::now();
    quickSort(arrCopy, 0, n - 1);
    end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsedQuick = end - start;

    // Print the sorted array after Quick Sort
    std::cout << "Sorted array with Quick Sort: ";
    for (int i = 0; i < n; i++) {
        std::cout << arrCopy[i] << " ";
    }
    std::cout << std::endl;
    std::cout << "Elapsed time for Quick Sort: " << elapsedQuick.count() << " seconds\n";

    return 0;
}
