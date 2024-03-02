#include <iostream>
#include <vector>

using namespace std;

int knapsack_recursive(int C, int n, const vector<int>& w, const vector<int>& p) {
    // Base case: If there are no items left or the capacity is 0, return 0.
    if (n == 0 || C == 0) {
        return 0;
    }

    // If the weight of the current item exceeds the remaining capacity, skip it.
    if (w[n - 1] > C) {
        return knapsack_recursive(C, n - 1, w, p);
    }

    // Calculate the maximum profit by either including or excluding the current item.
    int include_current = p[n - 1] + knapsack_recursive(C - w[n - 1], n, w, p);
    int exclude_current = knapsack_recursive(C, n - 1, w, p);

    // Return the maximum of including and excluding the current item.
    return max(include_current, exclude_current);
}

int main() {
    vector<int> weights = {4, 6, 8};
    vector<int> profits = {7, 6, 9};
    int capacity = 14;
    int n = weights.size();

    int max_profit = knapsack_recursive(capacity, n, weights, profits);
    cout << "Maximum Profit for P(14) = " << max_profit << endl;

    return 0;
}
