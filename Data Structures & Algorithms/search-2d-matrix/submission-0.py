class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])

        def rowSearch() -> int:
            left, right = 0, M - 1

            while left <= right:
                mid = (left + right) // 2

                if matrix[mid][0] == target:
                    return mid
                elif matrix[mid][0] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                
            return left - 1
        
        def colSearch(row: int) -> int:
            left, right = 0, N - 1

            while left <= right:
                mid = (left + right) // 2

                if matrix[row][mid] == target:
                    return mid
                elif matrix[row][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                
            return -1
        
        row = rowSearch()
        col = colSearch(row)

        return col >= 0
 