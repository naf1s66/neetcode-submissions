class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        pointer = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                continue
            else: 
                nums[pointer] = nums[i]
                pointer += 1
        for zero in range(pointer, len(nums)):
            nums[zero] = 0