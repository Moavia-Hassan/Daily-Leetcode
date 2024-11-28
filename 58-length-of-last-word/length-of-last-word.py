class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list1 = s.split()
        return len(list1[-1])
        # string = ""
        # output = []
        # for char in s:
        #     if char != ' ':
        #         string += char
        #     else:
        #         if string != "":
        #             output.append(string)
        #             print(string)
        #         string = ""
        # return len(output[-1])
        # This lengthy code is not running but I don't know why.