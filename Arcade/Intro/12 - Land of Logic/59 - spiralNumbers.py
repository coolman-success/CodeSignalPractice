def solution(n):

    res = [[0]*n for i in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y = 0, -1
    dir, num = 0, 0
    
    while num < n*n:
        for j in range(n - (dir + 1) // 2):
            num += 1
            x += dx[dir % 4]
            y += dy[dir % 4]
            res[x][y] = num
        dir += 1
    
    return res
