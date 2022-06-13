# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Time Compelxity: O(P + Q), the size of both trees added together, worst case we iterate through every single node in both trees
Space Complexity: O(P + Q) to keep run time stack 
'''

class TreeNode:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def isSameTree(self, p, q) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    
    is_root_same = p.val == q.val
    is_left_subtree_same = self.isSameTree(p.left, q.left) 
    is_right_subtree_same = self.isSameTree(p.right, q.right) 
    
    return (is_root_same and is_left_subtree_same and is_right_subtree_same)

node3_p = TreeNode(3, None, None)
node1_p = TreeNode(1, None, None)
root_p = TreeNode(2, node1_p, node3_p)

node3_q = TreeNode(3, None, None)
node1_q = TreeNode(1, None, None)
root_q = TreeNode(2, node1_p, node3_p)

sol = Solution()

print(sol.isSameTree(root_p, root_q))


