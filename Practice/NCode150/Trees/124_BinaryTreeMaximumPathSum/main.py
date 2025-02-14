"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. "Note that the path does not need to pass through the root."

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:
          1
         / \
        2   3
Input: root = [1, 2, 3]
Output: 6
Explanation: The optimal path is 2->1->3 with a path sum of 2 + 1 + 3 = 6.

Example 2:
        -10
        / \
       9   20
          /  \
         15   7

Input: root = [-10, 9, 20, null, null, 15, 7] 
Output: 42
Explanation: The optimal path is 15 ->20->7 with a path sum 15 -> 20 -> 7 with a path sum of 15+20+7 = 42


ALGORITHM
We understand a path can be defined 4 following ways.

A node by itself is a path.
    [9]

A node going/splitting left
    [20]
    /
  [15]

A node going/splitting right
    [20]
       \
       [7]

A node spltting boths way, basically starting from left or right and crossing through the root node
    [20]
    /  \
  [15] [7]

ALGORITHM
For each node we calculate all 4 of these paths and we keep a maxPath variable to keep track the most optimal path out of these 4 
paths.

RUNTIME
Time Complexity: O(N), we traverse each node once to check what is its maxPath out of all the 4 paths.
Space Complexity: O(H), where H is the height of the tree for our recursive call stack, and O(N) worse case if the tree is unbalanced
"""
class TreeNode:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right 

class Solution:
  def maxPathSum(self, root) -> int:
    maxPath = float('-inf')

    def dfs(root):
      nonlocal maxPath
      if not root:
        return 0

      left = dfs(root.left)
      right = dfs(root.right)

      maxPath = max(maxPath, root.val, root.val + left, root.val + right, left + root.val + right)

      # 3 possibilies and we get the max 
      return max(root.val, root.val + left, root.val + right)

    dfs(root)
    return maxPath

node7 = TreeNode(7, None, None)
node15 = TreeNode(15, None, None)
node20 = TreeNode(20, node15, node7)
node9 = TreeNode(9, None, None)
root = TreeNode(-10, node9, node20)

solution = Solution()
result = solution.maxPathSum(root)
print(result)