# Freddy/Fangyu@BNU
# 12/18/2016


def counter(dic,nums,l):
    for i in nums:
        if i in dic:
            dic[i]+=1
            if dic[i]>=l//2+1:
                # print('yes')
                return i
        else:
            dic[i]=1
        # print(dic)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        l=len(nums)
        if l==1:return nums[0]
        return counter(dic,nums,l)
    majorityElement(object,[1,2,4,4,4,3,4,4,2,4,4,5])
