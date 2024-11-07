from typing import List



"""
step1
実際に書き出してみて二分探索の際はどのようなleft, rightの更新をしてけばいいかを考える
"""

#middleとleftを比較するパターン
#time: O(logN)
#space: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        5, 6, 7, 0, 1, 2, 3, 4
        """
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]

            mid = (left + right)//2
            if nums[mid] >= nums[left] and nums[mid] >= nums[right]:
                left = mid+1
            if nums[mid] <= nums[left] and nums[mid] <= nums[right]:
                right = mid

        return nums[right]

#単純にmiddleよりrightの方が小さければ, middleより右側に最小値がある
#time: O(logN)
#space: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            middle = (left+right)//2
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
        return nums[right]


"""
step2
"""
#2:58
#time: O(logN)
#space: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            if nums[mid] < nums[right]:
                right = mid

        return nums[right]