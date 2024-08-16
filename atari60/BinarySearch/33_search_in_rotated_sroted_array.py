from typing import List

"""
step1
#time: O(logN)
#space: O(1)
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1


        rotation_num = 0
        left_idx = 0
        right_idx = len(nums)-1

        while left_idx < right_idx:
            mid = (left_idx+right_idx) // 2

            if nums[mid] < nums[right_idx]:
                right_idx = mid
            else:
                left_idx = mid+1
        
        rotation_num = right_idx

        left_idx = 0
        right_idx = len(nums)-1

        while left_idx <= right_idx:
            mid = (left_idx+right_idx) // 2

            real_mid = (mid + rotation_num)%len(nums)

            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] < target:
                left_idx = mid+1
            else:
                right_idx = mid-1
        
        return -1

        