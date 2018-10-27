# 给定一个 32 位有符号整数，将整数中的数字进行反转。

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            y = str(x)
            y = y[::-1]
            y = int(y)
        else:
            y = str(abs(x))
            y = y[::-1]
            y = "-" + y
            y = int(y)

        if y not in range(-2 ** 31,2 ** 31 - 1):
            return False
        else:
            return y
        


solution = Solution()
solution.reverse(-321)
