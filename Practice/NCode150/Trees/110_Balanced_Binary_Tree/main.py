'''
Given a binary tree, determine if its height-balanced.

For this problem, a height-balanced binary tree is defined as:
  a binary tree in which the left and right subtrees of every node
  differ in height by no more than 1
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
  def isBalanced(self, root) -> bool:
    if not root:
      return True
    
    left_height = self.tree_height(root.left)
    right_height = self.tree_height(root.right)
    
    difference = abs(left_height - right_height)
    if difference <= 1:
      is_root_balanced = True
    else:
      is_root_balanced = False
    
    is_left_subtree_balanced = self.isBalanced(root.left)
    is_right_subtree_balanced = self.isBalanced(root.right)
    
    return (is_root_balanced and is_left_subtree_balanced and is_right_subtree_balanced)

  def tree_height(self, root):
    if not root:
      return 0
    
    return 1 + max(self.tree_height(root.left), self.tree_height(root.right))
  


  def isBalanced2(self, root) -> bool:
      if not root:
          return True
      
      left_height = self.tree_height(root.left)
      right_height = self.tree_height(root.right)
      root_balanced = True if abs(left_height - right_height) <= 1 else False
  
      return root_balanced and self.isBalanced(root.left) and self.isBalanced(root.right)
  
  def isBalancedNC(self, root):
    def dfs(root):
      if not root:
        return [True, 0]
      
      left = dfs(root.left)
      right = dfs(root.right)
      balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
      return [balanced, 1 + max(left[1], right[1])]

    return dfs(root)[0]
"""
        4
      /  \
     2    7
    /\
   1  3    
"""
node7 = TreeNode(7, None, None)
node3 = TreeNode(3, None, None)
node1 = TreeNode(1, None, None)
node2 = TreeNode(2, node1, node3) 
root = TreeNode(4, node2, node7)
sol = Solution()
sol.isBalanced2(root)