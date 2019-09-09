# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

# k 是一个正整数，它的值小于或等于链表的长度。

# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

# 示例 :

# 给定这个链表：1->2->3->4->5

# 当 k = 2 时，应当返回: 2->1->4->3->5

# 当 k = 3 时，应当返回: 3->2->1->4->5

# 说明 :

# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        node_list = []
        while head:
            node_list.append(head)
            head = head.next
        times = len(node_list) // k
        tmp = []
        for i in range(0, times):
            res = []
            res = node_list[i * k : i * k + k]
            res.reverse()
            tmp += res
        other  = node_list[times * k:]
        tmp += (other)
        for j in range(0, len(tmp) - 1):
            tmp[j].next = tmp[j + 1]
        tmp[-1].next = None
        head = tmp[0]
        return head

    # 递归做法
    def reverseKGroup2(self, head: ListNode, k: int) -> ListNode:
        cur = head
        count = 0
        while cur and count!= k:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroup2(cur, k)
            while count:
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
                count -= 1
            head = cur   
        return head

if __name__ == "__main__":
    list_node1 = ListNode(1)
    list_node2 = ListNode(2)
    list_node3 = ListNode(3)
    list_node4 = ListNode(4)
    list_node5 = ListNode(5)
    list_node1.next = list_node2
    list_node2.next = list_node3
    list_node3.next = list_node4
    list_node4.next = list_node5
    so = Solution()
    print(so.reverseKGroup2(list_node1, 2))