class TreeNode:
  def __init__(self, val = 0, left = next, right = next):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def diameterOfBinaryTree(self, root: TreeNode):
    def dfs(root):
      nonlocal diameter
      if root is None:
        return 0
      
      left = dfs(root.left)
      right = dfs(root.right)
      diameter = max(left + right, diameter)

      return max(left, right) + 1
    
    diameter = 0
    dfs(root)
    return diameter

'''
Example 1)
    1
   / \
null null 

Max Diameter = 0

left_height = 0
right_height = 0
diameter = max(left + right, diameter)

return 1 + max(left, right)

'''
#root = TreeNode(5, None, None)


'''
Example
      1
    /  \
  2     null

Max Diameter = 1

  left_height = 1
  right_height = 0

  diameter = max(left + right, diameter)

  return 
'''
node2 = TreeNode(2, None, None)
root = TreeNode(1, node2, None)

sol = Solution()
print(sol.diameterOfBinaryTree(root))
