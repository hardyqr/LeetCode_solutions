# Freddy @DP
# Feb 23, 2018


''' DP '''
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if(n==0): return 0
        D = [nums[0]]*n
        for i in range(1,n):
          D[i] = max(nums[i], D[i-1]+nums[i])
        return max(D)
        
