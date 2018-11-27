# 请判断一个链表是否为回文链表。

# 示例 1:

# 输入: 1->2
# 输出: false
# 示例 2:

# 输入: 1->2->2->1
# 输出: true
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
import operator


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        list_node = []
        if head == None:
            return True
        current_node = head
        while current_node.next != None:
            list_node.append(current_node.val)
            current_node = current_node.next
        list_node.append(current_node.val)
        if len(list_node) % 2 == 0:
            if operator.eq(list_node, list_node[::-1]):
                return True
            else:
                return False
        else:
            return False

list_node1 = ListNode(1)
list_node2 = ListNode(2)
list_node3 = ListNode(2)
list_node4 = ListNode(1)
list_node1.next = list_node2
list_node2.next = list_node3
list_node3.next = list_node4
so = Solution()
print(so.isPalindrome(list_node1))

