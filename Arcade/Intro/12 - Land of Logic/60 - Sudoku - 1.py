def solution(grid):

    def not_pass(l):
        return len(set(l)) != 9
    
    # check row
    if any(not_pass(row) for row in grid):
        return False
    
    # check column
    if any(not_pass(col) for col in zip(*grid)):
        return False
    
    # 3*3 square
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = [grid[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not_pass(square):
                return False
    
    return True
