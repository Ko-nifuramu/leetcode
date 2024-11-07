from typing import List

"""
step1
"""


# approach1: 二つのarrayの出現率をhash_mapにまとめて、その上で被っているかを確かめてans_arrayに入れる
# time: O(n1+n2)
# space: O(n1+n2)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_map1 = {}
        count_map2 = {}
        for num in nums1:
            count_map1[num] = count_map1.get(num, 0) + 1
        for num in nums2:
            count_map2[num] = count_map2.get(num, 0) + 1

        intersection_array = []
        for num, count in count_map1.items():
            if count_map2.get(num, None):
                intersection_array.append(num)
        return intersection_array


# approach2: setを使った解放
# time: O(n1+n2)
# space: O(n1+n2)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_set = set([])
        for num in nums1:
            num_set.add(num)

        intersection_set = set([])
        for num in nums2:
            if num in num_set:
                intersection_set.add(num)
        return list(intersection_set)
    

"""
step2
setbuiltinにintersectionもあるらしい
"""

#所要時間 1:30
#time: O(n1+n2)
#space: O(n1+n2)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_set1 = set(nums1)
        intersection_set = set([])
        for num in nums2:
            if num in num_set1:
                intersection_set.add(num)
        return list(intersection_set)

#time: O(n1+n2)
#space: O(n1+n2)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_set1 = set(nums1)
        num_set2 = set(nums2)
        intersection_set = num_set1.intersection(num_set2)
        return list(intersection_set)