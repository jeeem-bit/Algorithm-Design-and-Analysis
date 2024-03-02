#include <iostream>
using namespace std;

int P(int C, int weight[], int profit[], int n) {
    // Base case: If the remaining capacity is 0 or there are no items left to consider
    if (C == 0 || n == 0) {
        return 0;
    }

    // If the weight of the current item is greater than the remaining capacity, skip it
    if (weight[n - 1] > C) {
        return P(C, weight, profit, n - 1);
    }

    // Return the maximum of two cases:
    // 1. Include the current item and recursively compute the profit for the remaining capacity
    // 2. Exclude the current item and recursively compute the profit for the same capacity
    return max(
        profit[n - 1] + P(C - weight[n - 1], weight, profit, n - 1),
        P(C, weight, profit, n - 1)
    );
}

int main() {
    int C = 10;
    int weight[] = {5, 6, 8};
    int profit[] = {7, 6, 9};
    int n = sizeof(weight) / sizeof(weight[0]);

    int maxProfit = P(C, weight, profit, n);
    cout << "Maximum Profit for C = " << C << " is " << maxProfit << endl;

    return 0;
}
