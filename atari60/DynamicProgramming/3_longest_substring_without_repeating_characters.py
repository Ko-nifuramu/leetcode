from collections import defaultdict

'''
step1
'''
#brute-force
#すべてのsubstringでwithout repeatingではないかをチェクする。
#N <= 5*1-0^4なのでtime exceed
#time: O(N^2)
#space: O(1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check_without_repeat(left, right):
            char_map = defaultdict(int)
            for index in range(left, right+1):
                char_map[s[index]] += 1
                if char_map[s[index]] >= 2:
                    return False
            return True

        max_len = 0
        for left in range(len(s)):
            for right in range(left, len(s)):
                if check_without_repeat(left, right):
                    max_len = max(max_len, right-left+1)

        return max_len
    


# sliding window
# 一度出てきた文字のindexを記録しておき、leftの更新を被った文字が出てきた時に行う

#所要時間: 4:00
#time: O(N)
#space: O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_index = {}
        left = 0
        max_len = 0
        seen_index = {}
        max_len = 0
        left = 0
        for right, c in enumerate(s):
            if c in seen_index and left <= seen_index[c]:
                left = seen_index[c]+1
            seen_index[c] = right
            max_len = max(max_len, right-left+1)
        return max_len


#setを使う回答, やってるとはseenと同じだけど, setから覗くので計算量が余計にかかる
#brute-forceに比べれば, leftとrightがそれぞれ一回だけなぞるので早い

#所要時間: 3:45
#time: O(N^2)
#space: O(N)
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
            max_len = max(max_len, right-left+1)
            right += 1
        return max_len