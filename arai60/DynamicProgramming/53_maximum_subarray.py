from typing import List
import math

"""
step1
approach1: 愚直に全てのsubarrayの和を求める.O(N^3)
approach2: i番目までの和の配列を作ってから、差を使って求める. O(N^2)
approach3: dynamic programmingを使用する. i番目を含める配列とiを含めなくても良いがsubarrayの最大を求める.
            選択肢としては, i番目を追加することで最大or新しくsubarrayを始めるiにした方が良いのかの二択
"""


# dynamic programming
# time: O(N)
# space: O(N)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_dp = [0 for _ in range(len(nums))]
        sum_dp_include_i = [0 for i in range(len(nums))]

        sum_dp[0] = nums[0]
        sum_dp_include_i[0] = nums[0]
        for i in range(1, len(nums)):
            sum_dp_include_i[i] = max(sum_dp_include_i[i - 1] + nums[i], nums[i])
            sum_dp[i] = max(sum_dp[i - 1], sum_dp_include_i[i])

        return sum_dp[-1]

#indexを含む中で最大のsumを求めて最後に最大を探せばよい. こっちの方がわかりやすい
#time: O(N)
#space: O(N)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum_subarray_end_index = [-math.inf]*len(nums)
        max_sum_subarray_end_index[0] = nums[0]
        for index in range(1, len(nums)):
            max_sum_subarray_end_index[index] = max(max_sum_subarray_end_index[index-1] + nums[index], nums[index])

        return max(max_sum_subarray_end_index)

#O(1)のspaceにもできる.　ただ, ループごとにmax演算子を使うことが遅いのか, 実行時間は結構遅い
#所要時間 2:56
#time: O(N)
#space: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum_subarray_end_index = nums[0]
        max_sum_subarray = nums[0]
        for index in range(1, len(nums)):
            max_sum_subarray_end_index = max(max_sum_subarray_end_index + nums[index], nums[index])
            max_sum_subarray = max(max_sum_subarray_end_index, max_sum_subarray)
        
        return max_sum_subarray