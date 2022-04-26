class TreeNode:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right


'''
Given a binary tree, determine if 
'''
def is_balanced():
  pass

# number of steps/edges to the leaf node
def tree_height(root):
  if root == None:
    return 0

  left = tree_height(root.left)
  right = tree_height(root.right)
  max_height = max(left, right)
  return 1 + max_height

node3 = TreeNode(3, None, None)
node2 = TreeNode(1, None, None)
root = TreeNode(2, left = node2, right = node3)
print(tree_height(root))

'''
tree_height(root) 
  left = tree_height(root.left) -> 1
    left = tree_height(root.left) -> None 
      return 0
    right = tree_height(root.right) -> None
      return 0
    return max(left, right) + 1 -> 1


  right = tree_height(root.right) -> 1
    left = tree_height(root.left) -> None
      return 0
    right = tree_height(root.right) -> None
      return 0
    return max(left, right) + 1 -> 1

  return max(left, right) + 1 -> 2
'''
