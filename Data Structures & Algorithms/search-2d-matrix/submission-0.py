class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix[0]) -1 
        while l < len(matrix) and r >= 0:
            if matrix[l][r] == target:
                return True
            elif target > matrix[l][r]:
                l += 1
            else:
                r -= 1
        return False