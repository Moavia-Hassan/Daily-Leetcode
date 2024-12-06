class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        total = 0
        output = 0
        banned.sort()
        length = len(banned)
        for value in range(1,n+1):
            if value not in banned:
                total += value
                if total > maxSum:
                    return output
                else:
                    output += 1
        return output