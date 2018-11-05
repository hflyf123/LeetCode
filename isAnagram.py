# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t) or len(set(s)) != len(set(t)) or set(s) != set(t):
            return False
        if s == t:
            return True
        dict1 = {}
        dict2 = {}
        for ch in s:
            if ch not in dict1:
                dict1[ch] = 1
            else:
                dict1[ch] += 1
        for ch in t:
            if ch not in dict2:
                dict2[ch] = 1
            else:
                dict2[ch] += 1
        for i in range(0, len(s)):
            if dict1[s[i]] != dict2[s[i]]:
                return False
            else:
                return True
    

so = Solution()
print(so.isAnagram('aacc', 'ccac'))

# class Solution:
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         m = 'qwertyuiopasdfghjklzxcvbnm'
#         for i in m:
#             if str.count(s,i)!=str.count(t,i):
#                 return False
#         return True