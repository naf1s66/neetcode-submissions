class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)
        pointer = 1
        for i in range(start, end):
            if i > 0 and i < end and nums[i] != nums[i - 1]:
                nums[pointer] = nums[i]
                pointer += 1
                
        return pointer