def solution(bishop, pawn):

    if ord(bishop[0]) + int(bishop[1]) == ord(pawn[0]) + int(pawn[1]):
        return True
    if ord(bishop[0]) - ord(pawn[0]) == int(bishop[1]) - int(pawn[1]):
        return True
    return False
