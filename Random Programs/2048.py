"""# The 2048 game
import random
gridFull = False
largestLength = 1
dash = ""
WASD = {"w": -4, "a": -1, "s": 4, "d": 1}
side_spots = {"w": [1, 2, 3, 4], "a": [1, 5, 9, 13], "s": [13, 14, 15, 16], "d": [4, 8, 12, 16]}
square = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " ", 10: " ", 11: " ", 12: " ", 13: " ",
          14: " ", 15: " ", 16: " "}
gS = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: "", 11: "", 12: "", 13: "",
      14: "", 15: "", 16: ""}


def grid(spots):
    global dash
    print "", spots[1] + gS[1], "|", spots[2] + gS[2], "|", spots[3] + gS[3], "|", spots[4] + gS[4]
    print "---" + dash + "+---" + dash + "+---" + dash + "+---" + dash + ""
    print "", spots[5] + gS[5], "|", spots[6] + gS[6], "|", spots[7] + gS[7], "|", spots[8] + gS[8]
    print "---" + dash + "+---" + dash + "+---" + dash + "+---" + dash + ""
    print "", spots[9] + gS[9], "|", spots[10] + gS[10], "|", spots[11] + gS[11], "|", spots[12] + gS[12]
    print "---" + dash + "+---" + dash + "+---" + dash + "+---" + dash + ""
    print "", spots[13] + gS[13], "|", spots[14] + gS[14], "|", spots[15] + gS[15], "|", spots[16] + gS[16], "\n\n"


def play(wasd, squares, sideSpots):
    global gS
    global largestLength
    direction = raw_input("Pick a direction (wasd):\n")
    for letter in wasd:
        if direction == letter:
            for k in range(1, 4):
                for j in squares:
                    if squares[j] != " " and j not in sideSpots[letter] and squares[j + wasd[letter]] == squares[j]:
                        gS[j + wasd[letter]] = gS[j]
                        squares[j + wasd[letter]] = str(int(squares[j]) * 2)
                        squares[j] = " "
                        gS[j] = ""
                        for l in range(1, largestLength):
                            gS[j] += " "
                    elif squares[j] != " " and j not in sideSpots[letter] and squares[j + wasd[letter]] == " ":
                        gS[j + wasd[letter]] = gS[j]
                        squares[j + wasd[letter]] = squares[j]
                        squares[j] = " "
                        gS[j] = ""
                        for l in range(1, largestLength):
                            gS[j] += " "


while True:
    upGrid = False
    openChoices = []
    gridSize = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    for i in square:
        if square[i] == " ":
            openChoices.append(i)
        elif square[i] == "2048":
            print "\n\n ------- YOU WON! ------- \n\n"
            grid(square)
            exit()
        if len(square[i]) > largestLength:
            gridSize.remove(i)
            upGrid = True
        elif len(square[i]) == largestLength:
            gS[i] = ""
        elif 1 < largestLength < len(square[i]):
            gS = ""
            for b in range(0, largestLength - len(square[i])):
                gS[i] += " "
    if upGrid:
        for i in gridSize:
            gS[i] += " "
        dash += "-"
        largestLength += 1
    if openChoices:
        nextLetter = random.choice(openChoices)
        square[nextLetter] = "2"
    else:
        gridFull = True
    grid(square)
    g1 = square
    play(WASD, square, side_spots)
    if g1 == square and gridFull:
        print "------- YOU LOST! -------\n\n"
        exit()
"""