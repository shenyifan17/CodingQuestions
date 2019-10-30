class Solution(object):

    # Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
    # Note:
    # The solution set must not contain duplicate triplets.
    # Example:
    # Given array nums = [-1, 0, 1, 2, -1, -4],
    # 
    # A solution set is:
    # [
    #   [-1, 0, 1],
    #   [-1, -1, 2]
    # ]
    def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        if len(nums) < 3:
            return res

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: continue
            j, k = i + 1, len(nums) - 1
            while j < k :
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    res.append([nums[i] ,nums[j] ,nums[k]])
                    j += 1; k -= 1
                    while j < k and nums[j] == nums[j - 1]: 
                        print(j,k)
                        j += 1
                    while j < k and nums[k] == nums[k + 1]: 
                        print(j,k)
                        k -= 1
                elif s < 0 :
                    j += 1
                else: # elif s > 0:
                    k -= 1
        return res    