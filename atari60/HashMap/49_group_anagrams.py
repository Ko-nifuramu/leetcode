from collections import defaultdict
from typing import List


#n: strs.length, m: strs[i].length
#time: O(n*mlogm)
#space: O(n*m)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            anagram_map[str(sorted(s))].append(s)
        
        return list(anagram_map.values())



#アルファベットそれぞれの数を数えたタプルをkeyとした辞書を作成, こっちの方が計算量時代は小さくなる
#ただ少し実装がめんどくさくなるのとPythonのソートはビルトインでPowersortで実装されているので処理がされるのでソートの方がシンプルでかつ速度ももしかするとソートの方が早そう。
#time: O(n*m)
#space: O(n*m)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def count_alpha(word):
            counts = [0]*26
            for char in word:
                counts[ord(char) - ord('a')] += 1
            return tuple(counts)

        anagram_map = defaultdict(list)
        for s in strs:
            counts = count_alpha(s)
            anagram_map[counts].append(s)
        return list(anagram_map.values())