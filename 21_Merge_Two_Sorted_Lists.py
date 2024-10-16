# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        if list1 is None:
            if list2 is None:
                return None
            else:
                return list2

        if list2 is None:
            return list1

        pointer_1 = list1
        pointer_2 = list2
        if pointer_1.val < pointer_2.val:
            head = pointer_1
            pointer_1 = pointer_1.next
        else:
            head = pointer_2
            pointer_2 = pointer_2.next

        current_node = head

        while True:
            if pointer_1 is None:
                if pointer_2 is None:
                    break
                else:
                    print(pointer_2.val)
                    current_node.next = pointer_2
                    pointer_2 = pointer_2.next
                    current_node = current_node.next
                    continue

            if pointer_2 is None:
                current_node.next = pointer_1
                pointer_1 = pointer_1.next
                current_node = current_node.next
                continue
            
            

            if pointer_1.val < pointer_2.val:
                current_node.next = pointer_1
                pointer_1 = pointer_1.next
            else:
                current_node.next = pointer_2
                pointer_2 = pointer_2.next

            current_node = current_node.next
        return head

        
