# April 16, 2018 @M3

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort() # quicksort
        return nums[-k]

