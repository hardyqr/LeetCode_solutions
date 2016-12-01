# Fangyu
# 11/26/2016

def convert_10_2(x):
	result=''
	while x//2!=0:
		result=result+str(int(x)%2)
		x=x//2
	result=result+str(int(x)%2)
	length=len(result)
	for i in range(1,33-length):
		result=result+'0'
	return result                                                                                                                                                                    

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

class Solution:
	# @param n, an integer
	# @return an integer
	def reverseBits(self, n):
		result_1=convert_10_2(n)
		length=len(result_1)
		# print(result_1,length)
		result=convert_2_10(result_1)
		# print(result)
		return result
	# test
    # reverseBits(object,43261596)
