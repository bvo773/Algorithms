class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    '''
    You are given head of a singly linked-list. The list can be represente as
    L0->L1->...->Ln-1->Ln
    
    Reorder the list to be on the following form:
    L0->Ln->L1->Ln-1->L2->Ln-2->...


    Example 1:
    1->2->3->4

    1->4->2->3

    Input: head = [1,2,3,4]
    
    ALGO:
    a)Find middle nodle of linked list. If there are 2 middle nodes, return the 2nd middle node.
    Ex) 1->2->3->4->5->6 , mid node is 4

    b) Once middle node is found, reverse the 2nd part of list. 
    Ex) 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4

    c) Merge the two sorted lists. 
    Ex) Merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
    

    Find Middle Node
    Use Two Pointers, slow and fast. 
        - slow move one step forward, slow = slow.next
        - fast pointer move two steps forward fast = fast.next.next
    Fast pointer traverses twice as fast as slow. When fast pointer reaches the end of list,
    the slow pointer should be in the middle.
    '''
    def reorderList(self, head):
        slow, fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
    def printList(self, head):
        curr = head
        while curr:
            print(str(curr.val) + "->", end="")
            curr = curr.next
        
node6 = Node(6)            
node5 = Node(5, node6)
node4 = Node(4, node5)
node3 = Node(3, node4)            
node2 = Node(2, node3)
node1 = Node(1, node2)

l1 = node1
sol = Solution()
sol.printList(l1)