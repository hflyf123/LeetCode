# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

#  

# 示例:

# 给定 1->2->3->4, 你应该返回 2->1->4->3.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        node_list = []
        while head:
            node_list.append(head)
            head = head.next
        for i in range(0, len(node_list) - 1, 2):
            node_list[i], node_list[i + 1] = node_list[i + 1], node_list[i]
        for j in range(0, len(node_list) - 1):
            node_list[j].next = node_list[j + 1]
        node_list[-1].next = None
        head = node_list[0]
        return head
    
    def swapPairs2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node_next = head.next
        head.next = self.swapPairs2(head.next.next)
        node_next.next = head
        return node_next
        

if __name__ == "__main__":
    list_node1 = ListNode(3)
    list_node2 = ListNode(2)
    list_node3 = ListNode(0)
    list_node4 = ListNode(-4)
    list_node1.next = list_node2
    list_node2.next = list_node3
    list_node3.next = list_node4
    so = Solution()
    print(so.swapPairs2(list_node1))