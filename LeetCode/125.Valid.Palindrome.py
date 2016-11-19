class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rt////////////////////////////////////////ype: bool
        """
        s='shit'
        s=s.repalce(' ','')
     

        delset=s.punctuation
        s=line.translate(None,delset)
        length=len(s)
        left=s[length/2:]
        right=s[:-length/2][::-1]
        print(left,right)
        if left==right:
            return True
        else:
            return False
        isPalindrome(shit)