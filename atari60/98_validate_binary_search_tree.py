from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
N: num of nodes in BST
time: O(N)
space: O(N)
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        val_list_in_order = []

        self.search_in_order(root, val_list_in_order)

        for i in range(1, len(val_list_in_order)):
            if val_list_in_order[i-1] >= val_list_in_order[i]:
                return False
        
        return True

    def search_in_order(self, root, val_list_in_order):
        if root is None:
            return
        
        self.search_in_order(root.left, val_list_in_order)
        val_list_in_order.append(root.val)
        self.search_in_order(root.right, val_list_in_order)