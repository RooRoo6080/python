# Tic - Tac - Toe
import random
Squares = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " ", "extra": ""}
Count = 0
ways_to_win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


def grid(squares):
    print("")
    print("", squares[1], "|", squares[2], "|", squares[3])
    print("---+---+---")
    print("", squares[4], "|", squares[5], "|", squares[6])
    print("---+---+---")
    print("", squares[7], "|", squares[8], "|", squares[9], "\n\n")


def complete():
    def foo(l, count, sign, win_lose):
        for done in l:
            for finish in done:
                if Squares[finish] == sign:
                    count += 1
                    if count == 3:
                        print ("------- YOU", win_lose, "-------")
                        exit()
            count = 0
    foo(ways_to_win, Count, "X", "WON!")
    foo(ways_to_win, Count, "O", "LOST!")


def ai(l, squares, sign):
    for bo in l:
        playerTwoInRow = 0
        placesToPlay = 0
        for le in bo:
            if squares[le] == sign:
                playerTwoInRow += 1
            elif squares[le] == " ":
                placesToPlay += le
        if playerTwoInRow == 2 and placesToPlay != 0 and Squares[placesToPlay] == " ":
            squares[placesToPlay] = "O"
            global computerPlayed
            computerPlayed = True
            break


grid(Squares)
full_board = 0
while full_board < 9:
    computerPlayed = False
    full_board = 0
    player_turn = int(input("Pick your square (1-9):\n"))
    if 1 <= player_turn <= 9 and Squares[player_turn] == " ":
        Squares[player_turn] = "X"
    else:
        print("\nOops! You can't play in that square!\n")
    grid(Squares)
    complete()
    print("Computers turn:\n")
    ai(ways_to_win, Squares, "O")
    if not computerPlayed:
        ai(ways_to_win, Squares, "X")
    if not computerPlayed:
        eligible_squares = []
        for j in Squares:
            if Squares[j] == " ":
                eligible_squares.append(j)
        if eligible_squares:
            computer_choice = random.choice(eligible_squares)
            Squares[computer_choice] = "O"
    grid(Squares)
    complete()
    for i in range(1, 10):
        if Squares[i] != " ":
            full_board += 1

print("------- TIE! -------")
