def solution(coins, price):

    res = 0
    for coin in reversed(coins):
        d, price = divmod(price, coin)
        res += d
    return res
