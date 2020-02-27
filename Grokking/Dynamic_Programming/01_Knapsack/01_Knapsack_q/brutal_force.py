# for each item 'i' 
#   create a new set which INCLUDES item 'i' if the total weight does not exceed the capacity, and 
#      recursively process the remaining capacity and items
#   create a new set WITHOUT item 'i', and recursively process the remaining items 
# return the set from the above two sets with higher profit 

def solve_knapsack(profits, weights, capacity):
    """"
    profits (list)
    weights (list)
    capacity (int)
    """
    return knapsack_recursive(profits, weights, capacity, 0)

def knapsack_recursive(profits, weights, capacity, currentIndex):
    """"
    profits (list)
    weights (list)
    capacity (int)
    currentIndex (int)
    """
    # base checks 
    if (capacity <= 0) or (currentIndex >= len(profits)):
        return 0 

    # recursive call after choosing the element at the currentIndex 
    # if the weight of element at currentIndex exceeds the capacity
    # we shouldnt process this
    profit1 = 0 
    if weights[currentIndex] <= capacity: 
        profit1 = profits[currentIndex] + \
                  knapsack_recursive(profits, 
                                     weights, 
                                     capacity - weights[currentIndex],
                                     currentIndex + 1)

    # recursive call after excluding the element at the currentIndex 
    profit2 = knapsack_recursive(profits, 
                                 weights, 
                                 capacity, 
                                 currentIndex +1)
                            
    return max(profit1, profit2)

def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))

main()


## Time complexity: O(2^n) wherer n is the total number of items. 
## in the recursion tree, we have 31 recursive calls, 
## by (2^n) + (2^n) - 1 which is asymptotically equivalent to O(2^n)

# the space complexity is O(n), this space will be used to store hte recursion stack 
# Since the recursive algo works in a depth first fashion, which means we cant have more than
# "n" recursive calls on the call stack at any time 

