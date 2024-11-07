from collections import defaultdict
from typing import List


# n: strs.length, m: strs[i].length
# time: O(n*mlogm)
# space: O(n*m)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            anagram_map[str(sorted(s))].append(s)

        return list(anagram_map.values())


# アルファベットそれぞれの数を数えたタプルをkeyとした辞書を作成, こっちの方が計算量時代は小さくなる
# ただ少し実装がめんどくさくなるのとPythonのソートはビルトインでPowersortで実装されているので処理がされるのでソートの方がシンプルでかつ速度ももしかするとソートの方が早そう。
# time: O(n*m)
# space: O(n*m)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def count_alpha(word):
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord("a")] += 1
            return tuple(counts)

        anagram_map = defaultdict(list)
        for s in strs:
            counts = count_alpha(s)
            anagram_map[counts].append(s)
        return list(anagram_map.values())

"""
step2
"""
#5:34 △
#time: O(Nnlogn)
#space: O(Nn)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)#key: sorted_str, value: original_str
        for string in strs:
            sorted_str = sorted(string)
            anagram_map[str(sorted_str)].append(string)

        anagram_lists = []
        for _, anagram_list in anagram_map.items():
            anagram_lists.append(anagram_list)

        return anagram_lists