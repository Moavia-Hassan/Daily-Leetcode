class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## SOLUTION 01
        # t = sorted(t)
        # s = sorted (s)

        # return t[:] == s[:]
        
        ## SOLUTION 02

        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True