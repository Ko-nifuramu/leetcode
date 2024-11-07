from typing import Optional
from collections import deque
import copy

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#bfs
#time: O(max(n1+n2))
#space: O(max(n1+n2)) 
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        queue_two_nodes = deque([(root1, root2)])

        while queue_two_nodes:
            node1, node2 = queue_two_nodes.popleft()
            node1.val = node1.val + node2.val

            if node1.left and node2.left:
                queue_two_nodes.append((node1.left, node2.left))
            if node1.right and node2.right:
                queue_two_nodes.append((node1.right, node2.right))

            if not node1.left and node2.left:
                node1.left = node2.left
            if not node1.right and node2.right:
                node1.right = node2.right

        return root1


#破壊的ではない方
#recursive bfs
#time: O(max(n1+n2))
#space: O(max(n1+n2)) 
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        if root1 and not root2:
            return copy.deepcopy(root1)
        if not root1 and root2:
            return copy.deepcopy(root2)
        
        new_node = TreeNode(root1.val + root2.val)
        new_node.left = self.mergeTrees(root1.left, root2.left)
        new_node.right = self.mergeTrees(root1.right, root2.right)

        return new_node


"""
step2
"""


#time: O(N)
#space: O(N)
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return copy.deepcopy(root2)
        if not root2:
            return copy.deepcopy(root1)
        
        new_node = TreeNode(root1.val + root2.val)
        new_node.left = self.mergeTrees(root1.left, root2.left)
        new_node.right = self.mergeTrees(root1.right, root2.right)

        return new_node


#time: O(max(n1,n2))
#space: O(max(n1,n2))
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return copy.deepcopy(root2)
        if not root2:
            return copy.deepcopy(root1)
        
        queue_two_node = deque([(root1, root2)])
        while queue_two_node:
            node1, node2 = queue_two_node.popleft()
            merge_node_val = node1.val + node2.val
            node1.val = merge_node_val

            if node1.left and node2.left:
                queue_two_node.append((node1.left, node2.left))
            if node1.right and node2.right:
                queue_two_node.append((node1.right, node2.right))

            if not node1.left and node2.left:
                node1.left = node2.left
            if not node1.right and node2.right:
                node1.right = node2.right
        
        return root1
            