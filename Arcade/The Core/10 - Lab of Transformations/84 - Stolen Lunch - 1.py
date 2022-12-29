def solution(note):

    D, L = "0123456789", "abcdefghij"
    table = str.maketrans(D + L, L + D)
    return note.translate(table)
