from typing import List
import copy

"""
step1
approach1: numsの中からcurrentに入っていない数列をremaining_numsにおき, traverseして入れていく
approach2: backtrackingをする, つまりcurrentに入っていないnumsをどんどん入れていく, しかし毎回nums文traverseしていく
            のでn^nになるとなり非常に遅くなると考えられる.
approach3: 昇順に作成して, next_permutationを求めていく, アルゴリズム的にNlogN * N!かかる.
"""


#approach1
#所要時間 12:00 ミスった
#time: O(N!)
#space: O(N!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        def make_permutations(current_candidate, remaining_nums):
            if len(remaining_nums) == 1:
                permutation_candidate = current_candidate + remaining_nums
                permutations.append(permutation_candidate)
            
            for index in range(len(remaining_nums)):
                inserted_num = remaining_nums[index]
                next_candidate = current_candidate + [inserted_num]
                next_remaining_nums = remaining_nums[:index] + remaining_nums[index+1:]
                make_permutations(next_candidate, next_remaining_nums)
        
        make_permutations([], nums)
        return permutations


'''
approach2
recursive を使用する. まず, current_candidateを用意して, 新たな要素をnumsから入れる.
これを繰り返していく
'''

#所要時間 6:41
#time: O(N!), we have to traverse nums for N! candidates. So we will take N^N time complexity.
#space: O(N!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        def make_permutations(current_candidate):
            if len(current_candidate) == len(nums):
                permutations.append(current_candidate)
            
            for num in nums:
                if num in current_candidate:
                    continue
                new_candidate = current_candidate + [num]
                make_permutations(new_candidate)
        
        make_permutations([])
        return permutations

#最大値になるまで, next permutationの生成を繰り返していく
#time: O(N!)
#space: O(N!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        permutations = []
        permutation = sorted(nums)
        while permutation:
            permutations.append(permutation)
            permutation = self.next_permutation(permutation)
        
        return permutations

    def next_permutation(self, permutation: List[int]) -> None:
        """
        1432 -> 2134 -> 2143
        """
        permutation_copy = copy.deepcopy(permutation)
        def reverse(start_idx):
            left = start_idx
            right = len(permutation)-1
            while left < right:
                permutation_copy[left], permutation_copy[right] = permutation_copy[right], permutation_copy[left]
                left += 1
                right -= 1
        
        def find_first_index_not_decending():
            left = len(permutation_copy)-2
            while left >= 0:
                if permutation_copy[left] < permutation_copy[left+1]:
                    break
                left -= 1
            return left

        def find_index_next_larger(base, base_index):
            right = len(permutation_copy)-1
            right_min = float('inf')
            for i in range(len(permutation_copy)-1, base_index-1, -1):
                if base < permutation_copy[i] < right_min:
                    right_min = permutation_copy[i]
                    right = i
            return right

        if len(permutation_copy) == 1:
            return None
        left = find_first_index_not_decending()
        if left == -1:
            return None
        right = find_index_next_larger(permutation_copy[left], left)
        permutation_copy[left], permutation_copy[right] = permutation_copy[right], permutation_copy[left]
        reverse(left+1)

        return permutation_copy
