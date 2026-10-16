# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        base = root
        root_to_base = 0
        while (base.left) and (base.right):
            if base.left == None:
                base = base.right
                root_to_base += 1
            elif base.right == None:
                base = base.left
                root_to_base += 1
            else:
                break
        
        c1 = self.diameterOfBinaryTree(base.left)
        c2 = self.maxDepth(base.left) + root_to_base
        c3 = self.maxDepth(base.left) + self.maxDepth(base.right)
        c4 = self.diameterOfBinaryTree(base.right)
        c5 = self.maxDepth(base.right) + root_to_base
        return max([c1,c2,c3,c4,c5])
        
