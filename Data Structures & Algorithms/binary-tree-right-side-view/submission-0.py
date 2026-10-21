# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        def dfs(node: Optional[Treenode], depth: int):
            if node == None:
                return None
            if depth == len(answer):
                answer.append(node.val)
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
        
        dfs(root, 0)
        return answer
                
                    