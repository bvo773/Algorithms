"""
Given an integer n, return any array containing n unique integers such that they add up to 0.

Example 1:
Input: n = 5
Output: [-7, -1, 1, 3, 4]
Explanation: These arrays also are accepted [-5, -1, 1, 2, 3] , [-3, -1, 2, -2, 4].

Example 2:
Input: n = 3
Output: [-1, 0, 1]

Example 3:
Input: n = 1
Output: [0]

n = 4
loop up to n/2


n = 3

[-1 1 0]
n = 6
[-1 1 -2 2 -3 3]
"""
class Solution:
  # Algorithm: We return an array where the values are symmetric (+x,-x), if n is odd, we add 0 
  # Time Complexity: O(N/2)
  # Space Complexity: O(N)
  def sumZero(self, n: int) -> List[int]:
    res = []
    length = int(n/2 + 1)
    for i in range(1, length):
        res.append(i)
        res.append(-i)
    
    if n % 2 == 1: res.append(0)
    return res

