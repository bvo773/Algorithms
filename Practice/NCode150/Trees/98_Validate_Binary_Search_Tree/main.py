# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
Runtime: O(N), We are visiting each node exactly once and check if the node is valid between the min and max value
Space Complexity: O(N) to keep runtime stack for each recursive call to visit each node
'''
class Solution:
    def isValidBST(self, root) -> bool:
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

    # Runtime O(N) - Fast
    def isValidBSTNC(self, root):
      def valid(node, mini, maxi):
        if not node:
          return True
        
        if not (node.val > mini and node.val < maxi):
          return False
        
        return (valid(node.left, mini, node.val) and 
          valid(node.right, node.val, maxi))
      
      return valid(root, float('-inf'), float('inf'))

node6 = TreeNode(6, None, None)
node3 = TreeNode(3, None, None)
node4 = TreeNode(4, node3, node6)
node1 = TreeNode(1, None, None)
root = TreeNode(5, node1, node4)

sol = Solution()
print(sol.isValidBST(root))
