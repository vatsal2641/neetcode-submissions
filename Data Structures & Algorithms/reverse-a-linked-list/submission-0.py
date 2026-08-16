# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        prev = None
        mid = None
        nex = head

        while nex != None:
            mid = nex
            nex = nex.next
            mid.next = prev
            prev = mid
        head = mid
        
        return head