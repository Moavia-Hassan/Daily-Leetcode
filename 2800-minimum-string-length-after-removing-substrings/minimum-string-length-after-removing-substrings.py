class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for val in s:
            if stack:
                if stack[-1] == 'A' and val == 'B':
                    stack.pop()
                    continue
                if stack[-1] == 'C' and val == 'D':
                    stack.pop()
                    continue
            stack.append(val)

        return len(stack)























        # stack = []
        # for i in s:
        #     if stack:
        #         if stack[-1] == "A" and i == 'B':
        #             stack.pop()
        #             continue
        #         elif stack[-1] == "C" and i == "D":
        #             stack.pop()
        #             continue
        #     stack.append(i)
        # return len(stack)