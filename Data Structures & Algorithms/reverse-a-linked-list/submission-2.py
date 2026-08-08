# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        def reverse(pre, cur):
            if cur is None:
                return pre
            else:
                nxt = cur.next
                cur.next = pre
                return reverse(cur, nxt)
        return reverse(None,head)

