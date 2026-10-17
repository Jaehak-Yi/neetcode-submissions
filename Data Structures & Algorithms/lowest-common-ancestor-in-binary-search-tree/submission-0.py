# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> Bool:
        Que = deque([root])
        Is_P = False
        Is_Q = False
        while len(Que) > 0:
            node = Que.popleft()
            if node == p:
                Is_P = True
            elif node == q:
                Is_Q = True
            if Is_P and Is_Q:
                return True
            
            if node.left != None:
                Que.append(node.left)
            if node.right != None:
                Que.append(node.right)
        return False

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        Q = deque([root])
        answer = root
        while len(Q) > 0:
            node = Q.popleft()
            if self.isCommonAncestor(node, p, q):
                answer = node
                if node.left != None and node.right != None:
                    Q = deque([node.left, node.right])
                elif node.left == None and node.right != None:
                    Q = deque([node.right])
                elif node.left != None and node.right == None:
                    Q = deque([node.left])
                else:
                    return answer
        return answer
        
