from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
step1
stackの選択肢が思い浮かばなかった. ノード処理が早く思いつかなかった.
"""


# 最初からのノードのvalをリストに保存して、逆向きにList Nodeを作っていく手法
# time: O(N)
# space: O(N)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        val_list = []
        curr_node = head
        while curr_node:
            val_list.append(curr_node.val)
            curr_node = curr_node.next

        new_head = ListNode(val=val_list[-1])
        curr_node = new_head
        for i in range(len(val_list) - 2, -1, -1):
            node = ListNode(val=val_list[i])
            curr_node.next = node
            curr_node = node
        return new_head


# stackを使う方法, 取り出していけば逆順になる
# time: O(N)
# space: O(N)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        stack = []
        curr_node = head
        while curr_node:
            stack.append(curr_node)
            curr_node = curr_node.next

        new_head = stack.pop()
        curr_node = new_head
        while stack:
            node = stack.pop()
            curr_node.next = node
            curr_node = node
        curr_node.next = None  # head.nextはNone
        return new_head


# prev_node, curr_nodeを使って入れ替えていく方法、空間計算量は小さい
# time: O(N)
# space: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        prev_node = None
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        return prev_node


# 再起処理, 端っこの処理はややこしいが理解しやすい
# time: O(N)
# space: O(N)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list_helper(curr_node, prev_node):
            if not curr_node.next:
                curr_node.next = prev_node
                return curr_node
            next_node = curr_node.next
            curr_node.next = prev_node
            return reverse_list_helper(next_node, curr_node)

        if not head or not head.next:
            return head
        return reverse_list_helper(head, None)


"""
step2
"""

#time: O(N)
#space: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        sentinel = None
        prev_node, curr_node = sentinel, head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node

        return prev_node


#time: O(N)
#space: O(N)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        node_stack = []
        current_node = head
        while current_node:
            node_stack.append(current_node)
            current_node = current_node.next
        
        reverse_linked_list_head = node_stack.pop()
        current_node = reverse_linked_list_head
        while node_stack:
            next_node = node_stack.pop()
            current_node.next = next_node
            current_node = next_node
        current_node.next = None
        
        return reverse_linked_list_head


#time: O(N)
#space: O(N)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list_helper(curr_node, prev_node):
            if not curr_node.next:
                curr_node.next = prev_node
                return curr_node
            next_node = curr_node.next
            curr_node.next = prev_node
            return reverse_list_helper(next_node, curr_node)

        if not head:
            return None
        return reverse_list_helper(head, None)