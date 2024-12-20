class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = defaultdict(int)
        for item in nums:
            if item %2==0:
                seen[item] += 1
        maxx = 0
        output = -1
        for element, count in seen.items():
            if count > maxx:
                maxx, output = count, element
            elif count == maxx:
                output = min(element, output)
            
        return output