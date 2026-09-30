# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        trackerPtr = head
        passPointer = dummy
        while n > 0 and trackerPtr:
            trackerPtr = trackerPtr.next
            n -= 1
        
        while trackerPtr:
            passPointer = passPointer.next
            trackerPtr = trackerPtr.next
        
        passPointer.next = passPointer.next.next
        return dummy.next
        

        