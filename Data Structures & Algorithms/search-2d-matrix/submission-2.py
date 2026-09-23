class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        colTop = 0
        colBot = len(matrix[0]) -1
        rowLst  = len(matrix) -1
        rowFst = 0

        while rowFst <= rowLst:
            mid = (rowFst+rowLst)//2
            if target < matrix[mid][0]:
                rowLst = mid - 1
            elif target > matrix[mid][colBot]:
                rowFst = mid + 1
            else:
                break
        
        rowMid = (rowFst+rowLst)//2

        while colTop <= colBot:
            mid  = (colTop+colBot)//2
            if target == matrix[rowMid][mid]:
                return True
            elif target >= matrix[rowMid][mid]:
                colTop = mid + 1 
            else:
                colBot = mid -1
        return False


        # l = 0
        # r = len(matrix[0]) -1
        # while l < len(matrix) and r >= 0:
        #     if matrix[l][r] == target:
        #         return True
        #     elif target > matrix[l][r]:
        #         l += 1
        #     else:
        #         r -= 1
        # return False