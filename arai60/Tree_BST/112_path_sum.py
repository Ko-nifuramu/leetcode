from typing import Optional



"""
step1
approach1: dfsで探索してleafに来たらsummationとtargetを比べる. stack と recursiveのにパターン
approach2: bfs ...

葉ノードまで探索しないとtargetSumと比較できないので、dfsの方がメモリ使用量はすくない
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        

#4:44
#time: O(N)
#space: O(N)        
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        node_sum_stack = [(root, root.val)]
        while node_sum_stack:
            node, summation = node_sum_stack.pop()
            if not node.left and not node.right:
                if summation == targetSum:
                    return True
            if node.left:
                node_sum_stack.append((node.left, summation + node.left.val))
            if node.right:
                node_sum_stack.append((node.right, summation + node.right.val))
        
        return False


#recursive, dfs
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        has_path_sum = False
        def dfs_has_path_sum(node, summation_to_node):
            nonlocal has_path_sum
            if not node.left and not node.right:
                if summation_to_node == targetSum:
                    has_path_sum = True
            if node.left:
                dfs_has_path_sum(node.left, summation_to_node + node.left.val)
            if node.right:
                dfs_has_path_sum(node.right, summation_to_node + node.right.val)

        dfs_has_path_sum(root, root.val)
        return has_path_sum


#recursive, dfs version2
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            if root.val == targetSum:
                return True
        
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)