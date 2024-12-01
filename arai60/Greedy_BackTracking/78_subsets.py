from typing import List

#time: (2^n)
#space: O(2^n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        nums = [1, 2, 3]
        output: [[], [1], [1, 2], [1, 3], [2], [2,3], [1,2,3]]

        we have two patterns looking at one element: contain it as one of subsets or not. -> we will implement this in recursive method.
        '''
        if len(nums) == 0:
            return [[]]
        
        subsets_array = []
        def make_subsets(current_subset, remain_nums):
            if len(remain_nums) == 1:
                subsets_array.append(current_subset)
                subsets_array.append(current_subset + [remain_nums[0]])
                return

            make_subsets(current_subset + [remain_nums[0]], remain_nums[1:])
            make_subsets(current_subset, remain_nums[1:])

        make_subsets([], nums)
        return subsets_array



"""
backtrackを再帰の代わりにstackを使う版。
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:      
        subsets = []

        building_subset_stack = [([], 0)] # (subset, index)
        while building_subset_stack:
            subset, index = building_subset_stack.pop()
            if index == len(nums):
                subsets.append(subset)
                continue
            building_subset_stack.append((subset + [nums[index]], index + 1))
            building_subset_stack.append((subset.copy(), index + 1))
        return subsets
```



LeetCodeの解法を見た。既存のsubsetsに含まれる全てのsubsetに現在注目している値を追加したsubsetを加える。
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            subsets.extend([subset + [num] for subset in subsets])
        return subsets
```
"""


#time: (2^n)
#space: O(2^n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        nums = [1, 2, 3]
        output: [[], [1], [1, 2], [1, 3], [2], [2,3], [1,2,3]]

        bitmask: '001' -> subset: [3]
        '''
        subsets = []

        #bitmask is implemted as reversed order
        def make_subset_from_bitmask(bitmask):
            subset = []
            index = 0
            while bitmask:
                if bitmask & 1:
                    subset += [nums[index]]
                bitmask >>= 1
                index += 1
            return subset
        
        for bitmask in range(2**len(nums)):
            subset = make_subset_from_bitmask(bitmask)
            subsets.append(subset)
        return subsets
        

'''
step2
'''

#time: O(2^n)
#space: O(2^n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = []
        def make_subset_from_bitmask(bitmask):
            subset = []
            for index in range(len(nums)):
                if (bitmask >> index) & 1:
                    subset.append(nums[index])

            return subset
        
        for bitmask in range(2**len(nums)):
            subset = make_subset_from_bitmask(bitmask)
            all_subsets.append(subset)
        
        return all_subsets


#time: O(2^n)
#space: O(2^n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = []
        def make_subsets(current_subset, remaining_nums):
            if remaining_nums == []:
                all_subsets.append(current_subset)
                return
            
            make_subsets(current_subset, remaining_nums[1:])
            make_subsets(current_subset + [remaining_nums[0]], remaining_nums[1:])
        
        make_subsets([], nums)
        return all_subsets
        