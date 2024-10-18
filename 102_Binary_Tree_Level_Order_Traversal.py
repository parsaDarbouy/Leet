# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        self.dfs(root,answer,0)
        return answer


    def dfs(self,node,answer, level):
        if node:
            if len(answer) -1 < level:
                answer.append([node.val])
            else:
                answer[level].append(node.val)
            self.dfs(node.left,answer,level+1)
            self.dfs(node.right,answer,level+1)


                


        
