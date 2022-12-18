def solution(n):

    res = [[0]*n for i in range(n)]
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    cur_dir = 0
    x, y = 0, 0
    i = 1
    while i <= n*n:
        res[x][y] = i
        i += 1
        next_x = x + dir[cur_dir][0]
        next_y = y + dir[cur_dir][1]
        if 0 <= next_x < n and 0 <= next_y < n and res[next_x][next_y] == 0:
            x = next_x
            y = next_y
        else:
            cur_dir = (cur_dir + 1) % 4
            x += dir[cur_dir][0]
            y += dir[cur_dir][1]
    
    return res
