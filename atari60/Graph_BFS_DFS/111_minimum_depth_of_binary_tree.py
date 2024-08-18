from typing import Optional
from collections import deque
import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
step1:
approach1. dfsで初めに葉ノードがきたらその深さを返す
approach2. bfsですべて探索して最小のdepthを求める二つの方法がある
'''
#所要時間: 7:23 rootのdepthが1なのを忘れてた,rootがNoneの時を考えていなかった
#time: O(N)
#space: O(N)
#dfs
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        node_queue = deque([(root, 1)])
        while node_queue:
            node, depth = node_queue.popleft()
            if not node.left and not node.right:
                return depth
            
            if node.left:
                node_queue.append((node.left, depth+1))
            if node.right:
                node_queue.append((node.right, depth+1))
        return

#所要時間: 4:36
#time: O(N)
#space: O(N)
#bfs
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        if root.right is None:
            return 1+self.minDepth(root.left)
        elif root.left is None:
            return 1+self.minDepth(root.right)
        else:
            return min(1+self.minDepth(root.left), 1+self.minDepth(root.right))

#所要時間: 4:34
#time: O(N)
#space: O(N)
#dfsをstackで実装
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        node_depth_stack = [(root, 1)]
        min_depth = sys.maxsize

        while node_depth_stack:
            node, depth = node_depth_stack.pop()
            if not node.left and not node.right:
                min_depth = min(min_depth, depth)
            if node.left:
                node_depth_stack.append((node.left, depth+1))
            if node.right:
                node_depth_stack.append((node.right, depth+1))
        
        return min_depth