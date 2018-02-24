# Feb 22, 2018 @DP

''' exceed time limit '''
'''
def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    D = {}
    n = len(s)
    if(n==1):
        if(s in wordDict): return True
        else: return False
    for i in range(0,n+1):
        D[i] = False
    for i in range(0,n):
        subs = s[0:i+1]
        if (subs in wordDict):
            D[i+1] = True
        # else
        for j in range(0,i+1):
            if (D[j] and (s[j:i+1] in wordDict)):
                D[i+1] = True
                break
    return D[n]

d1 = {'wtf','is','going','on',''}
d2 = {''}
d3 = {'aa','aaaa'}
d4 = {'leet','code'}
print(wordBreak("wtfisgoingon",d1))
print(wordBreak("a",d2))
print(wordBreak("aaaaaaa",d3))
print(wordBreak("leetcode",d4))
'''

''' modified '''
''' Feb 23, 2018 @DP '''

class Solution:
  def wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    n = len(s) 
    D = [False] * (n+1)
    for i in range(0,n+1):
        subs = s[0:i]
        if (subs in wordDict):
            D[i] = True
        # else
        for j in range(0,i):
            if (D[j] and (s[j:i] in wordDict)):
                D[i] = True
                break
    return D[-1]
