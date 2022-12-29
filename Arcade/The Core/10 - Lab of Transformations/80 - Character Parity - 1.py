def solution(symbol):

    try:
        x = int(symbol)
        return "odd" if x % 2 else "even"
    except ValueError:
        return "not a digit"
