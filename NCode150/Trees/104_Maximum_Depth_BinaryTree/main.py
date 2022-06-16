# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
To get the height of a tree and or the max depth of a tree,
get the max between the left subtree and right subtree + 1
'''
class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))