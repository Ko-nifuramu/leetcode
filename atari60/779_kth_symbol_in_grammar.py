'''
approach1: brute force

time: O(2^n*n)
space: O(2^n)

もちろんTLE
'''


#time: O(2^n*n)
#space: O(2^n)
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        row = '0'

        for _ in range(n-1):
            row = self.kth_grammar_helper(row)
        
        return int(row[k-1])


    def kth_grammar_helper(self, previous_row: str):
        next_row = ''

        for char in previous_row:
            if char == '0':
                next_row += '01'
            elif char == '1':
                next_row += '10'
        
        return next_row
        


'''
approach2: Recursive

time: O(N)
space: O(1)
'''

class Solution:
    def kth_symbol_grammar(self, n:int, k:int):
        
        if n == 1:
            return 0

        if k%2 == 0:
            return 1 if self.kth_symbol_grammar(n-1, k/2)==0 else 0
        else:
            return 0 if self.kth_symbol_grammar(n-1, (k+1)/2)==0 else 1
        

