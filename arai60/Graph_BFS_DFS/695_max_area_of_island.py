from typing import List
from collections import deque


# もしposの地点が陸地なら、そこからbfsで探索してislandのsizeを求める. この時, 探索した場所を0にして沈める.
# 時間 12:16


"""
step1
approach1: もしposの地点が陸地なら、そこからbfsで探索してislandのsizeを求める. この時, 探索した場所を0にして沈める.
            一つのislandの探索方法としては, bfsとdfsの二通りがある
approch2: union find方法 余裕があったら取り組む
"""

# time: O(width*height)
# space: O(width*height)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        height = len(grid)
        max_island_size = 0

        def cal_island_size(pos):
            island_size = 0
            pos_queue = deque([pos])
            while pos_queue:
                row, col = pos_queue.popleft()
                if row < 0 or row >= height or col < 0 or col >= width:
                    continue

                if grid[row][col] == 1:
                    island_size += 1
                    grid[row][col] = 0
                    pos_queue.append((row - 1, col))
                    pos_queue.append((row + 1, col))
                    pos_queue.append((row, col - 1))
                    pos_queue.append((row, col + 1))
            return island_size

        for row in range(height):
            for col in range(width):
                if grid[row][col] == 0:
                    continue
                island_size = cal_island_size((row, col))
                max_island_size = max(max_island_size, island_size)
        return max_island_size
    

"""
step2

"""

#bfs
#所要時間 8:00
#time: O(width*height)
#space: O(widht*height)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        LAND = 1
        VISITED = -1

        def measure_island_area(row, col):
            island_area = 0
            pos_queue = deque([(row, col)])
            while pos_queue:
                row, col = pos_queue.popleft()
                if row < 0 or row >= height or col < 0 or col >= width:
                    continue
                if grid[row][col] == LAND:
                    grid[row][col] = VISITED
                    island_area += 1
                    pos_queue.append((row+1, col))
                    pos_queue.append((row-1, col))
                    pos_queue.append((row, col+1))
                    pos_queue.append((row, col-1))

            return island_area
        
        max_area = 0
        for row in range(height):
            for col in range(width):
                if grid[row][col] == LAND:
                    max_area = max(max_area, measure_island_area(row, col))
        
        return max_area

#以下のようにdfsの方法もある. 再起的に行う方法もあるが, こっちの方がわかりやすい
#time: O(width*height)
#space: O(widht*height)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        LAND = 1
        VISITED = -1

        def measure_island_area(row, col):
            island_area = 0
            pos_stack = [(row, col)]
            while pos_stack:
                row, col = pos_stack.pop()
                if row < 0 or row >= height or col < 0 or col >= width:
                    continue
                if grid[row][col] == LAND:
                    grid[row][col] = VISITED
                    island_area += 1
                    pos_stack.append((row+1, col))
                    pos_stack.append((row-1, col))
                    pos_stack.append((row, col+1))
                    pos_stack.append((row, col-1))

            return island_area
        
        max_area = 0
        for row in range(height):
            for col in range(width):
                if grid[row][col] == LAND:
                    max_area = max(max_area, measure_island_area(row, col))
        
        return max_area