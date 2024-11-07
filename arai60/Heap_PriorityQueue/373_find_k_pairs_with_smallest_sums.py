from typing import List
import heapq

"""
step1
nums1, nums2ともに昇順に並べられているので, 候補(index1, index2)が入るってわかったら, 
次に入るの候補は(index1+1, index2) もしくは (index1, index2 + 1)になる.
"""

#所要時間9分
#time: O(klogN)
#space(N)
## N = len(nums1)+len(nums2)
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pairs = []
        seen_pairs = set((0, 0))
        candidate_pairs = [(nums1[0]+nums2[0], 0, 0)]
        while len(pairs) < k and candidate_pairs:
            _, index_nums1, index_nums2 = heapq.heappop(candidate_pairs)
            pairs.append([nums1[index_nums1], nums2[index_nums2]])
            if index_nums1 + 1 < len(nums1) and (index_nums1+1, index_nums2)  not in seen_pairs:
                total = nums1[index_nums1+1] + nums2[index_nums2]
                heapq.heappush(candidate_pairs, (total, index_nums1+1, index_nums2))
                seen_pairs.add((index_nums1+1, index_nums2))
            
            if index_nums2 + 1 < len(nums2) and (index_nums1, index_nums2+1) not in seen_pairs:
                total = nums1[index_nums1] + nums2[index_nums2+1]
                heapq.heappush(candidate_pairs, (total, index_nums1, index_nums2+1))
                seen_pairs.add((index_nums1, index_nums2+1))
        
        return pairs

"""
step2
"""
#time: O(klogk)
#space: O(m*n)
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        k_smallest_pairs = []
        seen_pairs = set([])
        candidate_pairs = [(nums1[0]+nums2[0], 0, 0)]
        while len(k_smallest_pairs) < k and candidate_pairs:
            _, index1, index2 = heapq.heappop(candidate_pairs)
            k_smallest_pairs.append([nums1[index1], nums2[index2]])
            if index1+1 < len(nums1) and (index1+1, index2) not in seen_pairs:
                heapq.heappush(candidate_pairs, (nums1[index1+1] + nums2[index2], index1+1, index2))
                seen_pairs.add((index1+1, index2))
            if index2+1  < len(nums2) and (index1, index2+1) not in seen_pairs:
                heapq.heappush(candidate_pairs, (nums1[index1] + nums2[index2+1], index1, index2+1))
                seen_pairs.add((index1, index2+1))

        return k_smallest_pairs