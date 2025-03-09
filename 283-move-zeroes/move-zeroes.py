class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        writer = 0
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[writer] = nums[writer], nums[i]
                writer += 1
            i += 1

        return nums
                