class TreeNode:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

# TODO: Given the root, write a function to print the list inorder
def print_inorder(root):
  if not root:
    return
  print_inorder(root.left)
  print(root.val)
  print_inorder(root.right)

def print_preorder(root):
  if not root:
    return
  print(root.val)
  print_preorder(root.left)
  print_preorder(root.right)

def print_postorder(root):
  if not root:
    return
  
  print_postorder(root.left)
  print_postorder(root.right)
  print(root.val)

def tree_height(root):
  if not root:
    return 0
  
  left_subtree = tree_height(root.left)
  right_subtree = tree_height(root.right)
  return 1 + max(left_subtree, right_subtree)

  

'''
      4
    /   \
   2      5
  / \   /  \
 1   3  6   7
'''
node1 = TreeNode(1)
node3 = TreeNode(3)
node2 = TreeNode(2, node1, node3)

node6 = TreeNode(6)
node7 = TreeNode(7)
node5 = TreeNode(5, node6, node7)

root = TreeNode(4, node2, node5)


#print_inorder(root)
#print_preorder(root)
#print_postorder(root)

print(tree_height(root))