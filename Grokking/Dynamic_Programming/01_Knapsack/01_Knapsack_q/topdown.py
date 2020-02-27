""""
Top down dynamic programming with memoination 

We can use memoization to overcome the overlapping sub-problems. 
To reiterate, memoization is when we store the results of all the 
previously solved sub-problems and return the results from memory 
if we encounter a problem that has already been solved.

Since we have two changing values (capacity and currentIndex) 
in our recursive function knapsackRecursive(), 
we can use a two-dimensional array to store the results of all the solved sub-problems. 
As mentioned above, 
we need to store results for every sub-array 
(i.e. for every possible index ‘i’) and for every possible capacity ‘c’.
"""

def solve_knapsack(profits, weights, capacity):
    """"
    profits (list)
    weights (list)
    capacity (int)
    """
    # create a two dimensional array for memoization 
    # each element is initilised to "-1"
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]

    return knapsack_recursive(dp, profits, weights, capacity, 0)


def knapsack_recursive(dp, profits, weights, capacity, currentIndex):

    # base checks 
    if (capacity <= 0) or (currentIndex >= len(profits)):
        return 0 

    # if we have already solved a similar problem, return result from memory 
    if dp[currentIndex][capacity] != -1: 
        return dp[currentIndex][capacity]

    # recursive call after choosing the lement at the currentIndex 
    # if the weight of the element at the currentIndex exceeds the capacity,
    # we shouldnt process this 
    profit1 = 0 
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + \
                  knapsack_recursive(dp, profits, weights,
                                     capacity-weights[currentIndex],
                                     currentIndex+1)

    # recursive call after excluding the element at the currentIndex 
    profit2 = knapsack_recursive(dp, profits, weights, capacity, currentIndex+1)

    dp[currentIndex][capacity] = max(profit1, profit2)
    return dp[currentIndex][capacity]

    
def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))

main()

""""
What is the time and space complexity of the above solution? 
Since our memoization array dp[profits.length][capacity+1] 
stores the results for all the subproblems, 
we can conclude that we will not have more than N*C subproblems 
(where ‘N’ is the number of items and ‘C’ is the knapsack capacity). 
This means that our time complexity will be O(N*C).

The above algorithm will be using O(N*C) space for the memoization array. 
Other than that we will use O(N) space for the recursion call-stack. 
So the total space complexity will be O(N*C + N), 
which is asymptotically equivalent to O(N*C).
"""