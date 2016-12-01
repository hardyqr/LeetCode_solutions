# Fangyu
# 11/26/2016

# not yet work
def convert_2_10(x):
	n=str(x)
	result=0
	n=int(n)
	count=len(str(n))-1
	n=str(n)
	for t in n:
		result=result+int(t)*(2**count)
		count=count-1
	return result                                                                                                                                                          


class Solution(object):
	def grayCode(self, n):
		"""
		:type n: int
		:rtype: List[int]
		"""
		result=''
		for i in range(1,n+1):
			for a in [0,1]:
				result=result+str(a)
		print(result)
		out=[]
		for x in result:
			out.append(convert_2_10(x))
		print(out)
		return out


	grayCode(object,5)