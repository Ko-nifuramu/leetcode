"""
step1
approach1: 直接zigzagに並べた配列を作ってから、各行ごとに取り出す
approach2: 各行ごとに周期があるのでそれを使用する
"""

#time: O(N)
#space: O(1)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= 2:
            return s
        if numRows == 1:
            return s
        
        zigzag_conversion = ""
        def traverse_zigzag_order_row(row):
            zigzag_one_row = ""
            s_index = row
            if row == 0 or row == numRows -1:
                while s_index < len(s):
                    zigzag_one_row += s[s_index]
                    s_index += 2 * numRows -2
            else:
                s_index = row
                top_down = True
                while s_index < len(s):
                    zigzag_one_row += s[s_index]
                    if top_down:
                        s_index += 2*numRows - 2 - 2 * row
                    else:
                        s_index += 2 * row
                    top_down = not top_down

            return zigzag_one_row

        zigzag_conversion = ""
        for row in range(numRows):
            zigzag_conversion += traverse_zigzag_order_row(row)
        return zigzag_conversion


#approach1のバージョン
#time: O(N)
#space: O(N)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        def create_zigzag_list(s, num_rows):
            pos = 0
            zigzag_list = [[] for _ in range(num_rows)]
            while pos < len(s):
                for row in range(num_rows):
                    zigzag_list[row].append(s[pos])
                    pos += 1
                    if pos >= len(s):
                        return zigzag_list
                
                for row in range(num_rows-2, 0, -1):
                    zigzag_list[row].append(s[pos])
                    pos += 1
                    if pos >= len(s):
                        return zigzag_list

            return zigzag_list

        zigzag_list = create_zigzag_list(s, numRows)
        zigzag_conversion = ''
        for row_list in zigzag_list:
            zigzag_conversion += ''.join(row_list)
        
        return zigzag_conversion