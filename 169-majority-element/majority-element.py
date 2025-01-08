class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        records = {}
        for num in nums:
            if num in records:
                records[num]+=1
            else:
                records[num] = 1
            if records[num]>len(nums)//2:
                return num