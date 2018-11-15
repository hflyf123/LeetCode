#   删除链表的倒数第N个节点
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

# 示例：

# 给定一个链表: 1->2->3->4->5, 和 n = 2.

# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：

# 给定的 n 保证是有效的。

# 进阶：

# 你能尝试使用一趟扫描实现吗？

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        list = []
        current_node = head
        while True:
            if current_node.next != None:
                list.append(current_node)
                current_node = current_node.next
            else:
                list.append(current_node)
                break
        delete_node = list[len(list) - n]
        if len(list) == 1:
            return None
        if delete_node.next == None:
            list[len(list)-2].next = None
        else:
            delete_node.val = delete_node.next.val
            delete_node.next = delete_node.next.next
        return head

node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
# node3 = ListNode(3)
# node4 = ListNode(4)
# node5 = ListNode(5)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# # node = node1
# while True:
#     if node.next != None:
#         print(node.val)
#         node = node.next
#     else:
#         print(node.val)
#         break

so = Solution()
head = so.removeNthFromEnd(node1, 1)
print(head.val, head.next)
node = node1
while True:
    if node.next != None:
        print(node.val)
        node = node.next
    else:
        print(node.val)
        break
