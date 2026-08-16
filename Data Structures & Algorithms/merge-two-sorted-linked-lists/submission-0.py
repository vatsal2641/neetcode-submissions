# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        temp1 = list1
        temp2 = list2 
        next1 = None
        next2 = None
        final = None

        if temp1.val<temp2.val:
            final= temp1
            temp1= temp1.next
        else:
            final= temp2
            temp2= temp2.next

        final_head = final 

        while temp1 != None and temp2 != None:
            next1 = temp1.next
            next2 = temp2.next

            if temp1.val<temp2.val:
                final.next = temp1
                temp1 = temp1.next
                final = final.next
            else:
                final.next = temp2
                temp2 = temp2.next
                final = final.next
        
        if temp1 != None:
            final.next = temp1
        
        elif temp2 !=None:
            final.next = temp2

        return final_head

        