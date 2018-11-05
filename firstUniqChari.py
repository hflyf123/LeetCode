# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        for ch in s:
            if ch not in dict:
                dict[ch] = 1
            else:
                dict[ch] += 1
        print(dict)
        for i in range(len(s)):
            if dict[s[i]] == 1:
                return i
        return -1

so = Solution()
print(so.firstUniqChar('leetcode'))


# class Solution:
#     def firstUniqChar(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         counter=[]
#         for i in 'qwertyuiopasdfghjklzxcvbnm':
#             if s.find(i)!=-1 and s.find(i)==s.rfind(i):
#                 counter.append(s.find(i))
#         if counter==[]:
#             return -1
#         else:
#             return min(counter)