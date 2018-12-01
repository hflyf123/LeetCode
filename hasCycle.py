# 环形链表
# 给定一个链表，判断链表中是否有环。

# 进阶：
# 你能否不使用额外空间解决此题？
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        slow_node = head
        fast_node = head
        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
            if slow_node is fast_node:
                return True
        return False

        
list_node1 = ListNode(3)
list_node2 = ListNode(2)
list_node3 = ListNode(0)
list_node4 = ListNode(-4)
list_node1.next = list_node2
list_node2.next = list_node3
list_node3.next = list_node4
so = Solution()
print(so.hasCycle(list_node1))