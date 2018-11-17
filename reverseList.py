# 反转一个单链表。

# 示例:

# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head != None:
            list_node = []
            temp_node = head
            while True:
                if temp_node.next != None:
                    list_node.append(temp_node)
                    temp_node = temp_node.next
                else:
                    list_node.append(temp_node)
                    break
            for i in range(len(list_node) - 1, 0, -1):
                while i == 0:
                    break
                list_node[i].next = list_node[i-1]
            list_node[0].next = None
            return list_node[len(list_node) - 1]
        else:
            return None


class BestSolution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev


bs = BestSolution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
print(bs.reverseList(node1).val)
