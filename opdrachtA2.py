word = input()

closed = [1, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
open = [2, 0, 2, 0, 3, 3, 2, 4, 2, 2, 4, 2, 2, 2, 0, 1, 2, 2, 2, 3, 2, 2, 2, 4, 3, 2]

a = 65

numClosed = 0
numOpen = 0
for i in range(len(word)):
    letter = ord(word[i]) - a
    numClosed += closed[letter]
    numOpen += open[letter]

print(numClosed)
print(numOpen)
