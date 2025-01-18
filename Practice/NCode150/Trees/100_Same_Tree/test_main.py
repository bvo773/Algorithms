
import unittest
from main import Solution, TreeNode



'''
     2        2
    / \      / \
   1   3     1  3
     p         q
'''
node3_p = TreeNode(3, None, None)
node1_p = TreeNode(1, None, None)
root_p = TreeNode(2, node1_p, node3_p)

node3_q = TreeNode(3, None, None)
node1_q = TreeNode(1, None, None)
root_q = TreeNode(2, node1_p, node3_p)


'''
    4
   / \
  3   5
 /
1
'''
node5_m = TreeNode(5, None, None)
node1_m = TreeNode(1, None, None)
node3_m = TreeNode(3, node1_m, None)
root_m = TreeNode(4, node3_m, node5_m)

node5_n = TreeNode(5, None, None)
node1_n = TreeNode(1, None, None)
node3_n = TreeNode(3, node1_m, None)
root_n = TreeNode(4, node3_m, node5_m)

solution = Solution()
class TestSameTree(unittest.TestCase):

  def test_same_tree(self):
    assert(True == solution.isSameTree(root_p, root_q))
    assert(True == solution.isSameTree(root_m, root_n))

#python -m unittest test_main or python -m unittest
  
