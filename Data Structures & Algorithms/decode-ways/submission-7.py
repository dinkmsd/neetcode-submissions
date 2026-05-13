class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == 0:
            return 0

        dp = {}

        def dfs(i: int) -> int:
            if i == len(s):
                return 1

            if s[i] == '0':
                return 0
            if dp.get(i) is not None:
                return dp[i]
            res = dfs(i + 1)

            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                res += dfs(i + 2)
            dp[i] = res
            return res
        
        return dfs(0)