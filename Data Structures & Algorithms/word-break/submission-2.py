class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s) # 8
        dp = {}
        def dfs(i: int):
            if i == n:
                return True
            if dp.get(i) == False:
                return False
            for word in wordDict: # ['neet', 'code']
                word_len = len(word)
                if i + word_len <= n and s[i:i+word_len] == word:
                    if dfs(i + word_len):
                        return True
            dp[i] = False
            return False
        return dfs(0)