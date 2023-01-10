def solution(shoes):

    return all([shoes.count(i) == shoes.count([1 - i[0], i[1]]) for i in shoes])
