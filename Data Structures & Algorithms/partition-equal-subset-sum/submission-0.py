class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        half = total // 2
        n = len(nums)
        def dfs(i, half):
            if i == n:
                return False
            if half < 0:
                return False
            if half == 0:
                return True

            return dfs(i + 1, half - nums[i]) or dfs(i+1, half)
        return dfs(0, half)