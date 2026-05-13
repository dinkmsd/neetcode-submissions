class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for i in range(len(strs[0])):
            flag = True
            for s in strs:
                if i < len(s):
                    flag = flag and strs[0][i] == s[i]
                else:
                    flag = False
                    break
            if flag == True:
                res += strs[0][i]
            else:
                break
        return res