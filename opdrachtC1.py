strategies = 0


def fit(current_value, max_val):
    global strategies, available_coins, goal_value
    if current_value == goal_value:
        strategies = strategies + 1
        return

    remaining_value = goal_value - current_value

    end = min(remaining_value, max_val)

    if end == 1:
        strategies += 1
        return
    for i in range(len(available_coins)):
        coin = available_coins[i]
        if coin > end:
            break

        fit(current_value+coin, coin)


num_coins = int(input())
available_coins = []
for i in range(num_coins):
    available_coins.append(int(input()))
available_coins.sort()
goal_value = int(input())
fit(0, goal_value)
print(strategies)


