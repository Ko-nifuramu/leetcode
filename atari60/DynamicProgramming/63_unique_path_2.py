from typing import List
from collections import deque


# time: O(row_num*col_num)
# space: O(row_num*col_num)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row_num, col_num = len(obstacleGrid), len(obstacleGrid[0])

        if row_num == 1:
            for col in range(col_num):
                if obstacleGrid[0][col] == 1:
                    return 0
            return 1

        if col_num == 1:
            for row in range(row_num):
                if obstacleGrid[row][0] == 1:
                    return 0

            return 1

        way_pattern_grid = [[0 for _ in range(col_num)] for _ in range(row_num)]
        way_pattern_grid[0][0] = 1

        pos_deque = deque([[1, 0], [0, 1]])

        while len(pos_deque) > 0:
            row, col = pos_deque.popleft()

            if row >= row_num or col >= col_num or obstacleGrid[row][col] == 1:
                continue
            elif way_pattern_grid[row][col] != 0:
                continue
            else:
                if row - 1 >= 0 and obstacleGrid[row - 1][col] == 0:
                    way_pattern_grid[row][col] += way_pattern_grid[row - 1][col]

                if col - 1 >= 0 and obstacleGrid[row][col - 1] == 0:
                    way_pattern_grid[row][col] += way_pattern_grid[row][col - 1]

                print(way_pattern_grid[row][col])

            pos_deque.append([row + 1, col])
            pos_deque.append([row, col + 1])

        return way_pattern_grid[row_num - 1][col_num - 1]
