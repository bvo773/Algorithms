class TreeNode:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right


def in_order(root):
  if root == None:
    return
  in_order(root.left)
  print(root.val)
  in_order(root.right)

def pre_order(root):
  if root == None:
    return 
  print(root.val)
  pre_order(root.left)
  pre_order(root.right)

def post_order(root):
  if root == None:
    return
  post_order(root.left)
  post_order(root.right)
  print(root.val)

node1 = TreeNode(1, None, None)
node2 = TreeNode(3, None, None)
root = TreeNode(2, left = node1, right = node2)
#in_order(root)
#pre_order(root)
#post_order(root)