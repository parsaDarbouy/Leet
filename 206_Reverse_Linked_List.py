# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None  
        current_node = head
        next_node = current_node.next
        while next_node:
            two_next = next_node.next
            next_node.next = current_node
            current_node = next_node
            next_node = two_next 
        head.next = None
        return current_node

