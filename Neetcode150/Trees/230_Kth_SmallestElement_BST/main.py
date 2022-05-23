class TreeNode:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right


def print_inorder(root):
  if not root:
    return None
  
  print_inorder(root.left)
  print(root.val)
  print_inorder(root.right)

node4 = TreeNode(4, None, None)
node2 = TreeNode(2, None, None)
node1 = TreeNode(1, None, node2)
root = TreeNode(3, node1, node4)
#print_inorder(root)

class Solution:
  def kthSmallest(self, root, k):
    res = []
    
    def recurse(root, res):
      if not root:
        return
      
      recurse(root.left, res)
      res.append(root.val)
      recurse(root.right, res)
      return res
    
    result =  recurse(root, res)
    return result[k-1]

sol = Solution()
print(sol.kthSmallest(root, 1))
