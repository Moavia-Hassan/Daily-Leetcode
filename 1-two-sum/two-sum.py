class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    output.append(i)
                    output.append(j)
        print(output)
        return output