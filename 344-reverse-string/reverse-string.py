class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place      instead.
        """
        # right = len(s) - 1
        # for left in range(len(s)):
        #     if left != right:     
        #         s[left], s[right] = s[right] , s[left]
        #         print(s)
        #         right -= 1
        # return s
        # why this for loop approach is not working

        l = 0
        r = len(s)-1
        while l < r:
            # s[l] , s[r] = s[r] , s[l]
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l, r = l+1 , r-1

