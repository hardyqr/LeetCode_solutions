# Freddy @DP
# Feb 23, 2018

class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        m,n = len(A),len(B)
        D = [[0 for x in range(m+1)] for y in range(n+1)] 

        # base cases
        for i in range(0,m+1):
            D[i][0] = 0
        for j in range(0,n+1):
            D[0][j] = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if (A[i-1] != B[j-1]):
                    D[i][j] = max(D[i-1][j],D[i][j-1])
                else:
                    D[i][j] = max(D[i-1][j],D[i][j-1],D[i-1][j-1]+1)
        return D[-1][-1]
