from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# time: O(N)
# space: O(N)
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        l1 2->9->8
        l2 2->1->1
        892+112 = 1004
        l 4->0->0->1
        """
        str_num1 = ""
        str_num2 = ""
        while l1:
            str_num1 = str(l1.val) + str_num1
            l1 = l1.next
        while l2:
            str_num2 = str(l2.val) + str_num2
            l2 = l2.next
        str_sum = str(int(str_num1) + int(str_num2))
        dummy_head = ListNode()
        curr_node = dummy_head
        for index in range(len(str_sum) - 1, -1, -1):
            digit = int(str_sum[index])
            curr_node.next = ListNode(digit)
            curr_node = curr_node.next
        return dummy_head.next


# l1, l2の値を取ってくるときにif文でNoneか確かめるところをif文でやっているところがあまり良くない
# next_digitよりもcarryの方が良い
# time: O(N)
# space: O(1)
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy_head = ListNode()
        curr_node = dummy_head
        next_digit = 0
        while l1 or l2:
            l1_digit = 0
            l2_digit = 0
            if l1:
                l1_digit = l1.val
                l1 = l1.next
            if l2:
                l2_digit = l2.val
                l2 = l2.next
            sum_digit = l1_digit + l2_digit + next_digit
            next_digit = sum_digit // 10
            sum_digit = sum_digit - 10 * next_digit
            curr_node.next = ListNode(sum_digit)
            curr_node = curr_node.next

        if next_digit != 0:
            curr_node.next = ListNode(next_digit)

        return dummy_head.next


# 最後にcarryが1となって桁上げされる場合をwhileの中に入れた
# 所要時間: 8:15 sentinelとcurr_nodeの接続をミスった
# time: O(N)
# space: O(1)
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        sentinel = ListNode(0)
        current_node = sentinel
        while l1 or l2 or carry:
            curr_l1_digit = 0
            curr_l2_digit = 0
            if l1:
                curr_l1_digit = l1.val
                l1 = l1.next
            if l2:
                curr_l2_digit = l2.val
                l2 = l2.next
            curr_digit_sum = curr_l1_digit + curr_l2_digit + carry
            curr_digit = curr_digit_sum % 10
            carry = curr_digit_sum // 10
            current_node.next = ListNode(curr_digit)
            current_node = current_node.next

        return sentinel.next


# 以下のようにように三項間演算子を使用してやる方法もある。若干遅くなる
# time: O(N)
# space: O(1)
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        sentinel = ListNode(0)
        curr_node = sentinel
        while l1 or l2 or carry:
            curr_l1 = l1.val if l1 else 0
            curr_l2 = l2.val if l2 else 0
            curr_sum = curr_l1 + curr_l2 + carry
            carry = curr_sum // 10
            curr_node.next = ListNode(curr_sum % 10)
            curr_node = curr_node.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        return sentinel.next


"""
step2
"""
#5:14 ◯
#time: O(N)
#space: O(1)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        sentinel = ListNode()
        node = sentinel
        while l1 or l2 or  carry >= 1:
            l1_num = 0
            l2_num = 0
            if l1:
                l1_num = l1.val
                l1 = l1.next
            if l2:
                l2_num = l2.val
                l2 = l2.next

            total = l1_num + l2_num +carry
            node.next = ListNode(total%10)
            carry = total//10
            node = node.next
            
        return sentinel.next