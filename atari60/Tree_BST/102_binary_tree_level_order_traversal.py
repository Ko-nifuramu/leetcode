from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#queueを使った, bfsでとく
#time: O(N)
#space: O(N)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        
        current_level_nodes = [root]
        nodes_ordered_by_level = []
        while current_level_nodes:
            current_node_values = []
            next_level_nodes = []
            for node in current_level_nodes:
                current_node_values.append(node.val)
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)
            current_level_nodes = next_level_nodes
            nodes_ordered_by_level.append(current_node_values)
        
        return nodes_ordered_by_level


#recursiveでのbfsでとく,　あまり早さは変わらない, stackかヒープのメモリを使うかの違い.
#time: O(N)
#space: O(N)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        nodes_ordered_by_level = []
        def order_nodes_by_level(node, level):
            if len(nodes_ordered_by_level) < level:
                nodes_ordered_by_level.append([])       
            nodes_ordered_by_level[level-1].append(node.val)
            if node.left:
                order_nodes_by_level(node.left, level+1)
            if node.right:
                order_nodes_by_level(node.right, level+1)
            
        order_nodes_by_level(root, 1)
        return nodes_ordered_by_level


"""
step2
"""
# 5:34
#time: O(N)
#space: O(N)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        nodes_ordered_by_level = []
        node_depth_queue = deque([(root, 1)])
        while node_depth_queue:
            node, depth = node_depth_queue.popleft()
            if len(nodes_ordered_by_level) < depth:
                nodes_ordered_by_level.append([])
            nodes_ordered_by_level[depth-1].append(node.val)
            if node.left:
                node_depth_queue.append((node.left, depth+1))
            if node.right:
                node_depth_queue.append((node.right, depth+1))

        return nodes_ordered_by_level


#time: O(N)
#space: O(N)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        nodes_ordered_by_level = []
        node_queue = deque([root])
        while node_queue:
            current_level_nodes_value = []
            next_level_nodes = []
            for node in node_queue:
                current_level_nodes_value.append(node.val)
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)
            nodes_ordered_by_level.append(current_level_nodes_value)
            node_queue = next_level_nodes
            
        return nodes_ordered_by_level