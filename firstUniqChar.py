# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is not None:
            for c in s:
                if s.count(c) < 2:
                    return s.index(c)
            return -1
        else:
            return -1
        
                
so = Solution()
print(so.firstUniqChar("sselff"))
                
