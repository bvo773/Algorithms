'''
Given a binary tree, determine if its height-balanced.

For this problem, a height-balanced binary tree is defined as:
  a binary tree in which the left and right subtrees of every node
  differ in height by no more than 1
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
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
      
