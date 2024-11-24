from typing import List


'''
step1: 単純なsliding windowだと思うが、ちょっとindexとかが扱いづらかった. 
こういうの苦手なのかも(こまなくindexの更新とか考えるのにワーキングメモリ的なものを使っている？).
'''

#Brute-Force: わかりやすい
#time: O(N*k)
#space: O(N-k)
# 12:00 ->問題の意味を理解するのに時間がかかった.丁寧に読まな
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        def power_of_subarray(left):
            max_num = nums[left]
            for i in range(left+1, left+k):
                if nums[i-1]+1 != nums[i]:
                    return -1
                max_num = max(max_num, nums[i])
            
            return max_num

        results = []
        for left in range(len(nums)-k+1):
            results.append(power_of_subarray(left))
        
        return results