# 有效的字母异位词
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false
# 说明:
# 你可以假设字符串只包含小写字母。
#
# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

# 解法1:排序
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)

# 解法2:Map计数


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for i in s:
            s_dict[i] = s_dict.get(i, 0) + 1
        for j in t:
            t_dict[j] = t_dict.get(j, 0) + 1
        return t_dict == s_dict


if __name__ == '__main__':
    soul = Solution()
    print(soul.isAnagram("aacc", "cacc"))



