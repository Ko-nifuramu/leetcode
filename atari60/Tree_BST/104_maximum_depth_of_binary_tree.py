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
    


'''
step2
'''

#approach1: dfsで探索, こっちの方が重要
#時間: 3:40
#time: O(N)
#space: O(N)木構造的に関数を実行しているのでスタックに貯まる
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if not root.left and not root.right:
            return 1
            
        max_depth = 0
        max_depth = max(1+self.maxDepth(root.right), 1+self.maxDepth(root.left))
        return max_depth

#bfs
#time: O(N)
#space: O(N)枝分かれの分だけqueueに溜まっていく
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue_node_depth = deque([(root, 1)])
        max_len = 0
        while queue_node_depth:
            node, depth = queue_node_depth.popleft()
            if not node.left and not node.right:
                max_len = max(max_len, depth)
            if node.left:
                queue_node_depth.append((node.left, depth+1))
            if node.right:
                queue_node_depth.append((node.right, depth+1))
        return max_len