from typing import List
'''
step1:

backtracking
time: O(n)
space: O(2^n)
補足として、再帰関数以外にもstackを用いて行うことができる。
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        all_combinations = []

        remain_right = n
        remain_left = n

        self.generate_parentheses_helper(remain_right, remain_left, '', all_combinations)

        return all_combinations

    def generate_parentheses_helper(self, remain_right, remain_left, curr_parentheses, all_combinations):
        if remain_left > remain_right:
            return

        if remain_left == 0 and remain_right == 0:
            all_combinations.append(curr_parentheses)
        elif remain_left == 0 and remain_right > 0:
                all_combinations.append(curr_parentheses + str(')' * remain_right))
        else:
            self.generate_parentheses_helper(remain_right-1, remain_left, curr_parentheses+')', all_combinations)
            self.generate_parentheses_helper(remain_right, remain_left-1, curr_parentheses+'(', all_combinations)
            

#変数・関数名の付け方、
# 関数名にhelperだと曖昧な気がする。ここでは、bracketのcombinationを作っているのでそれ由来の方がいい。
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        all_combinations = []

        remain_right_bracket = n
        remain_left_bracket = n

        
        def make_combinations(remain_right_bracket, remain_left_bracket, curr_parentheses, all_combinations):
            if remain_left_bracket > remain_right_bracket:
                return

            if remain_left_bracket == 0 and remain_right_bracket == 0:
                all_combinations.append(curr_parentheses)
            elif remain_left_bracket == 0 and remain_right_bracket > 0:
                    all_combinations.append(curr_parentheses + str(')' * remain_right_bracket))
            else:
                make_combinations(remain_right_bracket-1, remain_left_bracket, curr_parentheses+')', all_combinations)
                make_combinations(remain_right_bracket, remain_left_bracket-1, curr_parentheses+'(', all_combinations)
        
        
        make_combinations(remain_right_bracket, remain_left_bracket, '', all_combinations)

        return all_combinations


'''
step2:

approch1. backtracking
approach2. stackを使ってやってみる
'''


#approach1
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        all_parentheses = []

        def make_bracket_combinations(curr_combination, remain_left_num, remain_right_num):
            if remain_left_num == 0 and remain_right_num == 0:
                all_parentheses.append(curr_combination)
                return
            elif remain_left_num == 0 and remain_right_num>0:
                curr_combination += ')'*remain_right_num
                all_parentheses.append(curr_combination)
                return
            
            if remain_left_num == remain_right_num:
                make_bracket_combinations(curr_combination+'(', remain_left_num-1, remain_right_num)
            elif remain_left_num < remain_right_num:
                make_bracket_combinations(curr_combination+'(', remain_left_num-1, remain_right_num)
                make_bracket_combinations(curr_combination+')', remain_left_num, remain_right_num-1)
        
        make_bracket_combinations('', n, n)
        return all_parentheses
    

#approch2: using stack
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        all_parentheses = []
        stack = [('', n, n)]
        while stack:
            curr_combination, remain_left, remain_right = stack.pop()
            if remain_left > remain_right:
                continue
            
            if remain_left == 0:
                curr_combination += ')'*remain_right
                all_parentheses.append(curr_combination)
            else:
                stack.append((curr_combination+'(', remain_left-1, remain_right))
                stack.append((curr_combination+')', remain_left, remain_right-1))

        return all_parentheses

