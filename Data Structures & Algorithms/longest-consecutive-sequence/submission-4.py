class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        nums.sort()
        max_len = 1
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                curr += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                curr = 1
            max_len = max(curr, max_len)
        return max_len