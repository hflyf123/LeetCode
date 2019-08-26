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
        self.traverse_path_pre = []
        self.traverse_path_in = []
        self.traverse_path_post = []

    def pre_order(self, root: 'TreeNode') -> list:
        if root:
            self.traverse_path_pre.append(root.val)
            self.pre_order(root.left)
            self.pre_order(root.right)
        return self.traverse_path_pre

    def in_order(self, root: 'TreeNode') -> list:
        if root:
            self.in_order(root.left)
            self.traverse_path_in.append(root.val)
            self.in_order(root.right)
        return self.traverse_path_in


    def post_order(self, root: 'TreeNode') -> list:
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            self.traverse_path_post.append(root.val)
        return self.traverse_path_post



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
    print(root.pre_order(root))
    print(root.in_order(root))
    print(root.post_order(root))



    