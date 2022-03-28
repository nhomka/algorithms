def knapsack(items, pack_size):
    dp = [0]*(1+pack_size)
    used = [[] for _ in range(pack_size+1)]
    print(dp, used)
    
    for i in range(pack_size+1):
        for item in items:
            if item[0] <= i:

                if item[0] in used[i-item[0]]:
                    continue
                else:
                    if dp[i-item[0]] + item[1] > dp[i]:
                        dp[i] = dp[i-item[0]] + item[1]
                        used[i] = used[i-item[0]] + [item[0]]
    print(dp, used)
    return max(zip(dp, used), key = lambda x: x[0])

items = [(2, 3), (3, 4), (4, 8), (5, 8), (9, 10)]
size = 10
print(knapsack(items, size))