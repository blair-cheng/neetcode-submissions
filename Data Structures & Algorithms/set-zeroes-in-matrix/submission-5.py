class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
    # save 0 condition of list in first row
    # save 0 condition of row in first list [1]-[m-1]  
    # row_0 for the first row

        ROWS, COLS = len(matrix), len(matrix[0])   
        row_0 = False

        # determine which rows/cols need to be 0
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        row_0 = True
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        if row_0:
            for c in range(COLS):
                matrix[0][c] = 0

        