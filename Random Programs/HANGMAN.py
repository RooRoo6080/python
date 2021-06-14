from random_words import RandomWords


def hangman():
    global tries
    print("   _________   ")
    print("   |       |   ")
    print("   |       O   ")
    print("   |      /|\\ ")
    print("   |      /\\  ")
    print("   |      L L  ")
    print("___|___        ")


def indexAll(list, input):
    r = []
    count = 0
    for i in list:
        if input == i:
            r.append(count)
        count += 1
    return r


h = " "
tries = 6


def random_word():
    random = RandomWords()
    w = random.random_word()
    return w


print("--------------- HANGMAN ---------------- \n")
print("You have", tries, "tries to guess the word")
word = random_word()
lw = list(str(word))
l = len(word)
a = []
for i in range(0, l):
    a.append("_")
print(h.join(a))
while tries != 0:
    g = input("Guess a letter or the word:")
    if g in lw:
        c = indexAll(lw, g)
        for ya in c:
            del a[ya]
            a.insert(ya, g)
        print("Yup,", g, "is in the word!")
        print(h.join(a), "\n")
        if a == lw:
            print("GREAT JOB! You won!")
            break
    elif g == word:
        print("GREAT JOB! You won!")
        break
    elif g not in lw:
        tries -= 1
        print(g, "is not in the word. Please try again. You have", tries, "more tries.\n")
else:
    print("GAME OVER! You lost. Try again next time! The correct word was", word)
