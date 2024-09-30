# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root,0)

    def dfs(self,node,depth):
        if node is None:
            return depth
        max_depth = max(self.dfs(node.left,depth), self.dfs(node.right,depth))
        return max_depth + 1
