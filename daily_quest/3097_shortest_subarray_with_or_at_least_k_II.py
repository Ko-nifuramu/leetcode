from typing import List

"""
step1:
sliding windowはすぐに思いつくが, bit周りで実装がグダってしまった.
あるbitの桁についてsubarrayの中で一つでも1があればorで1になることに注意.
"""


#time: O(32*n) where n is the length of nums array.
#space: O(1)
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        bit_counts = [0]*32
        left = 0
        min_subarray_len = float('inf')
        current_or = 0
        for right in range(len(nums)):
            current_or |= nums[right]
            for bit in range(32):
                if nums[right] & (1<<bit):
                    bit_counts[bit] += 1
            
            while left <= right and current_or >= k:
                min_subarray_len = min(min_subarray_len, right - left + 1)
                updated_or = 0
                for bit in range(32):
                    if nums[left] & (1<<bit):
                        bit_counts[bit] -= 1
                    if bit_counts[bit] > 0:
                        updated_or |= (1<<bit)
                
                current_or = updated_or
                left += 1

        return min_subarray_len if min_subarray_len != float('inf') else -1