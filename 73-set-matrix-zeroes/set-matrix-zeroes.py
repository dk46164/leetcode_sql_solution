class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #intailzie rows, col array
        row_len = len(matrix)
        col_len = len(matrix[0])
        rows_arr = [0]*row_len
        col_arr = [0]*col_len

        for i in range(row_len):
            for j in range(col_len):
                if not matrix[i][j]:
                    rows_arr[i] = 1
                    col_arr[j] = 1
        
        for i in range(row_len):
            for j in range(col_len):
                if rows_arr[i] or col_arr[j]:
                    matrix[i][j]=0
        
        