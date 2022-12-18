def solution(grid):
    import numpy
    arr = numpy.array(grid)
    
    for r in range(3):
        for c in range(3):
            l = r*3 + c
            if len(numpy.unique(arr[l, :])) < 9:
                return False
            if len(numpy.unique(arr[:, l])) < 9:
                return False
            if len(numpy.unique(arr[r*3:r*3 + 3, c*3:c*3 + 3])) < 9:
                return False
    
    return True
