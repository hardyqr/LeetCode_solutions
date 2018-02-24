# Fangyu
# 11/26/2016

from functools import reduce


'''
class Solution(object):
	def maxProduct(self, nums):
		results=[]
		count=1
		length=len(nums)
		while count<=length:
			counter=0
			while counter+count<=length:
				aset=nums[counter:counter+count]
				counter=counter+1
				m=reduce(lambda x,y:x*y,aset)
				results.append(m)
				# print(m)
			count=count+1
		result=max(results)
		return result
	# maxProduct(object,[123,56,2,8,-1,3,-4,66])

def e_m(l):
	if len(l)==0:return 0
	else:return reduce(lambda x,y:x*y,l)

class Solution(object):
	def maxProduct(self, nums):
		results=[]
		length=len(nums)
		ne_indexes=[]
		zero_index=[]
		for num in nums:
			if num<0:
				ne_indexes.append(nums.index(num))
			if num==0:
				zero_index.append(nums.index(num))
		if len(zero_index)!=0:
			i=1
			count=0
			for e in nums:
				if nums[-1]==0:
					results.append(0)
				if e==0 and nums[-1]!=0:
					i=nums[count+1]
				else:
					i=i*e
					results.append(i)
				count+=count
			print(max(results))
			return max(results)
		if len(ne_indexes)!=1 and len(ne_indexes)%2==0:
			result=e_m(nums)
			print(result)
			return result
		else:
			if len(ne_indexes)==len(nums):
				if len(nums)==1:return nums[0]
				else:
					print(nums[1:],nums[:-1])
					result=max(e_m(nums[1:]),e_m(nums[:-1]))
					print(result)
					return result
			else:
				print(nums[ne_indexes[0]+1:],nums[:ne_indexes[-1]],nums[ne_indexes[0]+1:ne_indexes[-1]])
				result=max(e_m(nums[ne_indexes[0]+1:]),e_m(nums[:ne_indexes[-1]]),e_m(nums[ne_indexes[0]+1:ne_indexes[-1]]))
				print(result)
				return result
	maxProduct(object,[-5,0,2])
	#maxProduct(object,[123,56,2,8,-1,3,-4,66,-9,22,55])
	maxProduct(object,[-2])
	maxProduct(object,[0])
'''

''' DP '''
''' Feb 23, 2018 @DP '''
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # suffix product
        Dmax = [None] * n
        Dmin = [None] * n 
        Dmax[0],Dmin[0] = nums[0],nums[0]
        for i in range(1,n):
          if (nums[i] > 0):
            Dmax[i] = max(nums[i], Dmax[i-1]*nums[i])
            Dmin[i] = min(nums[i], Dmin[i-1]*nums[i])
          else:
            Dmax[i] = max(nums[i], Dmin[i-1]*nums[i])
            Dmin[i] = min(nums[i], Dmax[i-1]*nums[i])
        return max(Dmax)
