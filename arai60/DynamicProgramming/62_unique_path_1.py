"""
step1
数学的な解法とdynamic programmingの解法の二つ
"""

from math import factorial

#数学的な回答
#time: O(m+n)
#space: O(1)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        n_kai = 1
        m_kai = 1
        total = 1
        for i in range(1, m+n-1):
            total *= i
            if i == n-1:
                n_kai = total
            if i == m-1:
                m_kai = total
            
        return total // (n_kai * m_kai)

#dynamic prigrammingを使用する方法
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_of_paths = [[1]* n for _ in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                num_of_paths[row][col] = num_of_paths[row][col-1] + num_of_paths[row-1][col]
        
        return num_of_paths[-1][-1]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m+n-2) // (factorial(m-1)*factorial(n-1))