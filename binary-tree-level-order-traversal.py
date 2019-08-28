# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：

# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
from typing import List
import collections

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = []

    def levelOrder_bfs(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = collections.deque()
        queue.append(root)

        # 图需要加已经访问的节点,来减少重复操作
        # visited = set(root)
        while queue:
            level_size = len(queue)
            current_level = []
            for item in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result

    def levelOrder_dfs(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.result = []
        self._dfs(root, 0)
        return self.result

    def _dfs(self, node: TreeNode, level: int) -> List:
        if not node:
            return
        if len(self.result) < level + 1:
            self.result.append([])
        self.result[level].append(node.val)

        self._dfs(node.left, level + 1)
        self._dfs(node.right, level + 1)


if __name__ == "__main__":
    root = TreeNode(6)
    first = TreeNode(2)
    second = TreeNode(8)
    third = TreeNode(0)
    fourth = TreeNode(4)
    fifth = TreeNode(7)
    sixth = TreeNode(9)
    seventh = TreeNode(3)
    eighth = TreeNode(5)
    root.left = first
    root.right = second
    first.left = third
    first.right = fourth
    second.left = fifth
    second.right = sixth
    fourth.left = seventh
    fourth.right = eighth
    so = Solution()
    print(so.levelOrder_dfs(root))
