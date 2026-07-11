class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if (not matrix or not matrix[0]):
            return False

        total_rows = len(matrix)
        total_cols = len(matrix[0])

        start = 0
        end = (total_rows * total_cols) - 1

        while start <= end:
            mid = start + (end - start) // 2
            row = mid // total_cols
            col = mid % total_cols

            if target > matrix[row][col]:
                start = mid + 1
            elif target < matrix[row][col]:
                end = mid - 1
            else:
                return True
        
        return False