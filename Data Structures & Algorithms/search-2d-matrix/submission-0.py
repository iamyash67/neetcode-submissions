class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS - 1
        while top <= bottom:
            midrow = (top+bottom)//2
            if target > matrix[midrow][-1]:
                top = midrow + 1
            elif target < matrix[midrow][0]:
                bottom = midrow -1
            else:
                break
        if not (top <= bottom): return False
        midrow = (top+bottom)//2
        left , right = 0, COLS - 1
        while left <= right:
            m = (left+right)//2
            if target > matrix[midrow][m]:
                left = m+1
            elif target < matrix[midrow][m]:
                right = m-1
            else:
                return True
        return False
