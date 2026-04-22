class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        left_product = 1
        right_product = 1
        for i in range(0, len(nums)):
            output.append(left_product)
            left_product *= nums[i]


        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]

        return output



        