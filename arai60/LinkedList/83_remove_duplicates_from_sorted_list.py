from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
step1
まず問題を解く上で, 解法は元のリストを書き換えるのか, それとも新たな連結リストを作るのか.
問題的には前者であると考えられる.

approach1: ソートされているので、二つのノードを比べて被れば前のノードを次のノードに紐づける
"""


# time: O(N)
# space: O(1)
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prev_node = head
        curr_node = head.next
        while curr_node is not None:
            if prev_node.val == curr_node.val:
                prev_node.next = curr_node.next
                curr_node = curr_node.next
            else:
                prev_node = curr_node
                curr_node = curr_node.next
        return head


"""
step2
"""

#所要時間 3:10, 2:30
#time: O(N)
#space: O(1)
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        prev_node = head
        current_node = head.next
        while current_node:
            if prev_node.val == current_node.val:
                prev_node.next = current_node.next
                current_node = current_node.next
                continue
            prev_node = current_node
            current_node = current_node.next

        return head


#海保は同じだけど, current_nodeだけ使用する方法. 好みではあると思う.
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        current_node = head
        while current_node and current_node.next:
            if current_node.val == current_node.next.val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next

        return head