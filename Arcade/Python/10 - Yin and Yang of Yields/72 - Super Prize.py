class Prizes(object):
    def __init__(self, purchases, n, d):
        self.d = d
        self.n = n
        self.purchases = purchases
    
    def __iter__(self):
        for i in range((self.n - 1), len(self.purchases), self.n):
            if self.purchases[i] % self.d == 0:
                yield i + 1

def solution(purchases, n, d):
    return list(Prizes(purchases, n, d))
