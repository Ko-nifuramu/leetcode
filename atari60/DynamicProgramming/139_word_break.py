from typing import List


"""
Approach1: Dymnamic Programming

time: O(N^2)
space: O(N)
"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        if len(s) == 0:
            return True

        wordDict_set = set(wordDict)

        # segmentation_possible[i] means s[0:i] can be segmented into words in wordDict
        segmentation_possible = [False] * len(s) + 1
        segmentation_possible[0] = True

        for end_idx in range(1, len(s) + 1):
            for start_idx in range(end_idx):
                if (
                    segmentation_possible[start_idx]
                    and s[start_idx:end_idx] in wordDict_set
                ):
                    segmentation_possible[end_idx] = True

        return segmentation_possible[-1]


"""
Approach2: Rrcursive Algorithm

time: O(N^2)
space: O(N)
"""

from typing import List, Set


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        words_set = set(wordDict)
        memo = {}

        return self.word_break_helper(s, words_set, memo)

    def word_break_helper(self, s: str, words_set: Set[str], memo: dict) -> bool:
        if s in memo:
            return memo[s]

        if s in words_set:
            memo[s] = True
            return True

        for idx in range(1, len(s)):
            prefix = s[:idx]
            suffix = s[idx:]

            if prefix in words_set and self.word_break_helper(suffix, words_set, memo):
                memo[s] = True
                return True

        memo[s] = False
        return False


#TLE
#recursive
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        applespaceapples
        -> apple spaceapples or apples paceapples
        wordDict [apple, space, apples] 
        '''
        can_word_break = False
        def check_word_break(remaining_s):
            nonlocal can_word_break
            if can_word_break:
                return
            for word in wordDict:
                if remaining_s == word:
                    can_word_break = True
                    return
                if remaining_s[:len(word)] == word:
                    check_word_break(remaining_s[len(word):])
        
        check_word_break(s)
        return can_word_break
    

'''
step2
'''
#TLE
#time: O(len(s)*len(wordDict))
#space: O()
#time: O(len(s)*len(wordDict)*len(word))
#space: O()
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        can_break = False
        def check_word_break(remaininig_s):
            nonlocal can_break
            if len(remaininig_s) == 0:
                can_break = True

            for word in wordDict:
                if remaininig_s[:len(word)] == word:
                    check_word_break(remaininig_s[len(word):])
            

        check_word_break(s)
        return can_break

#Dynamic Programming
#time: O(N^2) N= len(s)
#space: O(len(wordDict) + len(s))
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_break_possible = [False]*(len(s)+1)
        word_break_possible[0] = True

        word_set = set(wordDict)
        for end in range(len(s)+1):
            for start in range(end):
                if s[start:end] in word_set and word_break_possible[start]:
                    word_break_possible[end] = True
        
        return word_break_possible[-1]