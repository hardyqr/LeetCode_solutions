# Freddy @DP
# Feb 23, 2018

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m,n = len(word1),len(word2)
        D = [[0 for x in range(n+1)] for y in range(m+1)] 
        for i in range(0,m+1):
          D[i][0] = i
        for j in range(0,n+1):
          D[0][j] = j
        for i in range(1,m+1):
          for j in range(1,n+1):
            if(word1[i-1] == word2[j-1]):
              p = 0
            else:
              p = 1
            D[i][j] = min(D[i-1][j]+1,D[i][j-1]+1,D[i-1][j-1]+p)       
        return D[-1][-1]
