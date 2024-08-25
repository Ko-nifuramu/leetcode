from typing import List
import heapq

'''
step1:
aproach1. 無難に新しいvalが入るたびにソートをしてk番目に大きい要素を返す.
approach2. 優先度キューや木構造を使って挿入時の計算量をlogNにする

'''



#1733ms
#time: O(NlogN)
#space: O(N) apppendする際に新たなメモリを作るため
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)
        self.kth_largest = None

    #time: O(NlogN)
    #space: O(N)
    def add(self, val: int):
        self.nums.append(val)
        self.nums.sort(reverse=True)
        self.kth_largest = self.nums[self.k - 1]
        return self.kth_largest


# 98 ms
# __init__ -> time: O(Nlogk), space: O(N)
# __add__ -> time: O(logk), space: O(1)
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k  = k
        self.kth_largest_nums = nums

        heapq.heapify(self.kth_largest_nums)
        while len(self.kth_largest_nums) > k:
            heapq.heappop(self.kth_largest_nums)
    
    def add(self, val:int):
        heapq.heappush(self.kth_largest_nums, val)
        if len(self.kth_largest_nums) > self.k:
            heapq.heappop(self.kth_largest_nums)
        return self.kth_largest_nums[0]