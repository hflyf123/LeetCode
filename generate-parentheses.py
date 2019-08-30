# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

# 例如，给出 n = 3，生成结果为：

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/generate-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.list = []
        self._gen(0, 0, n, "")
        return self.list

    def _gen(self, left: int, right: int, n: int, result: str):
        """
        left: 已经用了多少左括号
        righ: 已经用了多少右括号
        result:当前括号序列
        """
        if left == n and right == n:
            self.list.append(result)
            return
        if left < n:
            self._gen(left + 1, right, n, result + "(")
        if left > right and right < n:
            self._gen(left, right + 1, n, result + ")")


    def generateParenthesis_1(self, n: int) -> List[str]:
        self.list = []
        self.generateOneByOne(n, n, "")
        return self.list
    
    def generateOneByOne(self, left: int, right: int, result: str):
        if left == 0 and right == 0:
            self.list.append(result)
            return 
        if left > 0:
            self.generateOneByOne(left - 1, right, result + "(")
        if right > left:
            self.generateOneByOne(left, right - 1, result + ")")

if __name__ == "__main__":
    so = Solution()
    print(so.generateParenthesis_1(3))
    