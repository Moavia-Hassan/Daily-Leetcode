class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even = 0
        count = 0
        for i in nums:
            while i != 0:
                even += 1
                i = i //  10
            if even % 2 == 0:
                count += 1
            even = 0
        return count