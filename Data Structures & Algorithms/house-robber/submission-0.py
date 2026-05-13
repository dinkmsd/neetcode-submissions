class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for i in range(0, len(nums)):                        
            tmp = b
            b = max(a + nums[i], b)
            a = tmp
        return b