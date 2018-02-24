# Freddy @DP
# Feb 23, 2018

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        D = [1] * n
        for i in range(0,n):
          for j in range(0,i+1):
            if (nums[i] > nums[j]):
              D[i] = max(D[i],1+D[j])
        return max(D)
