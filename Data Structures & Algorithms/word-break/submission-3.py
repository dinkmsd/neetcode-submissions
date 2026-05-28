class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s) # 8
        memo = {
            n: True
        }
        def dfs(i: int):
            if i in memo:
                return memo[i]
            for w in wordDict: # ['neet', 'code']
                if i + len(w) <= n and s[i:i+len(w)] == w:
                    if dfs(i + len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        return dfs(0)