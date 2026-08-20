# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1 = 0
        pow_count1 = 0
        temp = l1
        while temp:
            digit_val = temp.val
            num1 += digit_val * 10**pow_count1
            pow_count1 += 1
            temp = temp.next

        num2 = 0
        temp = l2
        pow_count2 = 0
        while temp: 
            digit_val = temp.val
            num2 += digit_val * 10**pow_count2
            pow_count2 += 1
            temp = temp.next

        req_sum = num1 + num2
        new_ll_t = None

        if new_ll_t is None:
            digit_val = req_sum % 10 
            req_sum = req_sum//10
            head = ListNode(digit_val, None)
            new_ll_t = head

        while req_sum:
            digit_val = req_sum % 10 
            req_sum = req_sum//10
            
            new_ll_t.next = ListNode(digit_val, None)
            new_ll_t = new_ll_t.next
        
        return head
