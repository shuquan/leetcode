# Definition for singly-linked list.
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
        slow = head
        quick = head
        while True:
            if slow is None:
                return False
            if quick is None:
                return False
            if slow.next is None:
                return False
            if quick.next is None or quick.next.next is None:
                return False

            slow = slow.next
            quick = quick.next.next

            if slow is quick:
                return True

