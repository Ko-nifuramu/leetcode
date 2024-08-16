from typing import List


'''
step1
time: O(N)
space: O(N)
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        
        return max(self.linear_rob_dp(nums[:-1]), self.linear_rob_dp(nums[1:]))
        
    def linear_rob_dp(self, nums: List[int]):
        robbed_money_dp = [0 for _ in range(len(nums))]

        robbed_money_dp[0] = nums[0]
        robbed_money_dp[1] = max(nums[0], nums[1])

        for i in range(2, len(robbed_money_dp)):
            robbed_money_dp[i] = max(robbed_money_dp[i-2]+nums[i], robbed_money_dp[i-1])
        
        return robbed_money_dp[-1]