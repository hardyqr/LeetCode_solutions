# Freddy/Fangyu
# 12/17/2016

class Solution(object):
    def twoSum(self, nums, target):
        i=0
        while i < len(nums):
            j=i+1
            while j < len(nums):
                if nums[i]+nums[j]==target:
                    return [i,j]
                j+=1
            i+=1
