def solution(users):
    res = [CodeSignalUser(*user) for user in users]
    res.sort(reverse=True)
    return list(map(str, res))

class CodeSignalUser:
    def __init__(self, username, id, xp):
        self.username = username
        self.id = int(id)
        self.xp = int(xp)
    
    def __str__(self):
        return self.username
    
    def __lt__(self, other):
        return (self.xp, -self.id) < (other.xp, -other.id)
