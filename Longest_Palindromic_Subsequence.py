class Solution:
    def recursive_path(self,s,i,j,dp):
        if dp[i][j] != None:
            print("Here we use:",i,j,dp[i][j])
            return dp[i][j]
        if i > j:
            return 0
        if i == j:
            return 1
        if s[i] == s[j]:
            dp[i][j] = self.recursive_path(s, i+1, j-1, dp) + 2
        else:
            dp[i][j] = max(self.recursive_path(s, i+1, j, dp), self.recursive_path(s, i, j-1, dp))
        return dp[i][j]
            
    def longestPalindromeSubseq(self, s):
        dp = []
        for i in range(len(s)):
            dp.append([None]*len(s))
        return self.recursive_path(s, 0, len(s)-1, dp)
            
        """
        :type s: str
        :rtype: int
        """
