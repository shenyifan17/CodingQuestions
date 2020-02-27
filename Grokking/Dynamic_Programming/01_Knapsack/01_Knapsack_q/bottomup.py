def solve_knapsack(profits, weights, capacity):
    # basic checks 
    n = len(profits)
    if (capacity <= 0) or (n == 0) or (len(weights) != n):
        return 0 

    # generate an empty matrix with "0"s
    dp = [[0 for x in range(capacity+1)] for y in range(n)]

    # populate the capacity = 0 columns, 
    # with "0" capacity we have "0" profit
    ## the first column of "0"s
    for i in range(0, n):
        dp[i][0] = 0 

    # if we have only one weight, 
    # we will take it if it is not more than the capacity 
    for c in range(0, capacity+1):
        if weights[0] <= c: 
            dp[0][c] = profits[0] ## first row of "1"s

    # process all sub-arrays for ALL capacities 
    for i in range(1,n):
        for c in range(1, capacity+1):
            profit1, profit2 = 0, 0
            # include the item, if it is not more than the capacity 
            if weights[i] <= c:
                profit1 = profits[i] + dp[i-1][c-weights[i]]
            # exclude the item 
            profit2 = dp[i-1][c]
            # take maximum 
            dp[i][c] = max(profit1, profit2)

    print_selected_elements(dp, weights, profits, capacity)
    # generate an empty matrix with "0"
    # maximum profit will be at the bottom-right cornor. 
    return dp[n-1][capacity]


""""
Above solution has both time and space complexity of O(N*C)
where N is total number of items and C is the max capacity
"""


""""
As we know that the final profit is at the bottom-right corner; 
therefore we will start from there to find the items 
that will be going in the knapsack.

As you remember, at every step we had two options: 
include an item or skip it. 
If we skip an item, 
then we take the profit from the remaining items 
(i.e. from the cell right above it);hi 
if we include the item, 
then we jump to the remaining profit to find more items.
"""

def print_selected_elements(dp, weights, profits, capacity):
    print("Selected weights are: ", end='')
    n = len(weights)
    totalProfit = dp[n-1][capacity]
    for i in range(n-1, 0, -1): ## counting down
        if totalProfit != dp[i-1][capacity]:
            print(str(weights[i]) + " ", end='')
            capacity -= weights[i]
            totalProfit -= profits[i]

    if totalProfit != 0:
        print(str(weights[0]) + " ", end='')
    print()

def main():
    print(solve_knapsack(profits=[1, 6, 10, 16], weights=[1, 2, 3, 5], capacity=5))
    print(solve_knapsack(profits=[1, 6, 10, 16], weights=[1, 2, 3, 5], capacity=6))
    print(solve_knapsack(profits=[1, 6, 10, 16], weights=[1, 2, 3, 5], capacity=7))

main()
