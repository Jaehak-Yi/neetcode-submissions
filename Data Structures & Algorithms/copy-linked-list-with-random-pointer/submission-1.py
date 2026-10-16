"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head == None:
            return None
        
        pointer = head
        NumtoNode = {}
        i = 0
        while pointer:
            NumtoNode[i] = pointer
            pointer = pointer.next
            i = i+1

        NodetoNum = dict(zip(NumtoNode.values(), NumtoNode.keys()))
        L = len(NumtoNode)
        Hash_Table = {}
        for i in range(L):
            node1 = NumtoNode[i].next 
            node2 = NumtoNode[i].random
            if node1 != None:
                Hash_Table[i] = [NodetoNum[node1]]
            else:
                Hash_Table[i] = [-1]
            if node2 != None:
                Hash_Table[i].append(NodetoNum[node2])
            else:
                Hash_Table[i].append(-1)
        
        List_of_new_Nodes = []
        pointer = head
        for i in range(L):
            value = pointer.val
            node = Node(value, None, None)
            List_of_new_Nodes.append(node)
            pointer = pointer.next
        for i in range(L):
            if i != L-1:
                List_of_new_Nodes[i].next = List_of_new_Nodes[i+1]
            else:
                List_of_new_Nodes[i].next = None

            index = Hash_Table[i][1]
            if index != -1:
                List_of_new_Nodes[i].random = List_of_new_Nodes[index]
            else:
                List_of_new_Nodes[i].random = None
        return List_of_new_Nodes[0]