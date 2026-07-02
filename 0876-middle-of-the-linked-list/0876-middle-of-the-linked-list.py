# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # BruteForce
        # temp = head
        # count = 0
        # while (temp is not None):
        #     count += 1
        #     temp = temp.next
        # midNode = int((count/2)) + 1
        # temp = head
        # while (temp is not None):
        #     midNode -= 1
        #     if midNode == 0:
        #         break
        #     temp = temp.next
        # return temp

        # Optimal
        slow = head
        fast = head
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        return slow