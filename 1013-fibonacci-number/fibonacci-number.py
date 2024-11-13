class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 2 or n==1:
            return 1
        left = 0
        right = 1
        Fn = 1
        for i in range(n):
            if i == 0:
                continue
            temp = Fn
            Fn = left + right
            left = temp
            right = Fn
            # print(Fn)
        return Fn
            

        