def solution(matrix):
    
    rows, cols = len(matrix), len(matrix[0])
    
    def neighbor(i, j):
        l, r = max(0, j - 1), min(cols, j + 2)
        t, b = max(0, i - 1), min(rows, i + 2)
        return sum([sum(matrix[ind][l:r]) for ind in range(t, b)]) - matrix[i][j]
    
    return [[neighbor(i, j) for j in range(cols)] for i in range(rows)]
