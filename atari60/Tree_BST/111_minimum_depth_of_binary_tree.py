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
    

'''
step2:
解方法はすぐに浮かんでいる
'''

#bfs
#回答時間: 3:50
# bsfの方が枝分かれが起きてると速い
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        node_queue_depth = deque([(root, 1)])
        while node_queue_depth:
            node, depth = node_queue_depth.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                node_queue_depth.append((node.left, depth+1))
            if node.right:
                node_queue_depth.append((node.right, depth+1))
        return None 


#dfs, stackを用いる
#time: O(N), space: O(N)
#回答時間: 3:40
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        min_depth = sys.maxsize
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()
            if not node.left and not node.right:
                min_depth = min(min_depth, depth)
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
        return min_depth


#dfs, 再起処理を使う方法
#time: O(N), space: O(N)
#回答時間: 3:50
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        if not root.left:
            return 1 + self.minDepth(root.right)
        elif not root.right:
            return 1 + self.minDepth(root.left)
        else:
            return min(1+ self.minDepth(root.left), 1 + self.minDepth(root.right))