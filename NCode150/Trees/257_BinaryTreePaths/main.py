class TreeNode:
  def __init__(self, val = 0, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def binaryTreePaths(self, root):
    def create_paths(node, path):
      if not node:
        return None
      
      path += str(node.val)

      if not node.left and not node.right:
        paths.append(path)
      else:
        path += "->"
        create_paths(node.left, path)
        create_paths(node.right, path)
    
    paths = []
    create_paths(root, '')
    return paths