def solution(cell1, cell2):

    def getcolor(cell):
        col = ord(cell[0]) - ord('a')
        row = ord(cell[1]) - ord('1')
        return (row + col) % 2

    return getcolor(cell1) == getcolor(cell2)