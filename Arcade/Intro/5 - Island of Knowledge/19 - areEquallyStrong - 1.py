def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    you = set([yourLeft, yourRight])
    friend = set([friendsLeft, friendsRight])
    return you == friend
