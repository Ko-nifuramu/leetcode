from typing import List
from collections import deque

'''
step1
解法は一瞬で浮かんだが、コードに起こす時に時間がかかった.
また, 実装としてメモリオーバになるような実装もしていた
'''


#time: O(row_len*col_len)
#space: O(row_len*col_len)
#以下の回答はmemory_maxになった
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_len, col_len = len(grid), len(grid[0])

        def explore_island(row, col):
            queue = deque([(row, col)])
            while queue:
                row, col = queue.popleft()
                grid[row][col] = '-1'
                if row-1 >= 0 and grid[row-1][col] == '1':
                    queue.append((row-1, col))
                if row+1 < row_len and grid[row+1][col] == '1':
                    queue.append((row+1, col))
                if col-1 >= 0 and grid[row][col-1] == '1':
                    queue.append((row, col-1))
                if col+1 < col_len and grid[row][col+1] == '1':
                    queue.append((row, col+1))
                
        num_island = 0
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == '0':
                    grid[row][col] = '-1'
                if grid[row][col] == '-1':
                    continue
                if grid[row][col] == '1':
                    explore_island(row, col)
                    num_island += 1



#time: O(row_len*col_len)
#space: O(row_len*col_len)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        LAND = '1'
        VISITED = '-1'

        height = len(grid)
        width = len(grid[0])
        def mark_as_visited(row, col):
            if row < 0 or row >= height or col < 0 or col >= width:
                return
            if grid[row][col] != LAND:
                return
            grid[row][col] = VISITED
            mark_as_visited(row-1, col)
            mark_as_visited(row+1, col)
            mark_as_visited(row, col-1)
            mark_as_visited(row, col+1)
        
        num_island  = 0
        for row in range(height):
            for col in range(width):
                if grid[row][col] == LAND:
                    mark_as_visited(row, col)
                    num_island += 1
        return num_island