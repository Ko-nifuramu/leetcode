from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
step1
bstであるかを確認するには、親ノードとの関係だけではなく, もとの親との関係も大事. 
そのためには, max_val, min_valを意識することが大切.

approach1: BSTをin-orderに探索して, 最後に比較をする
approach2: maxとminを意識して再帰的にBSTかを判定していく.
"""

# N: num of nodes in BST
# time: O(N)
# space: O(N)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        val_list_in_order = []

        self.search_in_order(root, val_list_in_order)

        for i in range(1, len(val_list_in_order)):
            if val_list_in_order[i - 1] >= val_list_in_order[i]:
                return False

        return True

    def search_in_order(self, root, val_list_in_order):
        if root is None:
            return

        self.search_in_order(root.left, val_list_in_order)
        val_list_in_order.append(root.val)
        self.search_in_order(root.right, val_list_in_order)


# approach2 recursive こっちの方がシンプルで早い
#time: O(N)
#space: O(N)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node, lower, upper):
            if node is None:
                return True
            if not(lower < node.val < upper):
                return False
            else:
                return is_valid(node.left, lower, node.val) and is_valid(node.right, node.val, upper)
            
        return is_valid(root, -float('inf'), float('inf'))
    

#approach2 上限下限も考慮してbfsしていく. こっちがスチ
# bfs search looking at lower and upper bound
#time: O(N) N is num of nodes in bst
#space: O(N)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inf = float('inf')
        if root is None:
            return True
        node_queue = deque([(root, -inf, inf)])
        while node_queue:
            node, lower, upper = node_queue.popleft()
            if node is None:
                continue
            if not(lower < node.val < upper):
                return False
            node_queue.append((node.left, lower, node.val))
            node_queue.append((node.right, node.val, upper))
        
        return True
    



"""
step2
bfsでsearchする.この時lower, upperを保存しておく.
"""

# bfs search looking at lower and upper bound
#time: O(N) N is num of nodes in bst
#space: O(N)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid_bst(lower, upper, node):
            if not node:
                return True
            if not(lower < node.val < upper):
                return False
            
            return is_valid_bst(lower, node.val, node.left) and is_valid_bst(node.val, upper, node.right)

        lower = -float('inf')
        upper = float('inf')

        return is_valid_bst(lower, upper, root)
    

# bfs search looking at lower and upper bound
#time: O(N) N is num of nodes in bst
#space: O(N)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lower = -float('inf')
        upper = float('inf')

        queue = deque([(root, lower, upper)])
        while queue:
            node, lower, upper = queue.popleft()
            if node is None:
                continue
            if not(lower < node.val < upper):
                return False
            
            print(node.val)
            
            queue.append((node.left, lower, node.val))
            queue.append((node.right, node.val, upper))
        
        return  True