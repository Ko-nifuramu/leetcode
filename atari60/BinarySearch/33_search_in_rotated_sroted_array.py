from typing import List

"""
step1
#time: O(logN)
#space: O(1)
"""

#最小値を見つけてからbinary searchする
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        rotation_num = 0
        left_idx = 0
        right_idx = len(nums) - 1
        while left_idx < right_idx:
            mid = (left_idx + right_idx) // 2
            if nums[mid] < nums[right_idx]:
                right_idx = mid
            else:
                left_idx = mid + 1

        rotation_num = right_idx
        left_idx = 0
        right_idx = len(nums) - 1

        while left_idx <= right_idx:
            mid = (left_idx + right_idx) // 2
            real_mid = (mid + rotation_num) % len(nums)
            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] < target:
                left_idx = mid + 1
            else:
                right_idx = mid - 1

        return -1


#time: O(logN)
#sapce: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        [4,5,6,7,0,1,2]
        '''
        def find_pivot_index(left, right):
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < nums[right]:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        def binary_search(left, right, target):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        pivot_index = find_pivot_index(0, len(nums)-1)
        if nums[pivot_index] <= target <= nums[len(nums)-1]:
            left = pivot_index
            right = len(nums)-1
        else:
            left = 0
            right = pivot_index -1
        
        return binary_search(left, right, target)




#time: O(logN)
#sapce: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        [4,5,6,7,0,1,2]
        '''
        left, right = 0, len(nums)-1
        while left <= right:
            middle = (left+right) // 2
            if nums[middle] == target:
                return middle

            if nums[left] <= nums[middle]:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
                    
        return -1