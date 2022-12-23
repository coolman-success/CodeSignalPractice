def solution(coins, price):

    i, res = -1, []
    while price:
        res.append(price//coins[i])
        price %= coins[i]
        i -= 1
    return sum(res)
