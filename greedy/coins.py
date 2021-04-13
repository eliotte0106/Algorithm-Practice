def change():
    n = int(input()) # change amount
    coins = [10,50,100,500] # kinds of coins
    coins.sort(reverse=True)
    cnt = 0
    # for i in range(len(coins)):
    #     cnt += n // coins[i]
    #     n %= coins[i]
    for coin in coins:
        cnt += n // coin #count
        n %= coin # remainder
    return cnt
print(change())
