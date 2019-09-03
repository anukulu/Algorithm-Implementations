import unittest
from BinarySearchTree import BinarySearchTree

class BinarySearchTestcase(unittest.TestCase):
        def test_bst(self):
            bst = BinarySearchTree()

            bst.InsertNode(10)
            self.assertEqual(bst.size(),1)

            bst.InsertNode(20)
            self.assertEqual(bst.size(),2)

            bst.InsertNode(15)
            self.assertEqual(bst.size(),3)

            bst.InsertNode(30)
            self.assertEqual(bst.size(),4)

            self.assertListEqual(bst.Inorder(),[10,15,20,30])

            self.assertListEqual(bst.Preorder(),[10,20,15,30])

            self.assertListEqual(bst.Postorder(),[15,30,20,10])



if __name__ == "__main__":
    unittest.main()