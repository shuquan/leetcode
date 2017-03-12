# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        pre_n_th = n_th = tail = head
        i = 0

        if head.next is None:
            return None

        while n > 1:
            tail = tail.next
            n -= 1

        while tail.next is not None:
            tail = tail.next
            n_th = n_th.next
            if i > 0:
                pre_n_th = pre_n_th.next
            i += 1

        if n_th == pre_n_th:
            return head.next
        else:
            pre_n_th.next = n_th.next
            return head

    def removeNthFromEnd2(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
