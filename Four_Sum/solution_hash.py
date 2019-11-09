# Given an array nums of n integers and an integer target, 
# are there elements a, b, c, and d in nums such that 
# a + b + c + d = target? 
# Find all unique quadruplets in the array 
# which gives the sum of target.
# Note:
# The solution set must not contain duplicate quadruplets.
# Example:
# Given array nums = [1, 0, -1, 0, -2, 2], 
# and target = 0.
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

def fourSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    nums.sort()
    dic = collections.defaultdict(set)
    res = set() ## tried list, but doestnt work
                ## list end up with multiple solution
    ## eg:
    ## res = set()
    ## res.add(tuple([1,2]))
    ## res.add(tuple([1,2]))
    ## res = {(1,2)}

    ## res = []
    ## res.append([1,2])
    ## res.append([1,2])
    ## res = [[1,2], [1,2]]
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            sum = nums[i] + nums[j]
            for half in dic[target - sum]:
                ## decompose as two sum, it target - num exists, record it
                ## with nums[i], nums[k]
                res.add(tuple(list(half) + [nums[i], nums[j]]))
                
        for k in range(i):
            ## save the half results before i in the set 
            dic[nums[i] + nums[k]].add((nums[k], nums[i]))
            
    return list(res)




