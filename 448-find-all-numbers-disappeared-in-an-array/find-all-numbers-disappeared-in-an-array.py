class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nums = set(nums)
        i = 1
        output = []
        while i <= n:
            if i not in nums:
                output.append(i)
            i+=1
        
        return output

