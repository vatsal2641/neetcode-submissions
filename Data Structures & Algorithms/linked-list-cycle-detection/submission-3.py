# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head == None or head.next == None:
            return False
            
        temp1 = head
        temp2 = head
        
        while temp1 and temp2:
            if temp2.next is None:
                    return False
                    
            temp1 = temp1.next
            temp2 = temp2.next.next

            if temp1 == temp2:
                return True 

        return False