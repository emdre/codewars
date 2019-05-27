"""Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string."""


def capitals(word):
    lst = []
    position = -1
    for letter in word:
        if letter.isupper():
            position = word.index(letter, position + 1)
            lst.append(position)
    return lst

print(capitals('CodEWaRsssRRRRRRddsE')) # test
