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


class Solution:
  '''
  Time Complexity: O(N) to build a traversal by visiting every node
  Space Complexity: O(N) to keep an inorder traversal
  '''
  def kthSmallestRecursive(self, root, k):
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


  '''
  Time complexity:
    Leetcode:
      O(H + k), where H is a tree height. This complexity is defined by the stack, which contains at least H + k elements,
      since before starting to pop out one has to go down to a leaf. This results in O(log N + k)for the balanced tree and O(N + k) 
      for completely unbalanced tree with all the nodes in the left subtree.

    Bem:
      Since we are visiting every element in the tree one by one, worst case, O(N). Best case O(1), Average Case O(K)

  Space complexity: 
    Leetcode: 
       O(H) to keep the stack, where H is a tree height. That makes O(N) in the worst case of the skewed tree, and O(log N) in the average case of the balanced tree.
  '''
  def kthSmallestIterative(self, root, k):
    stack = []
    curr = root
    n = 0

    while curr or stack:
      while curr: # go as far left as we can and add the values into the stack
        stack.append(curr)
        curr = curr.left
      curr = stack.pop() # base case
      n += 1
      if n == k:
        return curr.val
      
      curr = curr.right
    
node4 = TreeNode(4, None, None)
node2 = TreeNode(2, None, None)
node1 = TreeNode(1, None, node2)
root = TreeNode(3, node1, node4)

sol = Solution()
print(sol.kthSmallestIterative(root, 5))




