class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        for i in range (0, len(mat)):
            for j in range(0, len(mat[0])):
                if i == j or i+j == len(mat)-1:
                    sum += mat[i][j]
                elif len(mat) == 1 and len(mat[0]) == 1:
                    return mat[i][j]
        return sum


        