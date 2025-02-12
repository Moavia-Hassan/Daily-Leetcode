class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consectives = 0
        max_consectives = 0
        for i in nums:
            if i == 1:
                consectives += 1
            else:
                max_consectives = max(max_consectives,consectives)
                consectives = 0
        max_consectives = max(max_consectives,consectives)
        return max_consectives