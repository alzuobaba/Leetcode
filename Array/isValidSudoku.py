"""
imput:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
宫格坐标 (m/3)*3 + (n/3) 从0 算起
// 表示整数除法
"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        h = [{} for i in range(9)]
        l = [{} for i in range(9)]
        gong = [{} for i in range(9)]
        for i in range(9):
            for j in range(9):
                nums = board[i][j]
                if nums == '.':
                    continue
                index_g = (i//3)*3 + (j//3)
                h[i][nums] = h[i].get('nums', 0) + 1
                l[j][nums] = h[i].get('nums', 0) + 1
                gong[index_g][nums] = gong[index_g].get(nums, 0) + 1
                if h[i][nums] > 1 or l[j][nums] > 1 or gong[index_g][nums] > 1:
                    return False

        else:
            return True


