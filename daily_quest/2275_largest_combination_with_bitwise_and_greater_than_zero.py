from typing import List

"""
step1
"""

#time: O(32*N)
#space: O(N)
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        largest_combination_num = 0
        for i in range(32):
            one_num = 0
            for candidate in candidates:
                if candidate & (1 << i):
                    one_num += 1
            largest_combination_num = max(one_num, largest_combination_num)

        return largest_combination_num


#time: O(32*N)
#space: O(N)
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        largest_combination_num = 0
        for i in range(32):
            one_num = sum(1 for candidate in candidates if candidate & (1<<i))
            largest_combination_num = max(one_num, largest_combination_num)

        return largest_combination_num