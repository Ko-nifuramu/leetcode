"""
step1: 
条件分岐でミスが多かった。ハジケースが取りきれていない

プッシュダウンオートマトンらしい
"""


# time: O(N)
# space: O(N)
class Solution:
    def isValid(self, s: str) -> bool:
        open_stack = []
        open_character = ["(", "{", "["]
        close_character = [")", "}", "]"]
        for character in s:
            if character in open_character:
                open_stack.append(character)
            elif character in close_character:
                if len(open_stack) == 0:
                    return False
                open_char = open_stack.pop()
                if open_character.index(open_char) != close_character.index(character):
                    return False
            else:
                return False
        return True if len(open_stack) == 0 else False


# index検索よりもペアを作った方が拡張性がある
# time: O(N)
# space: O(N)
class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket_stack = []
        bracket_pair_map = {"(": ")", "{": "}", "[": "]"}

        for c in s:
            if c in bracket_pair_map:
                open_bracket_stack.append(c)
                continue
            if open_bracket_stack:
                return False
            open_bracket = open_bracket_stack.pop()
            if bracket_pair_map[open_bracket] != c:
                return False

        return open_bracket_stack == []


"""
step2
"""
#5:14 △
#time: O(N)
#space: O(N)
class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {'(': ')', '{': '}', '[': ']'}
        open_brackets = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                open_brackets.append(c)
            else:
                if len(open_brackets) == 0:
                    return False
                open_bracket = open_brackets.pop()
                if bracket_map[open_bracket] != c:
                    return False
        
        return True if len(open_brackets) == 0 else False