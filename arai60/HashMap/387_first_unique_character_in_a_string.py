from collections import defaultdict


"""
step1
approach: hash_mapでcharごとのindexをリスト化していく.
"""

#time: O(N)
#sapce: O(N)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_map = defaultdict(list)
        for index, c in enumerate(s):
            char_map[c].append(index)

        first_unique_char = float('inf')
        for c, index_list in char_map.items():
            if len(index_list) == 1:
                first_unique_char = min(first_unique_char, index_list[0])
        return first_unique_char if first_unique_char != float('inf') else -1
    

# english lowercase letterのみであるので、以下のように回答できる.
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = [0]*26
        for c in s:
            freq[ord(c)-ord('a')] += 1
        for index, c in enumerate(s):
            if freq[ord(c) - ord('a')] == 1:
                return index
        return -1

#以下が一番早くて, space complexityが小さい
#time: O(N)
#space: O(N)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_freq = defaultdict(int)
        for c in s:
            char_freq[c] += 1
        for index, c in enumerate(s):
            if char_freq[c] == 1:
                return index
        return -1
    
    
"""
step2
"""

#time: O(N)
#space: O(N)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_index_map = defaultdict(list)
        for index, c in enumerate(s):
            char_index_map[c].append(index)

        first_unique_char_index = float('inf')
        for c, index_list in char_index_map.items():
            if len(index_list) == 1:
                first_unique_char_index = min(first_unique_char_index, index_list[0])
        
        return first_unique_char_index if first_unique_char_index != float('inf') else -1


#time: O(N)
#space: O(N)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_freq_map = defaultdict(int)
        for c in s:
            char_freq_map[c] += 1
        for index, c in enumerate(s):
            if char_freq_map[c] == 1:
                return index
        
        return -1