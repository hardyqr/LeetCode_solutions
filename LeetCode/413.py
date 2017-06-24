# Freddy/Fangyu
# 12/12/2016

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        length=len(A)
        if length<3:return 0
        i=1
        while i < length-1:
            if A[i]-A[i-1] == A[i+1]-A[i]:
                i+=1
            else:
                print('not')
                return 0
        return (1+length-2)*(length-2)/2
    numberOfArithmeticSlices(object,[1,2,3,4])
