# Freddy/Fangyu@BNU
# 12/20/2016

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        aws=[]
        for i in nums1:
            if i in nums2 and i not in aws:
                aws.append(i)
        return aws
