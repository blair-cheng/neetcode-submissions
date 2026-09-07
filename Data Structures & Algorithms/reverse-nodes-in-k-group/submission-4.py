# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left_pin = dummy

        while True:
            # move kth to kth node
            kth = left_pin
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            # reverse group
            prev, curr = kth.next, left_pin.next
            for _ in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp2 = left_pin.next
            left_pin.next = kth
            left_pin = tmp2

        return dummy.next


        