import re
class Solution(object):
    def isPalindrome(self, s):
        r='[ ’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
        s=re.sub(r,'',s) 
        s=s.lower()
        length=len(s)
        if(int(length//2)*2==length):
            left=s[0:length//2]
            right=s[length//2:][::-1]             
        if(int(length//2)*2!=length):
            length=length-1
            left=s[0:length//2]
            right=s[length//2+1:][::-1] 
        if left==right:return True
        else:return False
