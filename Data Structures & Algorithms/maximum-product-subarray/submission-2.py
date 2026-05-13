class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = -float('inf')
        for i in range(len(nums)):
            tmp = 1
            for j in range(i, len(nums)):
                tmp = tmp * nums[j]
                max_product = max(max_product, tmp)
        return max_product