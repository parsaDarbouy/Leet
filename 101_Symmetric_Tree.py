# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.check(root.left,root.right)
        

    def check(self,left,right):
        if left and right:
            if left.val != right.val:
                return False
            else:
                far = self.check(left.left,right.right)
                close = self.check(left.right,right.left)
                return far and close
        else:
            if (left is None) and (right is None):
                return True
            else:
                return False
