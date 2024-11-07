from typing import List

"""
setp1
dynamic programmingで解いてよって問題に思える. 泥棒は, 隣り合う家をまとめて盗みに入ることができなので, 
dp上では, i番目の家に盗みに入りdp[i-2]と合わせるかdp[i-1]のどっちか.
"""

#time: O(N)
#space: O(N)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)

        max_robbed_amount = [0 for _ in range(len(nums))]
        max_robbed_amount[0] = nums[0]
        max_robbed_amount[1] = max(nums[0], nums[1])
        for index in range(2, len(nums)):
            max_robbed_amount[index] = max(max_robbed_amount[index-2]+nums[index], max_robbed_amount[index-1])

        return max_robbed_amount[-1]

#time: O(N)
#space: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_amount_2_before = 0
        max_amount_1_before = nums[0]
        for num in nums[1:]:
            current = max(max_amount_2_before + num, max_amount_1_before)
            max_amount_2_before = max_amount_1_before
            max_amount_1_before = current
        return max_amount_1_before


"""
step2
"""
# 5:05
#time: O(N)
#space: O(N)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        max_amount_dp = [0]*len(nums)
        max_amount_dp[0] = nums[0]
        max_amount_dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            max_amount_dp[i] = max(max_amount_dp[i-1], max_amount_dp[i-2]+nums[i])
        return max_amount_dp[-1]
