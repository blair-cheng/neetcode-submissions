# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pin_left = dummy

        while True:
            kth = pin_left
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
                
            pre, curr = kth.next, pin_left.next
            for _ in range(k):
                tmp = curr.next
                curr.next = pre
                pre = curr
                curr = tmp

            tmp = pin_left.next
            pin_left.next = kth
            pin_left = tmp

        return dummy.next

















        dummy = ListNode(0, head)
        left_pin = dummy

        while True:
            kth = left_pin
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
                
            pre, curr = kth.next, left_pin.next
            for _ in range(k):
                tmp = curr.next
                curr.next = pre
                pre = curr
                curr = tmp

            tmp = left_pin.next
            left_pin.next = kth
            left_pin = tmp
        return dummy.next