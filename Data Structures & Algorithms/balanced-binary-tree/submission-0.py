# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right))+1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        queue = deque([root])

        while len(queue) != 0:
            node = queue.popleft()
            if node != None:
                if abs(self.height(node.left) - self.height(node.right)) > 1:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True
        