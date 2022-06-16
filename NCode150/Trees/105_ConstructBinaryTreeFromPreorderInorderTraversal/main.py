'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree 
and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Example 1
        3
       / \
      9  20
         / \
        15  7 
Input: preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
Output: [3, 9, 20, null, null, 15, 7]

Constraints:

 * 1 <= preorder.length <= 3000
 * inorder.length == preorder.length
 * -3000 <= preorder[i], inorder[i] <= 3000
 * preorder and inorder consist of unique values.
 * Each value of inorder also appears in preorder.
 * preorder is guaranteed to be the preorder traversal of the tree.
 * inorder is guaranteed to be the inorder traversal of the tree.
'''

class TreeNode:
  def __init__(self, val = 0, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

class Solution:

  # Runtime and space complexity: O(N^2), i think this solution might be O(N^2) since we use the index function
  # But the time and space complexity are both O(n^2) because of the inorder.index() function and passing subarrays of preorder/inorder in each stack of the recursion
  def buildTree(self, preorder, inorder):
    if not preorder or not inorder: #we don't have to construct(create) a tree since it is null
      return None
    
    #otherwise we create a TreeNode from the  1st value in the preorder array
    root = TreeNode(preorder[0])
    #then we find position of it in the inorder array, the value tells us how many values we want in the left subtree
    mid = inorder.index(preorder[0])
    # then we build the left subtree, starting at index 1 since we already build the root node up to mid + 1, in python mid + 1 is not inclusive, basically from 1 to mid
    root.left = self.buildTree(preorder[1 : mid + 1], inorder[ :mid])
    # then we build the right subtree, every values from from the right of mid until the endo the array
    root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
    return root

  def buildTreeTrace(self, preorder, inorder):
    if not preorder or not inorder:
      return None
    
    root = TreeNode(preorder[0])
    print(f"Creating Node: {preorder[0]}\n")
    mid = inorder.index(preorder[0])
    print(f"Mid: {mid}\n")
    print(f"Left Subtree Partition | Preorder: {preorder[1 : mid + 1]} | Inorder: {inorder[ :mid]}\n")
    root.left = self.buildTreeTrace(preorder[1:mid + 1], inorder[:mid])
    print(f"Right Subtree Parition | Preorder: {preorder[mid + 1: ]} | Inorder: {inorder[mid + 1 : ]}\n")
    root.right = self.buildTreeTrace(preorder[mid+1:], inorder[mid+1:])
    return root


def pre_order(root):
  if not root:
    return None
  
  print(root.val, end=' ')
  pre_order(root.left)
  pre_order(root.right)

def in_order(root):
  if not root:
    return None
  
  in_order(root.left)
  print(root.val, end=' ')
  in_order(root.right)

def post_order(root):
  if not root:
    return None
  
  post_order(root.left)
  post_order(root.right)
  print(root.val, end=' ')

sol = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
tree = sol.buildTreeTrace(preorder, inorder)
pre_order(tree)



node7 = TreeNode(7, None, None)
node15 = TreeNode(15, None, None)
node20 = TreeNode(20, node15, node7)
node9 = TreeNode(9, None, None)
root = TreeNode(3, node9, node20)


# print("PRE-ORDER TRAVERSAL")
# pre_order(root)
# print()

# print("IN-ORDER TRAVERSAL")
# in_order(root)
# print()

# print("POST-ORDER TRAVERSAL")
# post_order(root)
# print()