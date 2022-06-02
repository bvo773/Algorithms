# Least Common Ancestor
# Given a tree, and two nodes in the tree, find their least common ancestor
# Clarify with interviewer
# - does parent reference exist?
# - are node 1 and node 2 not null and actulally present in the tree (in this case, we assume they exist)

# three cases
# 1: assuming you have parent reference, binary tree (Hint: We know Root is LCA node1 and node2 have the fist same common ancestor )
# 2: assuming no parent refernce, binary search tree (Hint: We know Root is LCA if_val_interval = node1.val < current node < node2.val)
# 3: assuming no parent reference, binary tree  (Hint: We know Root is LCA if node1 and node2 are on different subtrees)


class TreeNode:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

# Case 3: Assuming no parent reference, binary tree
def lca(root, node1, node2):
  if not root:
    return None
  
  if root is node1 or root is node2:
    return root
  
  check_left = lca(root.left, node1, node2)
  check_right = lca(root.right, node1, node2)

  if check_left and check_right:
    return root
  
  if check_left:
    return check_left
  
  if check_right:
    return check_right
  