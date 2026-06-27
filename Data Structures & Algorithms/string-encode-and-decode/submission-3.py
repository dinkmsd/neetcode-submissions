class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s))) # 5#Hello5#World
            res.append("#")
            res.append (s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            len_s = int(s[i:j]) # s[0:1] = 5
            res.append(s[j + 1:j + 1 + len_s]) # s[2:7]
            i = j + 1 + len_s
        return res

        