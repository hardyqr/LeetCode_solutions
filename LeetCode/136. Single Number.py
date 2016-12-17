# Freddy/Fangyu@BNU
# 12/17/2016

'''Solution 1'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        for num in nums:
            res=res^num
        return res
'''Solution 2'''
class Solution(object):
    def singleNumber(self, nums):
        return reduce(lambda x,y:x^y, nums)
