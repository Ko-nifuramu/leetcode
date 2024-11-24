from typing import List
'''
問題url: https://leetcode.com/problems/maximum-matrix-sum/?envType=daily-question&envId=2024-11-24
'''

'''
step1: アルゴリズムの問題ではないかな
'''

#time: O(height*width)
#space: O(1)
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negative_count = 0
        total_sum_if_all_positive = 0
        min_abs_value = float('inf')
        for row_array in matrix:
            for value in row_array:
                if value < 0:
                    negative_count += 1
                min_abs_value = min(min_abs_value, abs(value))
                total_sum_if_all_positive += abs(value)
        
        if negative_count%2 == 0:
            return total_sum_if_all_positive
        else:
            return total_sum_if_all_positive - 2*min_abs_value