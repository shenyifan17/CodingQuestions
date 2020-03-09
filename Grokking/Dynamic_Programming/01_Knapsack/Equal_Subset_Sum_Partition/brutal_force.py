""""
Problem Statement #
Given a set of positive numbers, 
find if we can partition it into two subsets such that the sum of elements in both the subsets is equal.

Example 1: #
Input: {1, 2, 3, 4}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}
Example 2: #
Input: {1, 1, 3, 4, 7}
Output: True
Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}
Example 3: #
Input: {2, 3, 4, 6}
Output: False
Explanation: The given set cannot be partitioned into two subsets with equal sum.


this problem follows the 01_knapsack pattern

Assume if S represents the total sum of all the given numbers, 
then the two equal subsets must have a sum equal to S/2.
This essentially transforms our problem to: 
"Find a subset of the given numbers that has a total sum of S/2".

So our brute-force algorithm will look like:

for each number 'i' 
  create a new set which INCLUDES number 'i' if it does not exceed 'S/2', and recursively 
      process the remaining numbers
  create a new set WITHOUT number 'i', and recursively process the remaining items 
return true if any of the above sets has a sum equal to 'S/2', otherwise return false
"""

def can_partition(num):
	""""
	num (list)
	"""
	s = sum(num)
	# if "s" is an odd number, 
	# we cannot have two subsets with equal sum
	if s % 2 != 0:
		return False 
	return can_partition_recursive(num, s/2, 0)

def can_partition_recursive(num, sum, currentIndex):
	# base check:
	if sum == 0: ## as we see from below, we keep 
				 ## reducing sum, until it hits 1/2*sum(num)
		return True 
	
	n = len(num)
	if (n==0) or (currentIndex>=n):
		return False
	
	# recursive call after choosing the numebr 
	# at the "currentindex" 
	# if the number at ""currentIndex" exceeds the sum,
	# we shouldt process this 
	if num[currentIndex] <= sum: ## sum here is: sum = 1/2*sum(num)
		if (can_partition_recursive(num,
									sum-num[currentIndex],
									currentIndex+1)):
			return True 
	
	# recursive call after excluding the number	at the "currentIndexx"
	return can_partition_recursive(num, sum, currentIndex+1)

def main():
  	print("Can partition: " + str(can_partition([1, 2, 3, 4])))
  	print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
  	print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()


""""
Time complexity is O(2ˆn), and space comp is O(n)
"""
