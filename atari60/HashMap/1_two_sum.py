from typing import List
from collections import defaultdict


'''
step1:

approach1: brute-force
approach2: hash map
'''

#hash map
#time: O(N)
#space: O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = defaultdict(list)
        for index in range(len(nums)):
            hash_map[nums[index]].append(index)
        
        for index in range(len(nums)):
            key = target - nums[index]
            if len(hash_map[key]) == 1:
                if hash_map[key] == [index]:
                    continue
                else:
                    return [index] + hash_map[key]
            if len(hash_map[key]) == 2:
                return hash_map[key]

#time: O(N^2)
#space: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i, j]
                
#one-pass hash map
#time: O(N)
#space: O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index, num in enumerate(nums):
            remain_num = target -num
            if remain_num not in hash_map:
                hash_map[num] = index
                continue
            return [hash_map[remain_num], index]

#one-pass hash map
#time: O(N)
#space: O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_map = {}
        for index, num in enumerate(nums):
            remain_num = target - num
            if remain_num in num_index_map:
                return [num_index_map[remain_num], index]
            else:
                num_index_map[num] = index