class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n
        for i in range(n - 1, -1, -1):
            max_count = 0
            for j in range(i + 1, n):
                if nums[j] > nums[i] and memo[j] > max_count:
                    max_count = memo[j] 
            memo[i] = max_count + 1
        return max(memo)