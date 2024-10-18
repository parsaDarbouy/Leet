# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fastPtr = head
        slowPtr = head

        # The idea is: when fastPtr reached the end -> slowPtr is at the middle
        while fastPtr and fastPtr.next and fastPtr.next.next:
            fastPtr = fastPtr.next.next
            slowPtr = slowPtr.next

        curr = slowPtr.next
        prev = None

        while curr:
            nxt = curr.next
            curr.next, prev = prev, curr
            curr = nxt

        rHead = prev
        l = head    # beginning of left end
        r = rHead    # beginning of right end

        while r:    
            if l.val != r.val: return False
            l = l.next
            r = r.next

        return True
