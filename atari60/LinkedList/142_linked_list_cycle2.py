from typing import Optional


'''
step1:
approach1, setに訪れたノードを記録して返す
approach2, floydのサイクル発見アルゴリズム

approach2の実装ができなかった
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#time: O(N)
#space: O(N)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited_set = set()
        curr_node = head
        while curr_node:
            if curr_node in visited_set:
                return curr_node
            visited_set.add(curr_node)
            curr_node = curr_node.next
        return None

#time: O(N)
#space: O(1)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        else:
            return None
        
        curr_node = head
        while slow != curr_node:
            slow = slow.next
            curr_node = curr_node.next
        return curr_node