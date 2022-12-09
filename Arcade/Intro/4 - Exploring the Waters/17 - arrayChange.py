def solution(inputArray):

    moves = 0
    prev = inputArray[0]
    for x in inputArray[1:]:
        if x <= prev:
            moves += prev + 1 - x
            prev += 1
        else:
            prev = x
    
    return moves
