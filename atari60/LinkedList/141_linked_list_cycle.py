from typing import Optional

'''
step1:

approch1: floyd's cycle-finding algorithm
approch2: 
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#time: O(N)
#space: O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow, fast = head, head.next

        while fast and fast.next:
            if slow == fast:
                return True
                
            slow = slow.next
            fast = fast.next.next
        
        return False




'''
step2:
問題なくかけた、一行開けるところと開けないところが気になる、PEP8あたりを見る必要あり?
'''


#approach1 
#time: O(N)
#space: O(N)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_set = set()
        curr_node = head
        while curr_node:
            if curr_node in visited_set:
                return True
            visited_set.add(curr_node)
            curr_node = curr_node.next
        return False

#time: O(N)
#space: O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False