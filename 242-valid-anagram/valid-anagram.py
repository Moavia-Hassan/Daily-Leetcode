class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in s:
            if i in t:
                t = t.replace(i,"",1)
        
        if len(t) == 0:
            return True
        else:
            return False