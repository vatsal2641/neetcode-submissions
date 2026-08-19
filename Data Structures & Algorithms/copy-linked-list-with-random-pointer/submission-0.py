"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        Copy_to_old = {None: None}

        temp = head
        while temp:
            copy = Node(temp.val)
            Copy_to_old[temp] = copy
            temp= temp.next

        temp = head
        while temp:
            copy = Copy_to_old[temp]
            copy.next = Copy_to_old[temp.next]
            copy.random = Copy_to_old[temp.random]
            temp = temp.next
        
        return Copy_to_old[head]