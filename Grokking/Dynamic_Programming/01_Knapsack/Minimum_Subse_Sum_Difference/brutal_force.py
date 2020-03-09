""""
Problem Statement #
Given a set of positive numbers, partition the set into two subsets 
with a minimum difference between their subset sums.

Example 1: #
Input: {1, 2, 3, 9}
Output: 3
Explanation: We can partition the given set into two subsets where minimum absolute difference 
between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.
Example 2: #
Input: {1, 2, 7, 1, 5}
Output: 0
Explanation: We can partition the given set into two subsets where minimum absolute difference 
between the sum of number is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.
Example 3: #
Input: {1, 3, 100, 4}
Output: 92
Explanation: We can partition the given set into two subsets where minimum absolute difference 
between the sum of numbers is '92'. Here are the two subsets: {1, 3, 4} & {100}.

Basic Solution #
This problem follows the 0/1 Knapsack pattern and can be converted into a Subset Sum problem.

Let’s assume S1 and S2 are the two desired subsets. A basic brute-force solution could be to try adding each element either in S1 or S2, to find the combination that gives the minimum sum difference between the two sets.

So our brute-force algorithm will look like:

for each number 'i' 
    add number 'i' to S1 and recursively process the remaining numbers
    add number 'i' to S2 and recursively process the remaining numbers
return the minimum absolute difference of the above two sets 
"""

def can_partition(num):
    return can_partition_recursive(num=num, 
                                   currentIndex=0, 
                                   sum1=0, 
                                   sum2=0)

def can_partition_recursive(num, currentIndex, sum1, sum2):
    # base check
    if currentIndex == len(num):
        return abs(sum1  - sum2)

    # recursive call after including the number at the currentIndex 
    # in the first set 
    diff1 = can_partition_recursive(num=num,
                                    currentIndex=currentIndex+1,
                                    sum1=sum1+num[currentIndex],
                                    sum2=sum2)
    diff2 = can_partition_recursive(num=num,
                                    currentIndex=currentIndex+1,
                                    sum1=sum1,
                                    sum2=sum2+num[currentIndex])
    return min(diff1, diff2)


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))

main()

# The time complexity of the above algorithm is exponential O(2^n)
# ​​where ‘n’ represents the total number. 
# The space complexity is O(n) which is used to store the recursion stack.
