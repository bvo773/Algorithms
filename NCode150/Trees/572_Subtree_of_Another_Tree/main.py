'''
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure 
and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
The tree tree could also be considered as a subtree of itself.


Time Compelexity: O (S * T), size of both trees together, for every single position in S, we compare that subtree to the entire T tree
'''

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val = 0, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
      if not t: return True # if the T tree is empty, it will be a a subtree of S regardless
      if not s: return False # if the S tree is empty, T can't be subtree of S
      
      # check if t and s are the same initially
      if self.sameTree(s,t):
        return True

      # if not, we can check/compare if T is a subtree of the left or right subtree of S. Only one subtrees has to be true
      return (self.isSubtree(s.left, t) or
      self.isSubtree(s.right, t))


    def sameTree(self, s, t): 
      # if both trees are empty
      if not s and not t:
        return True
      
      # if both trees are non empty, compare (check),if they have the same value,
      # and do this recursively for the left subtree and right subtree
      if s and t and s.val == t.val:
        return (self.sameTree(s.left, t.left) and
                self.sameTree(s.right, t.right))

      # return false if they are not equal or if one of the trees is empty
      return False

# Is T a subtree of S
'''
        S           T
        3           4
      /  \         / \
     4    5       1   2 
    / \
   1   2
'''
# S Tree 
node5 = TreeNode(5, None, None)
node2 = TreeNode(2, None, None)
node1 = TreeNode(1, None, None)
node4 = TreeNode(4, node1, node2)
root_s = TreeNode(3, node4, node5)


root_t = TreeNode(4, node1, node2)
node1 = TreeNode(1, None, None)
node2 = TreeNode(2, None, None)


sol = Solution()
print(sol.isSubtree(root_s, root_t))