class Solution:
    def longestPalindrome(self, s: str) -> str:
        l, r = 0, 0
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for j in range(n - 1, -1, -1):
            for i in range(j, n):
                if (i == j or i - 1 == j or dp[i - 1][j + 1] == 1) and s[i] == s[j]:
                    dp[i][j] = 1
                
                if dp[i][j] == 1 and r - l < i - j:
                    r = i
                    l = j

        return s[l:r + 1]