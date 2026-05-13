class Solution:
    def cal(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        i, j = 0, 1
        water = 0
        count = 0
        while j < len(height):
            if height[j] >= height[i]:
                water += count
                count = 0
                i = j
            else:
                count += height[i] - height[j]
            j += 1
        return water

    def trap(self, height: List[int]) -> int:
        max_idx = 0
        for i in range(len(height)):
            if height[i] >= height[max_idx]:
                max_idx = i
        return self.cal(height[:max_idx + 1]) + self.cal(height[max_idx:][::-1])