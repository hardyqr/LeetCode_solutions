# Freddy/Fangyu
# 12/18/2016

# Freddy @BH
# 1/30/2018

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        aws=[]
        for num in nums:
            if num!=0:
                aws.append(num)
        for i in range(nums.count(0)):
            aws.append(0)
        for i in range(len(nums)):
            nums[i]=aws[i]
        
