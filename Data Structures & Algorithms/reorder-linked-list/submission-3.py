# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseList(self, head: Optional[ListNode]):
        prev = None
        curr = None
        nex = head
        while nex is not None:
            curr = nex
            nex = nex.next
            curr.next = prev
            prev = curr

        return curr

    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not (head == None or head.next == None or head.next.next == None):
            
        
            temp1 = head
            temp2 = head

            while temp2.next!=None and temp2.next.next!=None:

                temp1 = temp1.next
                temp2 = temp2.next.next

            head_rev = temp1.next
            temp1.next = None
            head_rev = self.reverseList(head_rev)

            
            initial_head = head
            later_head = head_rev
        

            while initial_head is not None and later_head is not None:
                initial_next = initial_head.next
                initial_head.next = later_head
                later_next = later_head.next
                later_head.next = initial_next
                initial_head = initial_next
                later_head = later_next

     
        
