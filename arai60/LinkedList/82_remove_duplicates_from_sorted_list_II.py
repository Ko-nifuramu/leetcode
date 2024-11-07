from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
step1
duplicateな値があれば, 全て抜かなければいけない.
current_nodeとcurrent_node.nextの値が等しければ, current_node.nextをcurret_node.next.nextにうつし
比較を繰り返していく. この過程でcurrent_node.nextがNoneになるときに別の処理を加えないといけない.

1 - 2 - 3 - 3 - 4 - 4 - 5
以下のようにheadも消される可能性がある
1 - 1
"""

#time: O(N)
#space: O(1)
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy_head = ListNode()
        dummy_head.next = head
        last_unique_node = dummy_head
        node = head
        while node and node.next:
            if node.val != node.next.val:
                last_unique_node = node
                node = node.next
                continue
            
            #skip_until_value_chanege
            while node:
                if not node.next:
                    last_unique_node.next = node.next
                    break
                if node.val != node.next.val:
                    last_unique_node.next = node.next
                    node = node.next
                    break
                if node.val == node.next.val:
                    node.next = node.next.next
            
        return dummy_head.next


#skip_until_value_changeの部分への分岐をわかりやすくした
# if文が深くなってしまったが、こっちの方が混乱しなさそう
#所要時間L: 9:00
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        sentinel = ListNode()
        sentinel.next = head
        last_unique_node = sentinel
        current_node = head
        while current_node:
            if not current_node.next or current_node.val != current_node.next.val:
                last_unique_node = current_node
                current_node = current_node.next
                continue
            if current_node.val == current_node.next.val:
                #skip_until_value_change
                while current_node:
                    if not current_node.next or current_node.val != current_node.next.val:
                        current_node = current_node.next
                        last_unique_node.next = current_node
                        break
                    if current_node.val == current_node.next.val:
                        current_node.next = current_node.next.next

        return sentinel.next


"""
step2
"""

'''
1 - 2 - 3 - 3 - 4 - 4 - 5

1 - 1
'''
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        current_node = head.next
        sentinel = ListNode()
        sentinel.next  = head
        last_unique_node = sentinel

        while current_node:
            if last_unique_node.next.val != current_node.val:
                last_unique_node = last_unique_node.next
                current_node = current_node.next
                continue
            if last_unique_node.next.val == current_node.val:
                while current_node:
                    if last_unique_node.next.val != current_node.val:
                        last_unique_node.next = current_node
                        current_node = current_node.next
                        break
                    current_node = current_node.next
                    if not current_node:
                        last_unique_node.next = None

        return sentinel.next
