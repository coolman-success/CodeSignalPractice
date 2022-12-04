def solution(matrix):
    
    rows = len(matrix)
    cols = len(matrix[0])
    sum = 0
    
    for i in range(cols):
        for j in range(rows):
            if matrix[j][i] == 0:
                break
            else:
                sum += matrix[j][i]
    
    return sum
