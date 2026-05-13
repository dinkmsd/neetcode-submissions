class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        check_dup = set()
        for i in range(len(nums)):
            if nums[i] in check_dup:
                return True

            check_dup.add(nums[i])
            if i >= k:
                check_dup.remove(nums[i - k])

        return False
