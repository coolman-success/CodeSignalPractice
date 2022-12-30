class Prizes(object):
    def __init__(self, purchases, n, d):
        self.i = -1
        self.d = d
        self.n = n
        self.purchases = purchases
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            self.i += self.n
            if self.i >= len(self.purchases):
                raise StopIteration
            elif self.purchases[self.i] % self.d == 0:
                return self.i + 1

def solution(purchases, n, d):
    return list(Prizes(purchases, n, d))
