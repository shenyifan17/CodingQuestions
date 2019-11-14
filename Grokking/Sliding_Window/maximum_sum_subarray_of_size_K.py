# Problem Statement
# Given an array of positive numbers and a positive number ‘k’, 
# find the maximum sum of any contiguous subarray of size ‘k’.
# 
# Example 1:
# 
# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].
# Example 2:
# 
# Input: [2, 3, 4, 1, 5], k=2 
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].

def solution_brute_force(k, arr):
    """"
    arr (list)
    k (int)

    Brute force solution, sliding window
    Time complexity O(N*K)
    """
    max_sum = 0 
    window_sum = 0 

    for i in range(len(arr) - k + 1):
        window_sum = 0
        for j in range(i, i+k):
            window_sum += arr[j]
        max_sum = max(max_sum, window_sum)

    return max_sum 

#  If you observe closely, 
#  you will realize that 
#  to calculate the sum of a contiguous subarray 
#  we can utilize the sum of the previous subarray. 
#  For this, c
#  onsider each subarray 
#  as a Sliding Window of size ‘k’. 
#  To calculate the sum of the next subarray,
#   we need to slide the window ahead by one element. 
#   So to slide the window forward and calculate 
#   the sum of the new position of the sliding window,
#   we need to do two things:
#  Subtract the element going out of the sliding window 
#  i.e., subtract the first element of the window.
#  Add the new element getting included in the sliding window 
#  i.e., the element coming right after the end of the window.
#  This approach will save us from re-calculating 
#  the sum of the overlapping part of the sliding window. 
#  Here is what our algorithm will look like:

def solution_better(k, arr):
    """"
    Time complexity O(N)
    """
    max_sum, window_sum = 0, 0
    window_start = 0 

    for window_end in range(len(arr)):
        window_sum += arr[window_end] ## add the next element 
        # slide window 
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start] # subtract element going out
            window_start += 1
    return max_sum 


if __name__ == "__main__":

    print("Maximum sum of a subarray of size K: " + str(solution_brute_force(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(solution_brute_force(2, [2, 3, 4, 1, 5])))

    print("Maximum sum of a subarray of size K: " + str(solution_better(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(solution_better(2, [2, 3, 4, 1, 5])))