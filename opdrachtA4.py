import math

num = int(input())

n = num


def nextNum(current):
    next = current
    string = str(current)
    for i in range(len(string)):
        next += int(string[i])
    return next

def nextNumProper(current):
    c = current
    size = math.floor(math.log(c, 10))
    div = math.pow(10, size)
    while c > 0:
        sub = math.floor(c / div)
        current += sub
        c -= sub * div
        div /= 10
    return current

def match(number, streamBases):
    streams = streamBases.copy()
    while number < 1000000:
        for i in range(len(streams)):
            while streams[i] < number:
                streams[i] = nextNumProper(streams[i])
            if streams[i] == number:
                return streamBases[i], number
        number = nextNumProper(number)


result = match(num, [1, 3, 9])
print(result[0])
print(result[1])