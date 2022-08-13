import random

words = ["cat", "baba", "dog", "hydrogen", "dumb", "door", "rectangle", "progamming", "computer", "ten"]


for i in range(10):
    x = random.randrange(1, 10)
    word = words[x]
    length = len(word)
    print("The word has " + str(length) + " characters" )
    print("The first letter is: " + word[0])
    char = input()
    if char == word:
        print("Good Job")
    else:
        print("You lost, the word is: " + word)