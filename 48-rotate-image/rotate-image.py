class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # transpose the matrix
        row  = len(matrix)
        for row_idx  in range(row):
            for col_idx in range(row_idx+1, row):
                matrix[col_idx][row_idx],matrix[row_idx][col_idx] = matrix[row_idx][col_idx],matrix[col_idx][row_idx]
            matrix[row_idx] = reversed(matrix[row_idx])
        return matrix