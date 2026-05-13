# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseLL(self, head):
        prev = None
        current = head
        while current is not None:
            front = current.next
            current.next = prev
            prev = current
            current = front
        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: 
        newhead = self.reverseLL(head)
        prev = None
        temp = newhead
        count = 1
        if  n == 1:
            newhead = newhead.next
            return self.reverseLL(newhead)
        while temp:
            if n == count:
                prev.next = temp.next
                break
            prev = temp
            temp = temp.next
            count += 1
        return self.reverseLL(newhead)
        
        