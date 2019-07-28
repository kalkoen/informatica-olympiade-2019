word = input()

nums = ["TWEE", "DRIE", "VIER", "VIJF", "ZES", "ZEVEN", "ACHT", "NEGEN"]


def search(word, num):
    letter_index = 0
    letter = num[letter_index]
    for i in range(len(word)):
        if word[i] == letter:
            letter_index += 1
            if letter_index == len(num):
                return 1
            letter = num[letter_index]
    return 0


def go():
    for i in range(len(nums)):
        if search(word, nums[i]):
            print(nums[i])
            return
    print("geen")

go()

