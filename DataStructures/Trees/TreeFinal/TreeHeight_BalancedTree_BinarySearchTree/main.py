class TreeNode:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

def tree_height(root):
  if not root:
    return 0
  
  height_left = tree_height(root.left)
  height_right = tree_height(root.right)
  max_height = max(height_left,height_right)
  return 1 + max_height

def is_balanced(root):
  if not root:
    return True
  
  height_left = tree_height(root.left)
  height_right = tree_height(root.right)
  difference = abs(height_left - height_right)
  if difference <= 1:
    is_root_balanced = True
  else:
    is_root_balanced = False
  
  is_left_subtree_balanced = is_balanced(root.left)
  is_right_subtree_balanced = is_balanced(root.right)
  return (is_root_balanced and is_left_subtree_balanced and is_right_subtree_balanced)

node6 = TreeNode(6, None, None)
node5 = TreeNode(5, None, None)
node0 = TreeNode(0, None, node5)
node4 = TreeNode(4, None, None)
node3 = TreeNode(3, None, node4)
node2 = TreeNode(2, node6, node3)
root = TreeNode(1, node0, node2)
print("Is balanced: ", is_balanced(root))