class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            tmp = b
            b = b + a
            a = tmp
        return b