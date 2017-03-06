import unittest
from invert_binary_tree import Solution
from invert_binary_tree import TreeNode

class TestInvertBinaryTree(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty_tree(self):
        result = self.s.invertTree(None)
        self.assertEqual(result, None)

    def test_tree_1(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)
        result = self.s.invertTree(root)
        self.assertEqual(self.pre_order(root), [4, 7, 9, 6, 2, 3, 1])

    def test_tree_2(self):
        root = TreeNode(2)
        result = self.s.invertTree(root)
        self.assertEqual(self.pre_order(root), [2])

    def test_tree_3(self):
        root = TreeNode(5)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        result = self.s.invertTree(root)
        self.assertEqual(self.pre_order(root), [5, 2, 1])

    def pre_order(self, root):
        pre_order = []
        stack = []
        stack.append(root)
        while len(stack) != 0:
            p = stack.pop()
            pre_order.append(p.val)
            if p.right is not None:
                stack.append(p.right)
            if p.left is not None:
                stack.append(p.left)
        return pre_order

    def tearDown(self):
        self.s = None
