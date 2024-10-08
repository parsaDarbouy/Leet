# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        node = head
        if node.next is None:
            return None
        count = 1
        while node.next is not None:
            node = node.next
            count += 1
        
        target = count - n + 1
        
        index = 1
        node = head
        pre_node = None
        while True:
            if index == target:
                if pre_node is None:
                    head = node.next
                    break
                pre_node.next = node.next
                break
            pre_node = node
            node = node.next
            index += 1
        return head
            

        
