"""
Algorithm

- Build a hashmap to record the relation of value -> index for inorder, so that we can find the position of root in constant time.
- Initialize an integer variable preorderIndex to keep track of the element that will be used to construct the root.
- Implement the recursion function arrayToTree which takes a range of inorder and returns the constructed binary tree:
    - if the range is empty, return null;
    - initialize the root with preorder[preorderIndex] and then increment preorderIndex;
    - recursively use the left and right portions of inorder to construct the left and right subtrees.
- Simply call the recursion function with the entire range of inorder.


"""


class TreeNode:
  def __init__(self, val = 0, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def buildTree(self, preorder, inorder):
    inorder_hashmap = {}
    for i in range(len(inorder)):
      inorder_hashmap[inorder[i]] = i

    def array_to_tree(left, right):
      nonlocal preorder_index
      # if there are no elements to construct the tree
      if left > right:
        return None

      # select the preorder_index element as the root and increment it after we build it
      root = TreeNode(preorder[preorder_index])
      preorder_index += 1

      # build left and right subtree
      # excluding the inorder_hashmap[root_value] element because it's the root
      root.left = array_to_tree(left, inorder_hashmap[root.val] - 1)
      root.right = array_to_tree(inorder_hashmap[root.val] + 1, right)

      return root
    
    preorder_index = 0
    return array_to_tree(0, len(preorder) - 1)


def in_order(root):
  if not root:
    return None
  
  in_order(root.left)
  print(root.val, end = " ")
  in_order(root.right)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
sol = Solution()
tree = sol.buildTree(preorder, inorder)
in_order(tree)
