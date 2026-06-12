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

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Brute Force
        # stack = []
        # temp = head
        # while temp is not None:
        #     stack.append(temp.val)
        #     temp = temp.next
        # temp = head
        # while temp is not None:
        #     if temp.val != stack.pop():
        #         return False
        #     temp = temp.next
        # return True

        # Optimal
        if head is None or head.next is None:
            return True

        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        newHead = self.reverseLL(slow.next)
        first = head
        second = newHead
        while second is not None:
            if first.val != second.val:
                self.reverseLL(newHead)
                return False
            first = first.next
            second = second.next
        self.reverseLL(newHead)
        return True