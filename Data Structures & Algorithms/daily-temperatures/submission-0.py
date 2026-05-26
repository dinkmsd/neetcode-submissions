class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        res = []
        for i in range(length):
            j = i
            while j < length and temperatures[j] <= temperatures[i]:
                j += 1
            if j < length:
                res.append(j - i)
            else:
                res.append(0)
        return res