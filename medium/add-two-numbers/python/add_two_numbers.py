# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i = 0
        j = 0
        l1_val = 0
        l2_val = 0
        while l1 is not None:
            l1_val = l1_val + l1.val * pow(10, i)
            i = i + 1
            l1 = l1.next
        while l2 is not None:
            l2_val = l2_val + l2.val * pow(10, j)
            j = j + 1
            l2 = l2.next
        l3_val = l1_val + l2_val
        n = 1
        while l3_val / pow(10, n) != 0:
            n = n + 1
        l3_array = []
        for i in reversed(xrange(n)):
            val = l3_val/pow(10, i)
            l3_array.append(ListNode(val))
            l3_val = l3_val - val * pow(10, i)
        l3_array.reverse()
        l3 = l3_array[0]
        for i in xrange(len(l3_array) - 1):
            l3_array[i].next = l3_array[i + 1]

        return l3

    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        carry = 0
        root = p = ListNode(0)
        while l1 or l2 or carry:
            val = carry
            if l1:
                val = val + l1.val
                l1 = l1.next
            if l2:
                val = val + l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            p.next = ListNode(val)
            p = p.next
        return root.next
