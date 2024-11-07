from typing import List
from collections import defaultdict, Counter
import heapq


"""
step1
approch1: hash_mapを使ってnumsに出現するnumの回数を測定, それを元に優先度キューを使用して指定の数k
個のnumを出現数が多い順に取り出してくる

approach2: (freq, num)の配列を作りfreqでソート
approach3: pythonの組み込み関数を使用
approach4: quick selectもある
"""

#time: O(N + klogN)
#space: O(N)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_frequency = defaultdict(int)
        for num in nums:
            num_frequency[num] += 1
        
        heap_frequency = []
        for num, freq in num_frequency.items():
            heapq.heappush(heap_frequency, (-freq, num))

        top_k_elements = []
        for _ in range(k):
            _, num  = heapq.heappop(heap_frequency)
            top_k_elements.append(num)
        
        return top_k_elements

# N > k　であるので, 上のやり方より下の方が早い. また, わざわざ-freqとしなくても良い.
#time: O(N + klogk)
#space: O(N)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_frequency = defaultdict(int)
        for num in nums:
            num_frequency[num] += 1
        
        top_k_frequency = []
        for num, freq in num_frequency.items():
            heapq.heappush(top_k_frequency, (freq, num))
            if len(top_k_frequency) > k:
                heapq.heappop(top_k_frequency)
        return [num for freq, num in top_k_frequency]


#approach2:
#time: O(NlogN)
#space: O(N)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = Counter(nums)
        freq_list = [(count, num) for num, count in freq_dict.items()]
        freq_list.sort(reverse = True)
        return [num for _, num in freq_list[:k]]
    
    
#approach3
# most_common。内部的には全部返すときはsort、それ以外はheapqのnlargestを使っている。
# https://github.com/python/cpython/blob/d610d821fd210dce63a1132c274ffdf8acc510bc/Lib/collections/__init__.py#L619
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, count in Counter(nums).most_common(k)]

#nlargest
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        if len(counter) == k:
            return [num for num, count in counter.items()]
        top_k = heapq.nlargest(k, counter.items(), key=lambda x: x[1])
        return [num for num, count in top_k]

#approach4:
# quickselect。Time Complexityは~O(nlogn)~ ← Average: O(n), Worse(n^2)になる。