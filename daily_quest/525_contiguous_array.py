from typing import List
from collections import defaultdict


#time: O(N)
#space: O(N)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_length = 0
        balance = 0  # balance of 1's and 0's (1 count - 0 count)
        balance_index_map = defaultdict(list)
        balance_index_map[0].append(-1)
        
        for index, num in enumerate(nums):
            balance += 1 if num == 1 else -1
            
            if balance in balance_index_map:
                max_length = max(index - balance_index_map[balance][0], max_length)
            balance_index_map[balance].append(index)
            
        return max_length