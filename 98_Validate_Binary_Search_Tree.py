# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root) -> bool:
        right = left = True
        if root.right is not None:
            right = right_val(root.right, [(root.val, 1)])
        if root.left is not None:
            left = left_val(root.left, [(root.val, 0)])
        return right and left


def right_val(root, fathers):
    right = left = True
    for i in fathers:
        if i[1]:
            if i[0] >= root.val:
                return False
        else:
            if i[0] <= root.val:
                return False
    if root.right is not None:
        right = right_val(root.right, fathers + [(root.val, 1)])
    if root.left is not None:
        left = left_val(root.left, fathers + [(root.val, 0)])
    return right and left


def left_val(root, fathers):
    right = left = True
    for i in fathers:
        if i[1]:
            if i[0] >= root.val:
                return False
        else:
            if i[0] <= root.val:
                return False
    if root.right is not None:
        right = right_val(root.right, fathers + [(root.val, 1)])
    if root.left is not None:
        left = left_val(root.left, fathers + [(root.val, 0)])
    return right and left



