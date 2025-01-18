import collections

class TreeNode:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

class Solution: 
  # Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
  """
  Example 1:
        1   <-
       / \
      2   3  <-
       \   \
        5   4 <-
  
  Input: root = [1,2,3,null, 5, null, 4]
  Output: [1,3,4]

  Example 2: root = [1, null, 3]
             Output: [1,3] 
  
  Example 3: root = []
             Output: []

  Time Complexity: O(N), we traverse every node at each level once and try to find the right most node
  Space Complexity: O(H), where H is the tree height, at any given time there are H nodes in our queue.           
  """
  def rightSideView(self, root) -> int:
    res = []
    q = collections.deque([root]) # our queue initialized with root initially, and root could be null so our queue could have null values | we are popping element from the element, and adding element to the right

    while q:
      rightSide = None
      qLen = len(q) # traverse up to the number of items in our current queue/level | our queue at any given point contains one level at a time | going to be updated

      #for every element in this level (up to q length)
      for i in range(qLen): 
        node = q.popleft()
        # we know the node can be null, so we can put a condition to check, if it is null we can go to the next iteration of the loop. 
        if node: 
          rightSide = node # after the entire loop is done executing, the last node in the last level will be our rightside node
          q.append(node.left)
          q.append(node.right)
      
      if rightSide: #if rightSide is not null, append it to result
        res.append(rightSide.val) # result append the right side
    
    return res 
root = TreeNode(3)
solution = Solution()
solution.rightSideView(root)
