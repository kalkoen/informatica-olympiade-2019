n = int(input())
m = int(input())
v = int(input())

for i in range(m):
    for j in range(n + v*i):
        print("*", end="")
    print()

