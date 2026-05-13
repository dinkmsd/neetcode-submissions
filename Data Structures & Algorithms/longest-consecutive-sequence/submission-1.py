class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_set = set(nums)
        longest = 0
        for item in new_set:
            if item - 1 not in new_set:
                length = 1
                while (item + length) in new_set:
                    length += 1
                longest = max(length, longest)

        return longest