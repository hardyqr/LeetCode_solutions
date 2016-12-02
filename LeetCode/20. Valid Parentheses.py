def judge(s_1,s_2):
    if (s_1=='(' and s_2==')') or (s_1=='{' and s_2=='}') or (s_1=='[' and s_2==']'):
        return True
    else:return False

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2!=0:return False
        i=0
        while i < len(s):
            if judge(s[i],s[i+1]):
                i=i+2
            else:return False
        return True
    # isValid(object,'[')
    # isValid(object,"()[]{}")
