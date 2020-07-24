import unittest
from serialize_and_deserialize_binary_tree import (
    Codec,
    TreeNode,
)


class SerializeAndDeserializeTest(unittest.TestCase):
    def _check_tree_is_the_same(self, tree_one: TreeNode, tree_two: TreeNode):
        if tree_one.val != tree_two.val:
            return False
        else:
            if tree_one.left:
                self._check_tree_is_the_same(tree_one.left, tree_two.left)
            if tree_one.right:
                self._check_tree_is_the_same(tree_two.right, tree_two.right)

    def test_encode_decode(self):
        root = TreeNode(1)
        two = TreeNode(2)
        three = TreeNode(3)
        four = TreeNode(4)
        five = TreeNode(5)
        root.left = two
        root.right = three
        two.left = four
        two.right = five

        c = Codec()

        deserialized_root = c.deserialize(c.serialize(root))
        self.assertTrue(self._check_tree_is_the_same(root, deserialized_root))
