#include <iostream>
using namespace std;

int main()
{
  // Declare variables
  int i, num, first, last, middle;
  int x, y, size, temp;
  int sz;

  // Ask user for the size of the array
  cout << "Enter the size of array::";
  cin >> sz;

  // Create an array of the specified size
  int arr[sz];

  // Populate the array with random numbers between 1 and 10000
  for (int i = 0; i < sz; i++)
    arr[i] = 1 + rand() % 10000; // Generate number between 1 to 10000

  // Display the generated array
  cout << "The generated array : ";
  for (int i = 0; i < sz; i++)
    cout << arr[i] << " ";

  // Sort the array in ascending order using Bubble Sort
  for (x = 0; x < sz; x++)
  {
    for (y = x; y < sz - 1; y++) // Use sz - 1 to avoid out-of-bounds access
    {
      if (arr[y] > arr[y + 1]) // Compare adjacent elements
      {
        // Swap elements if they are in the wrong order
        temp = arr[y];
        arr[y] = arr[y + 1];
        arr[y + 1] = temp;
      }
    }
  }

  // Output the sorted array
  cout << "\nElements sorted in the ascending order are : ";
  for (x = 0; x < sz; x++) // Indexing starts from 0, not 1
  {
    cout << arr[x] << " ";
  }

  // Ask user for the element to search
  cout << "\nEnter Element to be Searched: ";
  cin >> num;

  // Initialize search boundaries
  first = 0;
  last = sz - 1;
  middle = (first + last) / 2;

  // Perform binary search
  while (first <= last)
  {
    if (arr[middle] < num) // If middle element is less than the target, search the right half
      first = middle + 1;
    else if (arr[middle] == num) // If the element is found
    {
      cout << "\nThe number, " << num << " found at Position " << middle;
      break;
    }
    else // If middle element is greater than the target, search the left half
      last = middle - 1;

    // Recalculate middle index
    middle = (first + last) / 2;
  }

  // If the element is not found in the array
  if (first > last)
    cout << "\nThe number, " << num << " is not found in the given Array";

  cout << endl;
  return 0;
}
