
#   二进制求和
# 给定两个二进制字符串，返回他们的和（用二进制表示）。

# 输入为非空字符串且只包含数字 1 和 0。

# 示例 1:

# 输入: a = "11", b = "1"
# 输出: "100"
# 示例 2:

# 输入: a = "1010", b = "1011"
# 输出: "10101"



class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        res = str(bin(a + b))[2:]
        return res

if __name__ == "__main__":
    soul = Solution()
    print(soul.addBinary("11", "1"))

        

