# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Runtime: O(N), We are visiting each node exactly once and check if the node is valid between the min and max value
Space Complexity: O(N) to keep runtime stack for each recursive call to visit each node
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
      def recurse(root, mini, maxi):
        if not root:
          return True
        
        is_val_interval = root.val > mini and root.val < maxi
        
        if is_val_interval:
          is_root_valid = True
        else:
          is_root_valid = False
          
        if is_root_valid:
          check_left = recurse(root.left, mini, root.val)
          check_right = recurse(root.right, root.val, maxi)
        
        return (is_root_valid and check_left and check_right)
      
      return recurse(root, float('-inf'), float('inf'))