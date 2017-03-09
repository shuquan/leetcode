# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        joint = head
        slow = head
        quick = head
        while True:
            if slow is None:
                return None
            if quick is None:
                return None
            if slow.next is None:
                return None
            if quick.next is None or quick.next.next is None:
                return None
            slow = slow.next
            quick = quick.next.next

            if slow is quick:
                if quick is joint:
                    return joint
                while joint is not quick:
                    quick = quick.next
                    while quick is not slow:
                        if quick is joint:
                            return joint
                        quick = quick.next
                    joint = joint.next

        return None

    def detectCycle2(self, head):
        """
	Refer to Floyd's cycle-finding algorithm
	https://en.wikipedia.org/wiki/Cycle_detection#Floyd.27s_Tortoise_and_hare
	http://stackoverflow.com/questions/2936213/explain-how-finding-cycle-start-node-in-cycle-linked-list-work

        :type head: ListNode
        :rtype: ListNode
        """
        joint = head
        slow = head
        quick = head
        while True:
            if slow is None:
                return None
            if quick is None:
                return None
            if slow.next is None:
                return None
            if quick.next is None or quick.next.next is None:
                return None
            slow = slow.next
            quick = quick.next.next

            if slow is quick:
                while joint is not quick:
                    joint = joint.next
                    quick = quick.next
                return joint

        return None

    def detectCycle3(self, head):
        """
        Refer to Brent's algorithm

        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return None
        slow = head
        quick = slow.next
        length = i = 1
        while True:
            while length < pow(2, i):
                if slow is quick:
                    slow = quick = head
                    for j in range(length):
                        quick = quick.next
                    while slow is not quick:
                        slow = slow.next
                        quick = quick.next
                    return slow
                elif quick.next is None:
                    return None
                else:
                    quick = quick.next
                    length += 1
            i += 1
            length = 1
            slow = quick
            quick = slow.next
