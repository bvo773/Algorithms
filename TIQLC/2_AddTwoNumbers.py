"""
You are given two non-empty linked lists representing two non-negative integers. The digits
are stored in reverse order, and each of their nodes contains a single digit. Add
the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1)
 2->4->3

 5->6->4
 ========
 7->0->8

 Input: l1 = [2,4,3], l2 = [5,6,4]
 Output: [7,0,8]
 Explanation: 342 + 465 = 807
"""

class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next
class Solution:
  def addTwoNumbers(self, l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0
    while l1 or l2:
      pass