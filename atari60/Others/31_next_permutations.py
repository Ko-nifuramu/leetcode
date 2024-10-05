from typing import List


#time: O(N)
#space: O(1)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        1432 -> 2134 -> 2143
        """
        def reverse(start_idx):
            left = start_idx
            right = len(nums)-1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        if len(nums) == 1:
            return nums

        index1 = len(nums) - 2
        while index1 >= 0:
            if nums[index1] < nums[index1+1]:
                break
            index1 -= 1

        if index1 == -1:
            reverse(0)
            return
        
        index2 = len(nums)-1
        right_min = float('inf')
        for i in range(len(nums)-1, index1-1, -1):
            if nums[index1] < nums[i] < right_min:
                right_min = nums[i]
                index2 = i

        nums[index1], nums[index2] = nums[index2], nums[index1]
        reverse(index1+1)


#関数化
#time: O(N)
#space: O(1)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        1432 -> 2134 -> 2143
        """
        def reverse(start_idx):
            left = start_idx
            right = len(nums)-1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        def find_first_index_not_decending():
            left = len(nums)-2
            while left >= 0:
                if nums[left] < nums[left+1]:
                    break
                left -= 1
            return left

        def find_index_next_larger(base, base_index):
            right = len(nums)-1
            right_min = float('inf')
            for i in range(len(nums)-1, base_index-1, -1):
                if base < nums[i] < right_min:
                    right_min = nums[i]
                    right = i
            return right

        if len(nums) == 1:
            return nums
        left = find_first_index_not_decending()
        if left == -1:
            reverse(0)
            return
        right = find_index_next_larger(nums[left], left)
        
        nums[left], nums[right] = nums[right], nums[left]
        reverse(left+1)
        
        