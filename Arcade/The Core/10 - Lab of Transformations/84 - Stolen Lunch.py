def solution(note):

    table = str.maketrans("0123456789abcdefghij", "abcdefghij0123456789")
    return note.translate(table)
