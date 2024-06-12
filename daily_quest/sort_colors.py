from typing import List


#コードが来たなすぎる
#time: O(N)
#space: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_index = 0

        while nums[insert_index] == 0 and insert_index < len(nums)-1:
            insert_index += 1

        for index in range(insert_index, len(nums)):
            if nums[index] == 0:
                temp = nums[insert_index]
                nums[insert_index] = 0
                nums[index] = temp
                insert_index += 1
        
        for index in range(insert_index, len(nums)):
            if nums[index] == 1:
                temp = nums[insert_index]
                nums[insert_index] = 1
                nums[index] = temp
                insert_index += 1