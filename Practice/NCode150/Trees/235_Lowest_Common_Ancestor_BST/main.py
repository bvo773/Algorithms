'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia:
 “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”
'''

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


# Time Complexity : O(N), we are visiting each node until we find its common ancestor
# Space Compexity: O(1)
class Solution:
  def lowestCommonAncestor(self, root, p, q):
    cur = root
    while cur:
      if p.val < cur.val and q.val < cur.val: # p and q are in the left subtree
        cur = cur.left
      elif p.val > cur.val and q.val > cur.val: # p and q are in the right subtree
        cur = cur.right
      else:
        return cur # we found the split of the common ancestor

  def lca(self, root, node1, node2):
    if not root:
      return None
    
    # when we find the node 
    if root is node1 or root is node2:
      return root
    
    check_left = self.lca(root.left, node1, node2)
    check_right = self.lca(root.right, node1, node2)

    # 4 cases
    # check_left is not None, check_right is not None
    if check_left and check_right: # two different subtrees exist
      return root
    
    # check_left is None, check_right is None (this cannot happen because the nodes exist somewhere)

    # check_left is not None, check_right is None
    if check_left:
      return check_left

    # check_left is None, check_right is not None
    if check_right:
      return check_right   

    
'''
Example Tree for iterative solution
node9 = TreeNode(9, None, None)
node7 = TreeNode(7, None, None)
node5 = TreeNode(5, None, None)
node3 = TreeNode(3, None, None)
node4 = TreeNode(4, node3, node5)
node0 = TreeNode(0, None, None)
node8 = TreeNode(8, node7, node9)
node2 = TreeNode(2, node0, node4)
root = TreeNode(6, node2, node8)
p = node7
q = node9
'''

'''
# Example Tree for recursive solution A 
node5 = TreeNode(5, None, None)
node3 = TreeNode(3, None, None)
node1 = TreeNode(1, None, None)
node7 = TreeNode(7, node5, None)
node2 = TreeNode(2, node1, node3)
root = TreeNode(4, node2, node7)

p = node2
q = node7
'''
node5 = TreeNode(5, None, None)
node3 = TreeNode(3, None, None)
node1 = TreeNode(1, None, None)
node2 = TreeNode(2, node1, node3)
root = TreeNode(4, node2, node5)

p = node1
q = node3
sol = Solution()
print(sol.lca(root, p, q).val)
