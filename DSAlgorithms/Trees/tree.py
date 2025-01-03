class TreeNode:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right


'''
Given a binary tree, determine if a binary tree is balanced.
Definition: A binary tree is balanced if, for every node, the height of the left and right subtree differ by at most one.
'''
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

''' 
Write a function to calculate number of steps/edges to the leaf node or the maximum depth of a tree
'''
def tree_height(root):
  if root == None:
    return 0

  height_left = tree_height(root.left)
  height_right = tree_height(root.right)
  return 1 + max(height_left, height_right)

'''
Write a function that checks if a binary tree is a binary search tree. 
'''

def is_binary_search_tree(root):
  def recurse(root, minimum, maximum):
    if not root:
      return True
    is_val_in_interval = (root.val > minimum and root.val < maximum)
    if is_val_in_interval:
      check_left = recurse(root.left, minimum, root.val)
      check_right = recurse(root.right, root.val, maximum)
      return check_left and check_right
    else:
      return False
  
  return recurse(root, float("-inf"), float("inf"))



'''
node3 = TreeNode(3, None, None)
node2 = TreeNode(1, None, None)
root = TreeNode(2, left = node2, right = node3)
print(is_binary_search_tree(root))
'''

