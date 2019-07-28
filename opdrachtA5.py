import math


def register_spot(spot, str):
    for i in range(numSpots):
        if i != spot and str[i] == "1":
            # print(spot, "can go to", i)
            routes[spot].append(i)


def find_route(past_spots):
    if len(past_spots) == numSpots:
        return past_spots

    if past_spots:
        current_routes = routes[past_spots[-1]]
        # current = past_spots[-1]
    else:
        current_routes = range(numSpots)
        # current = "none"
    for i in range(len(current_routes)):
        dest = current_routes[i]
        # print("ENTRIES OF", current, ": ", ', '.join(map(str, current_routes)))
        if dest not in past_spots:
            # print("from ", current, " going to ", dest)
            new_spots = past_spots.copy()
            new_spots.append(dest)
            found_route = find_route(new_spots)
            if found_route:
                return found_route


numSpots = int(input())
routes = []
for i in range(numSpots):
    routes.append([])
for i in range(numSpots):
    register_spot(i, input())


def numToLetter(n):
    return chr(n + 65)


print("".join(map(numToLetter, find_route([]))))


