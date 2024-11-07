from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#time: O(N)
#space: O(N)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_val_index = {}
        for index, val in enumerate(inorder):
            inorder_val_index[val] = index

        preorder_index = 0
        def build_tree(left_idx, right_idx):
            nonlocal preorder_index
            if left_idx > right_idx:
                return None
            
            root = TreeNode(preorder[preorder_index])
            preorder_index += 1
            root_index_inorder = inorder_val_index[root.val]
            root.left = build_tree(left_idx, root_index_inorder-1)
            root.right = build_tree(root_index_inorder+1, right_idx)

            return root

        return build_tree(0, len(preorder)-1)