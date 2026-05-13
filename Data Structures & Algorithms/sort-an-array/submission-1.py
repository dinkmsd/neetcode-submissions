class Solution:
    def partition(self, arr, low, high):
        import random
        pivot_idx = random.randint(low, high)
        arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort(self, arr, low, high):
        while low < high:
            p = self.partition(arr, low, high)
            if p - low < high - p:
                self.quick_sort(arr, low, p - 1)
                low = p + 1
            else:
                self.quick_sort(arr, p + 1, high)
                high = p - 1

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums