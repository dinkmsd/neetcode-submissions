class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        zero_count = 0
        product = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
                if zero_count == 2:
                    return nums
            else:
                product *= nums[i]

        for i in range(len(nums)):
            if zero_count != 0:
                if nums[i] == 0:
                    output[i] = product
            else:
                output[i] = int(product / nums[i])

        return output