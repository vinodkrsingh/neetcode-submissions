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
        copyLL = {None : None}

        curr  = head
        while curr:
            node = Node(curr.val)
            copyLL[curr] = node
            curr = curr.next
        
        curr = head
        while curr:
            copyLL[curr].next = copyLL[curr.next]
            copyLL[curr].random = copyLL[curr.random]
            curr = curr.next
        
        return copyLL[head]

