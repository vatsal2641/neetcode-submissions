# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseLL(self, head, end):
        if not head or not head.next or head.next == end:
            return head, head
    
        start_head = head
        nex = head
        prev = None
        cur = None

        while nex!=end:
            cur = nex
            nex = nex.next
            cur.next = prev
            prev = cur
            

        return cur, start_head


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        prev = None
        cur = head
        end = head
        start = False

        while end:
            count = 0

            while count<k:
                count+=1
                end = end.next
                if end == None:
                    if count == k:
                        break
                    else:
                        if prev:                     #What if in case we need to quit in between, make the last connection. 
                            prev.next = cur

                        return head
            
            reversed_head, start_head = self.reverseLL(cur, end)

            #For joining prevlist to the next one
            if prev:
                prev.next = reversed_head

            if start == False:
                head = reversed_head
                start = True

           
            # start_head.next = end
            cur = end
            prev = start_head
            
        
        return head


        