from typing import List
'''
step1:
良い回答ではないが無難な回答、面白い回答もある(でも思いつけそう)
'''


#approach1: brute force
#time: O(2N)->O(N)
#space: O(N)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_list = []
        for num in nums:
            if num == 0:
                continue
            else:
                non_zero_list.append(num)
        
        for index in range(len(non_zero_list)):
            nums[index] = non_zero_list[index]
        
        for index in range(len(non_zero_list), len(nums)):
            nums[index] = 0
        
        return
    
#approach2: snow_ballの発想
#time: O(N)
#space: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        for index in range(len(nums)):
            if nums[index] == 0:
                zero_count += 1
                continue
            
            if zero_count > 0:
                nums[index-zero_count] = nums[index]
                nums[index] = 0
        
        return

#Approch3: 0でない数字を入れるindexをおく
#time: O(N)
#space: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[non_zero_index], nums[index] = nums[index], nums[non_zero_index]
                non_zero_index += 1

