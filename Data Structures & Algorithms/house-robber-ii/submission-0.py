class Solution:
    def check_rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        for i in range(0, len(nums)):                        
            tmp = b
            b = max(a + nums[i], b)
            a = tmp
        return b
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.check_rob(nums[0:-1]), self.check_rob(nums[1::]))