# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head.next == None and n ==1 :
            return None

        else:
            temp = head
            while n:
                temp = temp.next
                n-=1
            
            if temp == None:
                head = head.next

            else:
                temp_needed = head
                prev_needed = None

                while temp is not None:

                    temp=temp.next
                    prev_needed = temp_needed
                    temp_needed = temp_needed.next
                
                prev_needed.next = temp_needed.next

            return head
        