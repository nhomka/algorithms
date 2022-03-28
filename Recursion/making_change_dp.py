def make_change_memoization(coin_value_list, change, cache):
    min_coins = change
    if change in coin_value_list:
        cache[change] = 1
        return 1
    elif cache[change] > 0:
        return cache[change]
    else:
        for coin in [c for c in coin_value_list if c < change]:
            num_coins = 1 + make_change_memoization(coin_value_list, change - coin, cache)
            min_coins = min(min_coins, num_coins)
            cache[change] = min_coins
    return min_coins

change = 33

print(make_change_memoization([1, 5, 10, 25], change, [0] * (change+1)))

def make_change_dp(coin_value_list, change):
    dp = [float('inf')] * (change+1)
    dp[0] = 0
    for cents in range(1, change+1):
        for coin in coin_value_list:
            if cents - coin >= 0:
                dp[cents] = min(dp[cents], dp[cents-coin] + 1)
    print(dp)
    return dp[change]

print(make_change_dp([1, 5, 8, 10, 25], change))