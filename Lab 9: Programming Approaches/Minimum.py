def make_change(coins, change, coin_counts, coin_values):
    for i in range(1, change+1):  # change in cents
        count = i
        coin = 1
        for j in coins:  # coin nominations
            if j > i:
                break
            if coin_counts[i-j] + 1 < count:  # compare coin counts
                count = coin_counts[i-j]+1
                coin = j
        coin_counts[i] = count      # number of coins
        coin_values[i] = coin       # value of the coin
    return coin_counts[change]


def print_coins(used, change):
    while change > 0:
        coin = used[change]
        print(coin, end=' ')
        change -= coin
    print()


if __name__ == '__main__':
    change = 64
    coins = [1, 5, 10, 21, 25]
    coin_values = [0]*(change+1)  # values of coins
    coin_counts = [0]*(change+1)  # number of coins
    print("Making change for", change, "requires ",
          make_change(coins, change, coin_counts, coin_values), "coins:")
    print_coins(coin_values, change)

    change = 14
    coins = [1, 5, 7, 10]
    coin_values = [0]*(change+1)  # values of coins
    coin_counts = [0]*(change+1)  # number of coins
    print("Making change for", change, "requires ",
          make_change(coins, change, coin_counts, coin_values), "coins:")
    print_coins(coin_values, change)
