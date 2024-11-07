from typing import List


#TLE
#time: O(N^2)
#space: O(N)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cumulative_sum = [0] * len(nums)
        cumulative_sum[0] = nums[0]

        for i in range(1, len(nums)):
            cumulative_sum[i] = cumulative_sum[i-1] + nums[i]

        min_len_subarray = float('inf')
        for i in range(len(nums)):
            if cumulative_sum[i] >= target:
                min_len_subarray = min(min_len_subarray, i+1)
            for j in range(i):
                if cumulative_sum[i] - cumulative_sum[j] >= target:
                    min_len_subarray = min(min_len_subarray, i - j)

        return min_len_subarray if min_len_subarray != float('inf') else 0
    


#sliding window
#time: O(N)
#space: O(N)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum_subarray = 0
        min_len_subarray = len(nums)+1
        for right in range(len(nums)):
            sum_subarray += nums[right]
            while sum_subarray >= target:
                min_len_subarray = min(min_len_subarray, right - left + 1)
                sum_subarray -= nums[left]
                left += 1

        return min_len_subarray if min_len_subarray != len(nums)+1 else 0