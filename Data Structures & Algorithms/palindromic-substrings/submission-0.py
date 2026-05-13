class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = n
        for i in range(n):
            for j in range(i + 1, n):
                a, b = i, j
                while a < b and s[a] == s[b]:
                    a += 1
                    b -= 1
                if a >= b:
                    count += 1
        return count
