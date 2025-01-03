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

# returns a list in order [left, root, right]
def in_order_list(root): 
  result = []
  def in_order(result, root):
    if root == None:
      return result
    in_order(result,root.left)
    result.append(root.val)
    in_order(result, root.right)
    return result
  
  return in_order(result, root)
  
def pre_order(root):
  if root == None:
    return 
  print(root.val)
  pre_order(root.left)
  pre_order(root.right)

# Returns a list pre-order [root, left, right]
def pre_order_list(root):
  result = []
  def pre_order(result, root):
    if root == None: #returns empty list return result
      return result
    result.append(root.val)
    pre_order(result, root.left)
    pre_order(result, root.right)
    
    return result

  pre_order(result, root)
  return result


def post_order(root):
  if root == None:
    return
  post_order(root.left)
  post_order(root.right)
  print(root.val)

# Returns a list post-order [left, right, root]
def post_order_list(root):
  result = []
  def post_order(result, root):
    if not root:
      return result
    
    post_order(result, root.left)
    post_order(result, root.right)
    result.append(root.val)
    return result

  post_order(result, root)
  return result


node1 = TreeNode(1, None, None)
node2 = TreeNode(3, None, None)
root = TreeNode(2, left = node1, right = node2)
l = post_order_list(root)
print(l)
#in_order(root)
#pre_order(root)
