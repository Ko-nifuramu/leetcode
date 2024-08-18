from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
step1: 
dfsかbfsで実装, すべてのノードを探索する必要があるためどっちが早いとかはない
'''
#所要時間: 1:00
#time: O(n)
#space: O(n)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)

#所要時間: 3:54
#bfsで実装
#time: O(n)
#space: O(n)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        node_depth_queue = deque([(root, 1)])
        max_depth = 0
        while node_depth_queue:
            node, depth = node_depth_queue.popleft()
            if not node.left and not node.right:
                max_depth = max(max_depth, depth)
            if node.left:
                node_depth_queue.append((node.left, depth+1))
            if node.right:
                node_depth_queue.append((node.right, depth+1))
        return max_depth