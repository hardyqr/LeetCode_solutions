# Freddy/Fangyu@BNU
# 12/25/2016


def convert_10_to_2(num,l):
    l+=str(num%2)
    if num//2==0:
        return l
    else:
        num//=2
        return convert_10_to_2(num,l)

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        l=''
        print(convert_10_to_2(x,l)[::-1],convert_10_to_2(y,l)[::-1])
        a=convert_10_to_2(x,l)[::-1]
        b=convert_10_to_2(y,l)[::-1]
        length=max(len(a),len(b))
        for zero in range(length-min(len(a),len(b))):
            
        mark=[]
        for i in range(0,)):
            if a[i]==b[i]:
                pass
            else:
                mark.append(i)
        print(mark)
p=Solution()
p.hammingDistance(1,4)
