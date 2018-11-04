class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def recursive_path(self, i, j, A, B, dp):
        if dp[i][j] != None:
            return dp[i][j]
        if i == 0 or j == 0:
            if A[i] == B[j]:
                return 1
            return 0
        if A[i] == B[j]:
            dp[i][j] = self.recursive_path(i-1, j-1, A, B, dp) + 1
        else:
            dp[i][j] = max(self.recursive_path(i-1, j, A, B, dp), self.recursive_path(i, j-1, A, B, dp))
        return dp[i][j]
    def longestCommonSubsequence(self, A, B):
        if len(A)==0 or len(B)==0:
            return 0
        dp = []
        for i in range(len(A)):
            dp.append([None]*len(B))
        return self.recursive_path(len(A)-1, len(B)-1, A, B, dp)
        
