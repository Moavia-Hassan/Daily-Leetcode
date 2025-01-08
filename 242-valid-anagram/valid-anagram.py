class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count = defaultdict(int)

        for char in s:
            count[char] += 1

        for char in t:
            count[char] -= 1

        for val in count.values():
            if val != 0:
                return False
        
        return True
        