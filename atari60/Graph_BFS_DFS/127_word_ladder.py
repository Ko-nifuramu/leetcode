from typing import List

"""
brute force

n = word_list_length
m = word_length

time: O(m*n)
space: O(m*n) stack_memory
"""
from collections import deque


class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:

        word_set = set(word_list)

        if end_word not in word_set:
            return 0

        queue = deque([(begin_word, 1)])

        while queue:
            curr_word, ladder_step = queue.popleft()

            if curr_word == end_word:
                return ladder_step

            for index in range(len(curr_word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    neighbor_word = curr_word[:index] + c + curr_word[index + 1 :]

                    if neighbor_word in word_set:
                        word_set.remove(neighbor_word)
                        queue.append((neighbor_word, ladder_step + 1))

        return 0
