import unittest
from linked_list_cycle_ii import Solution
from linked_list_cycle_ii import ListNode

class TestLinkedListCycelII(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_1(self):
	"""
	[3,2,0,-4]
	tail connects to node index 1
	"""
        node_0 = self.build_linked_list([3,2,0,-4],1)
	result = self.s.detectCycle3(node_0)
	self.assertEqual(result, node_0.next)

    def test_2(self):
	"""
        [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]
        tail connects to node index 24
	"""
        node_0 = self.build_linked_list([-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5],24)
	result = self.s.detectCycle3(node_0)
        for i in range(24):
            node_0 = node_0.next
	self.assertEqual(result, node_0)

    def build_linked_list(self, array, index):
        for k,v in enumerate(array):
            if k == 0:
                pre = ListNode(v)
                start = pre
            if k == index:
                head = pre
            if k == len(array) - 1:
                tail = pre
            if k + 1 < len(array):
                next = ListNode(array[k + 1])
                pre.next = next
            pre = next
        tail.next = head
        return start

    def tearDown(self):
        self.s = None
