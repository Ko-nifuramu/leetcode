from typing import List


"""
step1
わからなかった.難易度自体は知らなきゃ難しいと思う.適切な例を考えなくては適切なアルゴリズムは導けない.
"""


# time: O(N)
# space: O(1)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(start_idx):
            left = start_idx
            right = len(nums) - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            return nums

        if len(nums) == 1:
            return nums

        index_1 = len(nums) - 2
        index_2 = len(nums) - 1
        while index_1 >= 0:
            if nums[index_1] < nums[index_1 + 1]:
                break
            index_1 -= 1

        if index_1 == -1:
            reverse(0)
            return nums

        while index_2 >= 0:
            if nums[index_2] > nums[index_1]:
                break
            index_2 -= 1

        nums[index_1], nums[index_2] = nums[index_2], nums[index_1]
        reverse(index_1 + 1)
        return nums
