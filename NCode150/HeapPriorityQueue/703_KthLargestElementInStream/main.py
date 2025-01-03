"""
Design a class to find the kth element in a stream. Note that it is the kth largest element in sorted order, 
not the kth distinct element.

Implememt KthLargest class:
  KthLargest(int k, int[] nums) Initializes the objext with the integer k and the stream of integers nums.
  int add(int val) Appends the integer val to the stream and returns the element respresenting the kth largest element in the stream.

Input
  ["KthLargest", "add", "add", "add", "add", "add"]
  [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

Output
  [null, 4, 5, 5, 8, 8]

Explanation
  KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
  kthLargest.add(3);   // return 4
  kthLargest.add(5);   // return 5
  kthLargest.add(10);  // return 5
  kthLargest.add(9);   // return 8
  kthLargest.add(4);   // return 8
"""

class KthLargest:
  def __init__(self, k: int, nums: List[int]):
    pass

  def add(self, val:int) -> int:
    pass