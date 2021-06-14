from random_words import RandomWords
import time


def random_word():
    random = RandomWords()
    w = random.random_word()
    return w


def sentence(length):
    s = ""
    for k in range(0, length):
        s += str(random_word()) + " "
    return s


raw_sentence = sentence(5)
S = list(raw_sentence)
lenS = len(S)
wrong_count = 0
for countdown in range(10, 0, -1):
    print(countdown)
    time.sleep(1)
start = time.time()
user_sentence = input(raw_sentence + "\n") + " "
end = time.time()
X = list(user_sentence)
lenX = len(X)
if lenX > lenS:
    for i in range(0, lenX - lenS):
        S.append("#")
elif lenS > lenX:
    for delta in range(0, lenS - lenX):
        X.append("#")
for i in range(0, len(S)):
    if S[i] != X[i]:
        wrong_count += 1
per = 100 - ((wrong_count * 100) / len(S))
print("\n\n")
print(end - start, "seconds")
print(per, "percent correct")
print(len(X), "characters or 5 words")
print(wrong_count, "wrong characters")
print(((len(X) / 5) - wrong_count) / ((end - start) / 60), "is your Net WPM / Score")
