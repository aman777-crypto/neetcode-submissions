class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        lower = 0
        upper = rows * cols - 1

        while lower <= upper:
            mid = (lower + upper) // 2

            row = mid // cols
            col = mid % cols

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                lower = mid + 1

            else:
                upper = mid - 1

        return False