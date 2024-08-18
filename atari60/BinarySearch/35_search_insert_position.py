from typing import List
from bisect import bisect_left

'''
step1
二分探索、実装して素早く読めるようにする。
'''

#標準ライブラリの使用
#time: O(logN)
#space: O(1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int: 
        return bisect_left(nums, target)

#time: O(NlogN)
#space: O(1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:         
        left, right = 0, len(nums)
        while left < right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
    
    
'''
step2
'''


#所要時間: 1:02
#time: O(logN)
#space: O(1)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:         
        left, right = 0, len(nums)
        while left < right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid
        return left