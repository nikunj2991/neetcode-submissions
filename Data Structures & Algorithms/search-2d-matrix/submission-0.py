class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_i = 0
        right_i = len(matrix) - 1

        left_j = 0
        right_j = len(matrix[0]) - 1

        while (left_i <= right_i):
            mid_i = (left_i + right_i) // 2
            min_i = matrix[mid_i][left_j]
            max_i = matrix[mid_i][right_j]

            if min_i > target:
                right_i = mid_i - 1
            elif max_i < target:
                left_i = mid_i + 1
            else:
                i = mid_i
                break;
        
        if (left_i > right_i):
            return False

        while (left_j <= right_j):
            mid_j = (left_j + right_j) // 2

            if matrix[i][mid_j] > target:
                right_j = mid_j - 1
            elif matrix[i][mid_j] < target:
                left_j = mid_j + 1
            else:
                return True

        return False