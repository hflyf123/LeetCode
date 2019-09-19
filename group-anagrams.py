# 49 字母异位分词
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

# 示例:

# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# 说明：

# 所有输入均为小写字母。
# 不考虑答案输出的顺序。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/group-anagrams
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from collections import defaultdict

class Solution(object):
    def groupAnagrams1(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 创建一个value内容为list的字典
        res = defaultdict(list)
        for s in strs:
            # key使用tuple,如果是异位词,所使用的字母的元组排序后应该是相同的
            res[tuple(sorted(s))].append(s)
        return res.values()

    def groupAnagrams2(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return res.values()


if __name__ == "__main__":
    so = Solution()
    so.groupAnagrams1( ["eat", "tea", "tan", "ate", "nat", "bat"])
