# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

# 说明：本题中，我们将空字符串定义为有效的回文串。
import re


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        s = re.findall("[a-zA-Z0-9]*", s)
        new_s = ""
        for c in s:
            new_s += c
        new_s = new_s.lower()
        if new_s == new_s[::-1]:
            return True
        else:
            return False


so = Solution()
print(so.isPalindrome("A man, a plan, a canal: Panama"))
print(so.isPalindrome("0p"))