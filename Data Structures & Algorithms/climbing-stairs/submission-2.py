class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def dfs(n):
            if n <= 1:
                return 1
            if dp.get(n) is not None:
                return dp.get(n)
            dp[n] =  dfs(n-1) + dfs(n-2)
            return dp[n]
        
        return dfs(n)