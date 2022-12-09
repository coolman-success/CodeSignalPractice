def solution(young, beautiful, loved):

    # (young and beautiful and not loved) or (loved and (not young or not beautiful))
    # (young and beautiful and not loved) or (loved and not (young and beautiful))
    # ((young and beautiful) and not loved) or (not (young and beautiful) and loved)
    return (young and beautiful) ^ loved
