def solution(symbol):

    return "not a digit" if not symbol.isdigit() else "odd" if int(symbol)%2 else "even"
