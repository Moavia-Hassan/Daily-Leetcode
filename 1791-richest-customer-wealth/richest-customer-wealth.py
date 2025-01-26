class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        total = 0
        max1 = 0
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                total += accounts[i][j]
            max1 = max(max1, total)
            total= 0
        
        return max1