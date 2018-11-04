class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """     
    def longestCommonSubstring(self, A, B):
        if len(A) == 0 or len(B) == 0:
            return 0
        dp = []; max_length = 0; max_str = ""
        for i in range(len(A)):
            line = []
            for j in range(len(B)):
                if A[i] == B[j]:
                    line.append(1); max_length = 1; max_str = A[i]
                else:
                    line.append(None)
            dp.append(line)
        for index_1 in range(1, len(A)):
            for index_2 in range(1, len(B)):
                if dp[index_1-1][index_2-1]!=None and A[index_1] == B[index_2]:
                    dp[index_1][index_2] = dp[index_1-1][index_2-1] + 1
                    max_length = max(max_length, dp[index_1][index_2])
        return max_length
