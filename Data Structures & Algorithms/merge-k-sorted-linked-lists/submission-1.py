# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists)>1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append(self.mergeLists(l1, l2))
            
            lists = mergedLists
        
        return lists[0]

    
    def mergeLists(self, l1, l2):
        
        req_val = None
        req_Node = None
        temp1 = l1 
        temp2 = l2
        ans = None
        head = None

        while temp1 and temp2:
            if temp1.val < temp2.val:
                req_val = temp1.val
                temp1 = temp1.next
            else:
                req_val = temp2.val
                temp2 = temp2.next
            
            req_Node = ListNode(req_val)

            if head == None:
                head = req_Node
                ans = head
            else:
                ans.next = req_Node
                ans= ans.next
            
        if temp1:
            if head == None:
                head = temp1
            else:
                ans.next = temp1
        
        if temp2:
            if head == None:
                head = temp2
            else:
                ans.next = temp2

        return head




