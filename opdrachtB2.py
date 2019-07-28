# Somewhat optmised brute force
# Satisfaction: 3/10

# pos (k, g) dus kanaal,gracht

absolute_maximum_distance = 50

def available_ways(pos):
    a = []
    ds = []
    if pos[1] == 0:
        for i in range(8):
            a.append((i, 1))
            ds.append(4)
        return a, ds

    side_dis = pos[1] * 3

    a.append(((pos[0] - 1) % 8, pos[1]))
    ds.append(side_dis)
    a.append(((pos[0] + 1) % 8, pos[1]))
    ds.append(side_dis)

    if pos[0] % 2 == 1:
        a.append((pos[0], pos[1] - 1))
        ds.append(4)
    else:
        if pos[1] != 3:
            a.append((pos[0], pos[1] + 1))
            ds.append(4)

    return a, ds


def shortest_distance(pos, dest, past_stops, total_dis):
    if pos == dest or (pos[1] == 0 and dest[1] == 0):
        return past_stops, total_dis

    res = available_ways(pos)
    # print("AV", res)
    ways = res[0]
    dis = res[1]

    past_stops_new = past_stops.copy()
    past_stops_new.append(pos)
    # print("PS", past_stops )

    lowest_dis_from_here = 100000
    path = []
    for i in range(len(ways)):
        stop = ways[i]
        d = dis[i]
        if stop in past_stops:
            continue

        if total_dis + d > min(absolute_maximum_distance, lowest_dis_from_here):
            continue

        res_path = shortest_distance(stop, dest, past_stops_new, total_dis + d)

        if res_path[1] < lowest_dis_from_here:
            lowest_dis_from_here = res_path[1]
            path = res_path[0]

    return path, lowest_dis_from_here


distances = []


def populate_distances():
    for odd_even in range(2):
        distances.append([])
        for startg in range(4):
            distances[odd_even].append([])
            for endk in range(5):
                distances[odd_even][startg].append([])
                for endg in range(4):
                    distances[odd_even][startg][endk].append(
                        shortest_distance((odd_even, startg), (odd_even + endk, endg), [], 0)[1])


def calculated_distance(pos, dest):
    odd_even = pos[0] % 2
    startg = pos[1]
    endk = int(min(abs(pos[0] - dest[0]), pos[0] + 8 - dest[0], abs(pos[0] - 8 - dest[0])))
    endg = dest[1]
    return distances[odd_even][startg][endk][endg]


populate_distances()

it = 0


def shortest_route(houses, startpos, past_stops, total_dis):
    global it
    if not houses:
        it += 1
        return past_stops, total_dis + calculated_distance(startpos, (0, 0))

    shortest_route_so_far = ([], 10000)
    for i in range(len(houses)):
        house = houses[i]
        new_houses = houses.copy()
        new_houses.remove(house)
        new_past_stops = past_stops.copy()
        new_past_stops.append(house)

        side_dis = house[1] * 3

        for j in range(2):
            next_pos = (int((house[0] + j - 0.5) % 8), house[1])
            new_total_dis = total_dis + calculated_distance(startpos, next_pos) + side_dis
            new_start_pos = (int((house[0] - j + 0.5) % 8), house[1])
            shortest_route_from_here = shortest_route(new_houses, new_start_pos, new_past_stops, new_total_dis)
            if shortest_route_from_here[1] < shortest_route_so_far[1]:
                shortest_route_so_far = shortest_route_from_here

    return shortest_route_so_far


des_houses = [(6.5, 3), (5.5, 1), (4.5, 1), (4.5, 2), (2.5, 3), (1.5, 2)]

print(shortest_distance((0, 3), (3, 2), [], 0))
print(calculated_distance((0, 3), (3, 2)))
print(shortest_route(des_houses, (0, 0), [], 0))
print(it)
