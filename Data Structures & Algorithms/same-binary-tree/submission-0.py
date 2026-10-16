# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        Lqueue = deque([p])
        Rqueue = deque([q])

        while len(Lqueue) > 0 and len(Rqueue) > 0:
            Lnode = Lqueue.popleft()
            Rnode = Rqueue.popleft()
            if Lnode == None or Rnode == None:
                if Lnode != None or Rnode != None:
                    return False
                else:
                    continue
            if Lnode.val != Rnode.val:
                return False
            Lqueue.append(Lnode.left)
            Lqueue.append(Lnode.right)
            Rqueue.append(Rnode.left)
            Rqueue.append(Rnode.right)
        return True