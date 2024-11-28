#include <iostream>
#include <algorithm>
using namespace std;

// Structure to represent an item with a value and weight
struct Item
{
    int value, weight;

    // Constructor to initialize the value and weight of the item
    Item(int value, int weight)
    {
        this->value = value;
        this->weight = weight;
    }
};

// Comparator function to sort items by value-to-weight ratio in decreasing order
bool cmp(struct Item a, struct Item b)
{
    // Calculate the value-to-weight ratio of each item
    double r1 = (double)a.value / (double)a.weight; // Ratio of item a
    double r2 = (double)b.value / (double)b.weight; // Ratio of item b
    return r1 > r2;                                 // Sort in descending order of ratio
}

// Function to calculate the maximum value that can be obtained in a fractional knapsack
double fractionalKnapsack(int W, struct Item arr[], int N)
{
    // Sort items based on value-to-weight ratio in decreasing order
    sort(arr, arr + N, cmp);

    double finalValue = 0.0; // Variable to store the final maximum value

    // Loop through all items
    for (int i = 0; i < N; i++)
    {
        // If the item can fully fit in the knapsack, add it fully
        if (arr[i].weight <= W)
        {
            W -= arr[i].weight;          // Reduce the remaining capacity of the knapsack
            finalValue += arr[i].value;   // Add the item's full value to the total value
        }
        else
        {
            // If the item can't fully fit, take a fraction of it to fill the knapsack
            finalValue += arr[i].value * ((double)W / (double)arr[i].weight); // Take fraction of value based on remaining weight
            break; // Knapsack is full, so exit the loop
        }
    }

    return finalValue; // Return the maximum value obtained
}

int main()
{
    int W = 20; // Total capacity of the knapsack
    Item arr[] = {{10, 3}, {20, 5}, {21, 5}, {30, 8}, {16, 4}}; // Array of items (value, weight)

    int N = sizeof(arr) / sizeof(arr[0]); // Calculate the number of items

    // Output the maximum value obtainable in the knapsack
    cout << "Maximum value we can obtain = " << fractionalKnapsack(W, arr, N) << endl;

    return 0;
}
