# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dict_val = {}
        while head:
            if head.val in dict_val.keys():
                if head in dict_val[head.val]:
                    return True
                dict_val[head.val] += [head]
            else:
                dict_val[head.val] = [head]
            head = head.next 
        return False
