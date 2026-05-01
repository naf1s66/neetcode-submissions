class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        fixed, left, right = 0, 1, len(nums) - 1
        
        
        set = []
        for fixed in range(0, len(nums) - 2):
            if fixed > 0 and nums[fixed] == nums[fixed - 1]:
                continue
            target = -nums[fixed]
            
            left = fixed + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    set.append([nums[fixed], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return set
                
