def solution(image):

    rows, cols = len(image), len(image[0])
    res = [[]]
    
    for i in range(rows - 2):
        for j in range(cols - 2):
            mean = sum(sum(row[j:j + 3]) for row in image[i:i + 3])//9
            res[i].append(mean)
        res.append([])
    
    return res[:-1]
