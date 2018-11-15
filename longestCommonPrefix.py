# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 ""。

# 示例 1:

# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:

# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:

# 所有输入只包含小写字母 a-z 。

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        length_str = len(strs[0])
        index = 0
        for i in range(len(strs)):
            if len(strs[i]) < length_str:
                length_str = len(strs[i])
                index = i
        res = ""
        for j in range(len(strs[index])):
            for str in strs:
                if str[j] == strs[index][j]:
                    continue
                else:
                    return res
            res += strs[index][j]
        return res

so = Solution()
so.longestCommonPrefix(["flower","flow","flight"])
        



        
            

                   
