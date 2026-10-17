# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def checkEqual(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if (root1 == None) ^ (root2 == None):
            return False
        elif root1 == None and root2 == None:
            return True
        
        if root1.val != root2.val:
            return False
        else:
            return self.checkEqual(root1.left,root2.left) and self.checkEqual(root1.right, root2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            if subRoot == None:
                return True
            else:
                return False
        
        Q = deque([root])
        while len(Q) > 0:
            node = Q.popleft()
            if self.checkEqual(node, subRoot):
                return True
            else:
                if node.left != None:
                    Q.append(node.left)
                if node.right != None:
                    Q.append(node.right)
        return False
        

        