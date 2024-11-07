from typing import List
from bisect import bisect_left

#time: O(N^2)
#space: O(N)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        7, 7, 7, 7, 7 return 1
        3, 19, 2, 78, 9, 11 rerturn 3 
        '''
        if len(nums) == 0:
            return 0
        
        max_len_dp = [0] * len(nums)
        for i, num in enumerate(nums):
            max_len_before_i = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    max_len_before_i = max(max_len_before_i, max_len_dp[j])
            
            max_len_dp[i] = max_len_before_i + 1
        
        return max(max_len_dp)
    
#上記のコードのブラッシュアップ
#以下のコードの方が変数名からやりたいことが分かる.
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        lis_lengths = [0] * len(nums)

        def get_max_lis_before_index(right):
            max_lis_len = 0
            for i in range(right):
                if nums[right] > nums[i]:
                    max_lis_len = max(max_lis_len, lis_lengths[i])
            return max_lis_len
                    
        for i, num in enumerate(nums):
            lis_lengths[i] = get_max_lis_before_index(i) + 1
        
        return max(lis_lengths)
    


#例のように最大のlisを考える時, 各長さのsubsequenceのtailsを保存していく
#time: O(N^2)
#space: O(N)
'''
nums: [9, 1,4, 2, 11, 4, 9]

1, 4
1, 2, 11
1, 2, 4
1, 2, 4, 9
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis_tails = [nums[0]]
        
        def find_first_idx_greater_than_target(lis_tails, target):
            i = 0 
            while target > lis_tails[i]:
                i += 1
            return i

        for i in range(len(nums)):
            if lis_tails[-1] < nums[i]:
                lis_tails.append(nums[i])
                continue
            idx = find_first_idx_greater_than_target(lis_tails, nums[i])
            #一時的に元の配列通りの順番ではなくなるが、長さは変わらないので、このままで良い
            lis_tails[idx] = nums[i]

        return len(lis_tails)

#以下のように二分探索書き換える
#time: O(NlogN)
#space: O(N)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis_tails = [nums[0]]
        
        def find_first_idx_greater_than_target(lis_tails, target):
            left, right = 0, len(lis_tails)
            while left < right:
                middle = (left + right) // 2
                if lis_tails[middle] < target:
                    left = middle + 1
                if lis_tails[middle] >= target:
                    right = middle
            return right

        for i in range(len(nums)):
            if lis_tails[-1] < nums[i]:
                lis_tails.append(nums[i])
                continue
            idx = find_first_idx_greater_than_target(lis_tails, nums[i])
            #一時的に元の配列通りの順番ではなくなるが、長さは変わらないので、このままで良い
            lis_tails[idx] = nums[i]

        return len(lis_tails)
    
#time: O(NlogN)
#space: O(N)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis_tails = [nums[0]]

        for i in range(len(nums)):
            if lis_tails[-1] < nums[i]:
                lis_tails.append(nums[i])
                continue
            first_idx_greater_than_target = bisect_left(lis_tails, nums[i])
            lis_tails[first_idx_greater_than_target] = nums[i]

        return len(lis_tails)
    


"""
step2
"""
#time: O(N^2)
#space: O(N)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        max_subsequence_len = [1] * len(nums)
        for i, num in enumerate(nums):
            max_len_before_i = 0
            for j in range(i):
                if nums[j] < num:
                    max_len_before_i = max(max_len_before_i, max_subsequence_len[j])
            
            max_subsequence_len[i] = max_len_before_i + 1
        
        return max(max_subsequence_len)


#time: O(NlogN)
#space: O(N)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        [1,5,3, 9, 7, 6, 6, 10]
        1 -> 1, 5 -> 1,3 -> 1,3,9 -> 1, 3, 7 -> 1,3,6 -> 1,3,6,10
        """

        if len(nums) == 0:
            return 0

        lis_tails = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] <= lis_tails[-1]:
                index = bisect_left(lis_tails, nums[i])
                lis_tails[index] = nums[i]
                continue
            lis_tails.append(nums[i])
        
        return len(lis_tails)