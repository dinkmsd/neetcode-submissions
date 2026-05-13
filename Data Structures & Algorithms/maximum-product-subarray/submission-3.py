class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[1] * len(nums) for _ in range(len(nums))]
        max_product = -float('inf')
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if i != j:
                    dp[i][j] = nums[i] * dp[i+1][j]
                else:
                    dp[i][j] = nums[i]
                max_product = max(dp[i][j], max_product)
        return max_product