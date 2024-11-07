from typing import List


"""
step1
index=0を取りindex=-1を取らないパターン, index=0を取らないパターンを考えればいい

approach1: 通常のdpをnums[1:], nums[:-1]のにパターンやる. この時dp配列を2つ使う
approach2: 各パターンで線形dpを行う関数を作ってやる
approach3: 2つ, 1つまでの最大利益を保持しておき, 更新していく
"""

# time: O(N)
# space: O(N)
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
            robbed_money_dp[i] = max(
                robbed_money_dp[i - 2] + nums[i], robbed_money_dp[i - 1]
            )

        return robbed_money_dp[-1]


#time: O(N)
#space: O(N)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        get_first_dp = [0] * len(nums)
        get_last_dp = [0] * len(nums)

        get_first_dp[0] = nums[0]
        get_first_dp[1] = nums[0]
        
        get_last_dp[0] = 0
        get_last_dp[1] = nums[1]

        for index in range(2, len(nums)):
            if index == len(nums)-1:
                get_first_dp[-1] = get_first_dp[-2]
                get_last_dp[-1] = max(get_last_dp[-3] + nums[-1], get_last_dp[-2])
                continue

            get_first_dp[index] = max(get_first_dp[index-2] + nums[index], get_first_dp[index-1])
            
            get_last_dp[index] = max(get_last_dp[index-2] + nums[index], get_last_dp[index-1])

        return max(get_last_dp[-1], get_first_dp[-1])
    

# approach3
#time: O(N)
#space: O(1)
#time: O(N)
#space: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def linear_rob_dp(nums):
            if len(nums) == 1:
                return nums[0]
            max_rob_amount_2_before = nums[0]
            max_rob_amount_1_before = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                current_max_rob = max(max_rob_amount_2_before + nums[i], max_rob_amount_1_before)
                max_rob_amount_2_before = max_rob_amount_1_before
                max_rob_amount_1_before = current_max_rob
            
            return max_rob_amount_1_before

        return max(linear_rob_dp(nums[:-1]), linear_rob_dp(nums[1:]))