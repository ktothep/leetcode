v = 19
available_coins = [1, 5, 10, 25]
res = []


def count_money(v, index):
    if v == 0:
        return res
    if v - available_coins[index] < 0:
        count_money(v, index - 1)
    else:
        v = v - available_coins[index]
        res.append(available_coins[index])
        count_money(v, index)


count_money(v, len(available_coins) - 1)
print(res)
