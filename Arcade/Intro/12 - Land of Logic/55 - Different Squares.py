def solution(matrix):

    rows, cols = len(matrix), len(matrix[0])
    squares = set()
    for i in range(rows - 1):
        for j in range(cols - 1):
            squares.add((matrix[i][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1]))
    return len(squares)
