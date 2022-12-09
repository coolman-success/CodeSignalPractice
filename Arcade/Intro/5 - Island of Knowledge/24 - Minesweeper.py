def solution(matrix):
    
    rows, cols = len(matrix), len(matrix[0])
    
    def neighbor(i, j):
        res = -matrix[i][j]
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if 0 <= x < rows and 0 <= y < cols:
                    res += matrix[x][y]
        return res
    
    return [[neighbor(i, j) for j in range(cols)] for i in range(rows)]
