from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
step1
approach1: bfs-recursive
approach2: bfs-queue
"""

#time: O(N)
#space: O(N)
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) < 1:
            return None
        mid = (0 + len(nums)-1) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root


#time: O(N)
#space: O(N)
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        sentinel = TreeNode(float('inf'))
        nodes_queue = deque([(sentinel, 0, len(nums)-1)])
        while nodes_queue:
            parent, left, right = nodes_queue.popleft()
            if left > right:
                continue
            middle = (left + right) // 2
            node = TreeNode(nums[middle])
            if parent.val > nums[middle]:
                parent.left = node
            if parent.val < nums[middle]:
                parent.right = node
            
            nodes_queue.append((node, left, middle-1))
            nodes_queue.append((node, middle+1, right))
        
        return sentinel.left



"""
step2

"""
#N: number of elements in nums
#time: O(N)
#space: O(N)
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:        
        def sorted_array_to_bst(left, right):
            if left > right:
                return None
            middle = (left + right) // 2
            root = TreeNode(nums[middle])
            root.left = sorted_array_to_bst(left, middle-1)
            root.right = sorted_array_to_bst(middle+1, right)
            return root
        
        left = 0
        right = len(nums)-1
        return sorted_array_to_bst(left, right)

#BFS
#time: O(N)
#space: O(N)
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        sentinel = TreeNode(float('inf'))
        nodes_queue = deque([(sentinel, 0, len(nums)-1)])
        while nodes_queue:
            parent, left, right = nodes_queue.popleft()
            if left > right:
                continue
            middle = (right+left) // 2
            node = TreeNode(nums[middle])
            if parent.val < node.val:
                parent.right = node
            if parent.val > node.val:
                parent.left = node
            
            nodes_queue.append((node, left, middle-1))
            nodes_queue.append((node, middle+1, right))
        
        return sentinel.left