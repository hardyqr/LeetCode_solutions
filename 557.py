# Feb 26, 2018 @DP

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = s.split(' ')
        res = ''
        for word in ss:
            res = res + word[::-1] + ' '
        return res[:-1]

