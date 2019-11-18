# Problem Statement
# Given an array of characters where 
# each character represents a fruit tree,
# you are given two baskets and 
# your goal is to put maximum number of fruits in each basket. 
# The only restriction is that 
# each basket can have only one type of fruit.
# 
# You can start with any tree,
# wbut once you have started you can’t skip a tree. 
# You will pick one fruit from each tree until you cannot, 
# i.e., you will stop when you have to pick 
# from a third fruit type.
# 
# Write a function to 
# return the maximum number of fruits in both the baskets.
# 
# Example 1:
# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: 
# We can put 2 'C' in one basket 
# and one 'A' in the other from the subarray ['C', 'A', 'C']

# Example 2:
# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: 
# We can put 3 'B' in one basket and 
# two 'C' in the other basket. 
# This can be done if 
# we start with the second letter: ['B', 'C', 'B', 'B', 'C']

import collections 


def solution(fruits):
    """"
    fruits (list)

    This problem follows the Sliding Window pattern 
    and is quite similar to 
    Longest Substring with K Distinct Characters.
    In this problem, we need to find 
    the length of the longest subarray 
    with no more than two distinct characters 
    (or fruit types!). 
    This transforms the current problem into 
    Longest Substring with K Distinct Characters where K=2.
    """
    window_start = 0 
    max_length = 0 
    fruit_frequency = collections.Counter()

    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        fruit_frequency[right_fruit] += 1

        ## shrink the sliding window 
        ## unitil we left "2" frutts in the final dic
        while len(fruit_frequency) > 2: ## k for the longest substring
            left_fruit = fruits[window_start]
            fruit_frequency[left_fruit] -= 1
            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]
            window_start += 1 ## shrink the window
        max_length = max(max_length, window_end - window_start + 1)
    return max_length

def main():
    print("Maximum number of fruits: " + str(solution(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(solution(['A', 'B', 'C', 'B', 'B', 'C'])))

main()

