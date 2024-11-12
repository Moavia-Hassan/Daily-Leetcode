class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
                if i == '*':
                    stack.pop()
                    continue
                stack.append(i)
                #stack
        return "".join(stack)