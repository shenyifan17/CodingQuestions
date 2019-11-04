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

class Solution(object):
    """"
    This solution decomposed problem into 
    threeSum 

    740ms 
    """
    def threeSum(self, nums, target):   
        """"
        Note not exactly the same with 
        threeSum, previous threeSum:
        nums[i] + nums[j] + nums[k] = 0 

        This version: 
        nums[i] + nums[j] + nums[k] = target
        
        nums (list) 
        target (int)
        """
        res = []
        nums.sort()
        if len(nums) < 3:
            return res

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: continue
            j, k = i + 1, len(nums) - 1
            while j < k :
                s = nums[i] + nums[j] + nums[k] - target 
                if s == 0:
                    res.append([nums[i] ,nums[j] ,nums[k]])
                    j += 1; k -= 1
                    while j < k and nums[j] == nums[j - 1]: 
                        j += 1
                    while j < k and nums[k] == nums[k + 1]: 
                        k -= 1
                elif s < 0 :
                    j += 1
                else: # elif s > 0:
                    k -= 1
        return res    

    def fourSum(self, nums, target):
        results = []
        nums.sort()
        for i in range(len(nums) - 3):
            print('=================', i)
            if i == 0 or nums[i] != nums[i-1]:
                print('three sum nums:', nums[i+1:], 'target', target-nums[i])
                threeResult = self.threeSum(nums[i+1:], target-nums[i])
                for item in threeResult:
                    results.append([nums[i]] + item)
        return results 
