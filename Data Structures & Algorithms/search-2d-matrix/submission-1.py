class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) > 2:
            mid = len(matrix) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                newmatrix = matrix[mid:]
                return self.searchMatrix(newmatrix, target)
            elif matrix[mid][0] > target:
                newmatrix = matrix[:mid]
                return self.searchMatrix(newmatrix, target)
        else:
            matrixlist = []
            for i in range(len(matrix)):
                matrixlist += matrix[i]
            
            L = len(matrixlist)
            left = 0
            right = L-1
            while left <= right:
                middle = left + (right-left)//2
                test = matrixlist[middle]
                if test == target:
                    return True
                elif test < target:
                    left += 1
                elif test > target:
                    right -= 1
            return False
        return self.searchMatrix(matrix,target)
        