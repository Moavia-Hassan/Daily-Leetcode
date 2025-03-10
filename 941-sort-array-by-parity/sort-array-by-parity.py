class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        swap = 0
        i = 1
        while i < len(nums):
            if nums[swap] %2 == 0:
                swap += 1
                i += 1
            elif nums[i] % 2 == 0:
                nums[i], nums[swap] = nums[swap] , nums[i]
                i+= 1
                swap += 1
            else:
                i += 1
        
        return nums