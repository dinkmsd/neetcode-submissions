class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        a, b = 1, 1
        for i in range(1, n):
            tmp = b
            b = a + b
            a = tmp
        return b