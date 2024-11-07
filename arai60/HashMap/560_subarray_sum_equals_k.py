from typing import List
from collections import defaultdict


"""
step1:
approach1: calculate the summation of each elements, so we have to traverse the array of list 'nums' twice
approach2: Use hashmap to store the summation
"""


# time: O(N)
# space: O(N)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_map = defaultdict(int)
        sum_map[0] = 1
        summation = 0
        num_of_sum_k = 0
        for index, num in enumerate(nums):
            summation += num
            if summation - k in sum_map:
                num_of_sum_k += sum_map[summation - k]
            sum_map[summation] += 1

        return num_of_sum_k


# time: O(N)
# space: O(N)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_freq = defaultdict(int)
        sum_val = 0
        count = 0
        sum_freq[0] = 1
        for num in nums:
            sum_val += num
            count += sum_freq[sum_val - k]
            sum_freq[sum_val] += 1
        return count


"""
step1
"""

#time: O(N)
#space: O(N)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cum_sum_map = defaultdict(int)
        num_of_subarray = 0
        cum_sum_map[0] = 1
        cum_sum = 0
        for num in nums:
            cum_sum += num
            remaining = cum_sum - k
            if remaining in cum_sum_map:
                num_of_subarray += cum_sum_map[remaining]
            cum_sum_map[cum_sum] += 1
        
        return num_of_subarray