from collections import defaultdict

"""
step1
"""


# brute-force
# すべてのsubstringでwithout repeatingではないかをチェクする。
# N <= 5*1-0^4なのでtime exceed
# time: O(N^2)
# space: O(1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check_without_repeat(left, right):
            char_map = defaultdict(int)
            for index in range(left, right + 1):
                char_map[s[index]] += 1
                if char_map[s[index]] >= 2:
                    return False
            return True

        max_len = 0
        for left in range(len(s)):
            for right in range(left, len(s)):
                if check_without_repeat(left, right):
                    max_len = max(max_len, right - left + 1)

        return max_len


# sliding window
# 一度出てきた文字のindexを記録しておき、leftの更新を被った文字が出てきた時に行う


# 所要時間: 4:00
# time: O(N)
# space: O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_index = {}
        left = 0
        max_len = 0
        seen_index = {}
        for right, c in enumerate(s):
            if c in seen_index and left <= seen_index[c]:
                left = seen_index[c] + 1
            seen_index[c] = right
            max_len = max(max_len, right - left + 1)
        return max_len


# setを使う回答, やってるとはseenと同じだけど, setから覗くので計算量が余計にかかる
# brute-forceに比べれば, leftとrightがそれぞれ一回だけなぞるので早い


# 所要時間: 3:45
# time: O(N^2)
# space: O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        seen_index = set()
        max_len = 0
        while right < len(s):
            while s[right] in seen_index:
                seen_index.remove(s[left])
                left += 1

            seen_index.add(s[right])
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len


"""'
step2:
approach1:  left, right index + hashmap -> O(N^2), O(N)
approach2:  sliding window-> O(N), O(N)
"""


# dictを使っているけど、その必要はない.一番最後に出てきた時のindexを保持すれば良い
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = defaultdict(list)
        max_len_substring = 0
        left_index = 0
        for index, c in enumerate(s):
            if len(char_map[c]) >= 1 and char_map[c][-1] >= left_index:
                max_len_substring = max(max_len_substring, index - left_index)
                left_index = char_map[c][-1] + 1
            char_map[c].append(index)
        max_len_substring = max(max_len_substring, len(s) - left_index)
        return max_len_substring


# 所要時間: 2:14
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left_index = 0
        max_len = 0
        for right_index, c in enumerate(s):
            if c in char_index and char_index[c] >= left_index:
                max_len = max(right_index - left_index, max_len)
                left_index = char_index[c] + 1
            char_index[c] = right_index

        max_len = max(len(s) - left_index, max_len)
        return max_len


# 毎回更新する方法もあるけど、こっちの方がその分遅い
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        max_len = 0
        left = 0
        for right, c in enumerate(s):
            if c in char_index and char_index[c] >= left:
                left = char_index[c] + 1
            char_index[c] = right
            max_len = max(right - left + 1, max_len)

        return max_len


"""
step3
"""




'''
所要時間 5:12
approach2:  sliding window-> O(N), O(N)
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        max_len_substring = 0
        char_last_seen = defaultdict(int)
        left = 0
        for index, c in enumerate(s):
            if c in char_last_seen and left <= char_last_seen[c]:
                max_len_substring = max(index-left, max_len_substring)
                left = char_last_seen[c]+1
            char_last_seen[c] = index
        max_len_substring = max(index-left+1, max_len_substring)
        return max_len_substring


#下のようにやれば, forループ抜けた後のmax_len_substringの評価はいらない
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        max_len_substring = 0
        char_last_seen = defaultdict(int)
        left = 0
        for index, c in enumerate(s):
            if c in char_last_seen and left <= char_last_seen[c]:
                left = char_last_seen[c]+1
            char_last_seen[c] = index
            max_len_substring = max(index-left+1, max_len_substring)
        return max_len_substring
            