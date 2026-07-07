class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        if not matrix or not matrix[0]:
            return
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Create a 2D prefix sum array with an extra row and column (padding with 0s)
        # to elegantly handle edge cases without index out-of-bounds errors.
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        # Populate the prefix sum matrix using the inclusion-exclusion principle.
        for row in range(rows):
            for col in range(cols):
                self.prefix[row + 1][col + 1] = (
                    matrix[row][col] +             # 1. Current element from the original matrix
                    self.prefix[row][col + 1] +    # 2. Sum of the entire block directly above
                    self.prefix[row + 1][col] -    # 3. Sum of the entire block directly to the left
                    self.prefix[row][col]          # 4. Subtract the overlapping diagonal block (counted twice)
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Shift indices by +1 to account for the padding in our prefix matrix.
        return (
            self.prefix[row2 + 1][col2 + 1] -      # 1. Total sum bounded by the bottom-right corner
            self.prefix[row1][col2 + 1] -          # 2. Subtract the unwanted top rectangle
            self.prefix[row2 + 1][col1] +          # 3. Subtract the unwanted left rectangle
            self.prefix[row1][col1]                # 4. Add back the overlapping top-left rectangle (subtracted twice)
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)