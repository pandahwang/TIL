import random

wordnum = random.randint(0,4)
words = ["apple", "pear", "bee", "person", "pineapple"]
word = words[wordnum]
print(word)
blank = []

for i in range(len(word)):
    blank.append("_")
print(blank)

guess = input()
if guess in word:
    print("Correct!")
    