class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        add = 0
        for i in range(len(nums)):
            add += nums[i] 
            output.append(add)

        return output