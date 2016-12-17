# Freddy/Fangyu
# 12/17/2016

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        aws=len(nums)-nums.count(val)
        print(aws)
        return aws
    removeElement(object,[3,2,2,3],3)
