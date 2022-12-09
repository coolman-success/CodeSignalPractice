def solution(image):

    rows, cols = len(image), len(image[0])
    
    return [[sum(sum(row[j:j + 3]) for row in image[i:i + 3])//9
                    for j in range(cols - 2)]
                    for i in range(rows - 2)]
