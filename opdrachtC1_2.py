

def fit(goal, max_val):

    if (goal,max_val) in possible_searches:
        return possible_searches[goal, max_val]

    if goal <= 1 or max_val == 1:
        return 1

    end = min(goal, max_val)

    strategies = 0
    for i in range(len(available_coins)):
        coin = available_coins[i]
        if coin > end:
            break

        search_result = fit(goal-coin, coin)
        possible_searches[goal-coin, coin] = search_result
        strategies += search_result

    return strategies


possible_searches = dict()

num_coins = int(input())
available_coins = []
for i in range(num_coins):
    available_coins.append(int(input()))
available_coins.sort()
goal_value = int(input())
print(fit(goal_value, goal_value))


