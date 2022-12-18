def solution(cell):

    from itertools import product, chain

    row, col = int(cell[1]) - 1, ord(cell[0]) - ord('a')
    L1, L2 = [2, -2], [1, -1]
    cnt = 0

    for off_x, off_y in chain(product(L1, L2), product(L2, L1)):

        if 0 <= row + off_y < 8 and 0 <= col + off_x < 8:
            cnt += 1

    return cnt
