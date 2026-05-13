class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = set(s)
        max_len = 0
        for char in char_set:
            l, r = 0, 0
            count = k
            while r < len(s):
                if s[r] != char:
                    count -= 1
                if count < 0:
                    if s[l] != char:
                        count += 1
                    l += 1
                r += 1
            
            max_len = max(max_len, r - l)
        return max_len
