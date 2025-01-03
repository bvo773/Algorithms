import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
    
  # Time Complexity: O(N), visiting every node at each level once
  # Space Comlexity: O(N/2) -> O(N), for each level, the maxinum number of nodes in our queue will hold is n/2
  # Algorithm: Breadth First Search Level Order Traversal
  def levelOrder(self, root):
    result = [] # to store our sublists result at each level
    q = collections.deque() # Our queue - FIFO - append right, pop left
    q.append(root) 
    
    while q:
      qLen = len(q)
      level = []
      for i in range(qLen):
        node = q.popleft() # when pop, we have to add its children
        if node:
          level.append(node.val)
          q.append(node.left)
          q.append(node.right)
      if level:
          result.append(level)
            
    return result

root = TreeNode(7, None, None)
solution = Solution()
solution.levelOrder(root)