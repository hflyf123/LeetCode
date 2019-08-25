# 二叉树的遍历
# Pre-order: root-left-right
# In-order: left-root-right
# post-order: left-right-root


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.traverse_path = []

    def pre_order(self, root: 'TreeNode') -> list:
        if root:
            self.traverse_path.append(root.val)
            self.pre_order(root.left)
            self.pre_order(root.right)

    def in_order(self, root: 'TreeNode') -> list:
        if root:
            self.in_order(root.left)
            self.traverse_path.append(root.val)
            self.in_order(root.right)

    def post_order(self, root: 'TreeNode') -> list:
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            self.traverse_path.append(root.val)


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
    root.post_order(root)
    print(root.traverse_path)


    