""""
Can we further improve our bottom-up DP solution? 
Can you find an algorithm that has O(C) space complexity?

The above solution is similar to the previous solution, 
the only difference is that we use i%2 instead if i 
and (i-1)%2 instead if i-1. 
This solution has a space complexity of O(2*C) = O(C), 
where ‘C’ is the maximum capacity of the knapsack.
"""
def solve_knapsack(profits, weights, capacity):
    # Since we update the table row by row, we can only keep 
    # 2 rows, see video 

    # basic checks 
    n = len(profits)
    if (capacity<=0) or (n==0) or (len(weights)!=n):
        return 0 

    ## we onlu needxc one previous row to find the optimal solution,
    ## overall we need "2" rows 
    ## this solution is similar to "bottomup.py"
    ## only difference is to use "i%2" instead of "i"
    ## and "(i-1)%2" instead of "i-1"
    dp = [[0 for x in range(capacity+1)] for y in range(2)]

    ## if we only have one weight, 
    ## we will take it if it is not more than the capacity 
    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[0][c] = dp[1][c] = profits[0]

    # process all sub-arrays for all the capacities 
    for i in range(1,n):
        for c in range(0, capacity+1):
            profits1, profits2 = 0, 0
            # include the item, if it is not moret than the capacity 
            if weights[i] <=c:
                profits1 = profits[i] + dp[(i-1)%2][c-weights[i]]
            # exclude the item 
            profits2 = dp[(i-1)%2][c]
            # take maximum 
            dp[i%2][c] = max(profits1, profits2)

    return dp[(n-1)%2][capacity]

def main():
    print(solve_knapsack(profits=[1, 6, 10, 16], weights=[1, 2, 3, 5], capacity=5))
    print(solve_knapsack(profits=[1, 6, 10, 16], weights=[1, 2, 3, 5], capacity=6))
    print(solve_knapsack(profits=[1, 6, 10, 16], weights=[1, 2, 3, 5], capacity=7))

main()

"""""
This space optimization solution can also be implemented using a single array. 
It is a bit tricky though, 
but the intuition is to use the same array for the previous and the next iteration!

If you see closely, 
we need two values from the previous iteration: dp[c] and dp[c-weight[i]]

Since our inner loop is iterating over c:0-->This space optimization solution can also be implemented using a single array. It is a bit tricky though, but the intuition is to use the same array for the previous and the next iteration!

If you see closely, we need two values from the previous iteration: dp[c] and dp[c-weight[i]]

Since our inner loop is iterating over c:0-->capacity, let’s see how this might affect our two required values:

When we access dp[c], 
it has not been overridden yet for the current iteration, 
so it should be fine.
dp[c-weight[i]] might be overridden if “weight[i] > 0”. 
Therefore we can’t use this value for the current iteration.
To solve the second case, 
IMPORTRANT:@
we can change our inner loop to process in the reverse direction: c:capacity-->0. 
This will ensure that whenever we change a value in dp[], 
we will not need it anymore in the current iteration.
"""

def solve_knapsack_2(profits, weights, capacity):
    # basic checks 
    n = len(profits)
    if (capacity <= 0) or (n==0) or (len(weights)!=n):
        return 0

    dp = [0 for x in range(capacity+1)]
    
    # if we have only one weight, we will take it if it is not more than capacity 
    for c in range(0, capacity+1):
        if weights[0] <= c:
            dp[c] = profits[0]

    # process all sub-arrays for all the capacities 
    for i in range(1,n):
        for c in range(capacity, -1, -1):
            profit1, profit2 = 0, 0 
            # include the item, if it is more than the capacity 
            if weights[i] <= c:
                profit1 = profits[i] + dp[c-weights[i]]
            # exclude the item 
            profit2 = dp[c]
            # take maximum 
            dp[c] = max(profit1, profit2)

    return dp[capacity]
        
def main_():
    print(solve_knapsack_2(profits=[1, 6, 10, 16], weights=[1, 2, 3, 5], capacity=5))
    print(solve_knapsack_2(profits=[1, 6, 10, 16], weights=[1, 2, 3, 5], capacity=6))
    print(solve_knapsack_2(profits=[1, 6, 10, 16], weights=[1, 2, 3, 5], capacity=7))

main_()