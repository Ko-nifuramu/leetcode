from typing import List, Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
step1
preorderの初めがrootとなり,そのルートの左部分木はpreorderでのroot.valの左側となる
preorder: [root, rootの左, rootの右]
inorer:   [rootの左, root, rootの右]
"""

#time: O(N^2)
#space: O(N)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        num_left_nodes = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:num_left_nodes+1], inorder[:num_left_nodes])
        root.right = self.buildTree(preorder[1+num_left_nodes:], inorder[num_left_nodes+1:])

        return root




"""
step2
"""
#5:05
#time: O(N^2)
#space: O(N)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        pre: [3, 9, 20, 15, 7]
        in: [9, 3, 15, 20, 7]
        '''
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        root_index_in_inorder = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:root_index_in_inorder+1], inorder[: root_index_in_inorder])
        root.right = self.buildTree(preorder[root_index_in_inorder+1:], inorder[root_index_in_inorder+1:])

        return root



#time: O(N)
#space: O(N)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        pre: [3, 9, 20, 15, 7]
        in: [9, 3, 15, 20, 7]
        '''
        if len(preorder)==0:
            return None
        
        inorder_index = defaultdict(int)
        for i in range(len(inorder)):
            inorder_index[inorder[i]] = i

        preorder_index = 0
        def build_tree(left_index, right_index):
            nonlocal preorder_index
            if left_index > right_index or preorder_index >= len(preorder):
                return None
            root = TreeNode(preorder[preorder_index])
            root_index_in_inorder = inorder_index[root.val]
            preorder_index += 1
            root.left = build_tree(left_index, root_index_in_inorder-1)
            root.right = build_tree(root_index_in_inorder+1, right_index)
            return root
        
        root = build_tree(0, len(preorder))
        return root