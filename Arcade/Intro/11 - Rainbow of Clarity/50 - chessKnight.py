def solution(cell):

    row, col = int(cell[1]), ord(cell[0]) - ord('a') + 1
    move = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
    cnt = 0

    for off_x, off_y in move:

        if 0 < row + off_y < 9 and 0 < col + off_x < 9:
            cnt += 1

    return cnt
