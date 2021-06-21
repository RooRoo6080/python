import discord
import random
from random_words import RandomWords
import time

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


async def complete(message, ways_to_win, Count, Squares):
    async def foo(l, count, sign, win_lose, message, Squares):
        for done in l:
            for finish in done:
                if Squares[finish] == sign:
                    count += 1
                    if count == 3:
                        await message.channel.send("------- YOU " + win_lose + " -------")
                        close = True
                        return close
            count = 0

    if await foo(ways_to_win, Count, "X", "WON!", message, Squares):
        return True
    if await foo(ways_to_win, Count, "O", "LOST!", message, Squares):
        return True


async def random_word():
    random = RandomWords()
    w = random.random_word()
    return w


async def sentence(length):
    s = ""
    for k in range(0, length):
        s += str(await random_word()) + " "
    return s


async def ai(l, Squares, sign):
    for bo in l:
        playerTwoInRow = 0
        placesToPlay = 0
        for le in bo:
            if Squares[le] == sign:
                playerTwoInRow += 1
            elif Squares[le] == "--":
                placesToPlay += le
        if playerTwoInRow == 2 and placesToPlay != 0 and Squares[placesToPlay] == "--":
            Squares[placesToPlay] = "O"
            computerPlayed = True
            return computerPlayed


async def indexAll(list, input):
    r = []
    count = 0
    for i in list:
        if input == i:
            r.append(count)
        count += 1
    return r


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for _help"))


@client.event
async def on_member_remove(member):
    try:
        guild = member.guild
        await guild.text_channels[0].send("{} left the server".format(member))
    except Exception:
        pass


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("_"):
        try:
            print("someone used the bot! ")
        except Exception:
            pass
        if message.content.startswith("_help"):
            embed = discord.Embed(title="alright, calling 911...", description="you can: \nuse _roast to get wrecked\nuse _ttt to "
                                       "play tic-tac-toe \nuse _test to see how slow you type \nuse _hangman to play "
                                       "hangman \nuse _poll question: option; option; etc. (up to 10) \nuse _2048 to play 2048"
                                       "\n\nuse _feedback and then your feedback to help me improve this bot!"
                                       "\nuse _share to receive the link to add this bot to your server"
                                       "\n\n\nDISCLAIMER: This bot may not be active all the time as I do not "
                                       "have a server to run it on.\n\nOther features:\nthe bot logs when someone leaves the server"
                                       , color=0xFF2C3B)
            await message.channel.send(embed=embed)

        elif message.content.startswith("_feedback"):
            print(message)
            print(message.content)
            await message.channel.send("Thanks for your feedback")

        elif message.content.startswith("_share"):
            await message.channel.send("You can use this link to add this bot to your server:\n"
                                       "https://discord.com/api/oauth2/authorize?client_id=833781878514384966&permissions=8&scope=bot")

        if message.content.startswith("_roast"):
            roasts = ["achoo, sorry, I'm allergic to BS", "You're as useless as the ueue in queue",
                      "Mirrors can't talk. Lucky for you, they can't laugh either",
                      "If I wanted to kill myself I'd climb your ego and jump to your IQ",
                      "Yes, that ugly face in the mirror is you",
                      "Light travels faster than sound, which is why you seemed bright until you spoke",
                      "Your face makes onions cry",
                      "If your brain was dynamite it wouldn't be enough to blow your hat off",
                      "I thought of you today. It reminded me to take out the trash",
                      "OH MY GOD IT SPEAKS",
                      ]
            await message.channel.send(random.choice(roasts))

        elif message.content.startswith("_ttt"):

            async def grid(squares, message):
                a = squares[1] + '  ' + squares[2] + '  ' + squares[3]
                c = squares[4] + '  ' + squares[5] + '  ' + squares[6]
                e = squares[7] + '  ' + squares[8] + '  ' + squares[9]
                b = a + "\n" + c + "\n" + e
                await message.channel.send(b)

            await message.channel.send("Tic-tac-toe\nuse 'quit' to retire")
            await message.channel.send("starting...")
            Squares = {1: "--", 2: "--", 3: "--", 4: "--", 5: "--", 6: "--", 7: "--", 8: "--", 9: "--", "extra": ""}
            Count = 0
            ways_to_win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
            close = False

            await grid(Squares, message)
            full_board = 0
            while full_board < 9:
                full_board = 0
                await message.channel.send("Pick your square (1-9):")
                playerTurn = await client.wait_for('message')
                while playerTurn.content not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'quit']:
                    await message.channel.send("Pick your square (1-9):")
                    playerTurn = await client.wait_for('message', check=lambda
                        check: check.author == message.author and check.channel == message.channel)
                if 'quit' not in playerTurn.content:
                    player_turn = int(playerTurn.content)
                    if 1 <= player_turn <= 9 and Squares[player_turn] == "--":
                        Squares[player_turn] = "X"
                    else:
                        await message.channel.send("\nOops! You can't play in that square!\n")
                    await grid(Squares, message)
                    if await complete(message, ways_to_win, Count, Squares):
                        close = True
                        break
                    else:
                        await message.channel.send("Computer's turn:")
                        if not await ai(ways_to_win, Squares, "O"):
                            if not await ai(ways_to_win, Squares, "X"):
                                eligible_squares = []
                                for j in Squares:
                                    if Squares[j] == "--":
                                        eligible_squares.append(j)
                                if eligible_squares:
                                    computer_choice = random.choice(eligible_squares)
                                    Squares[computer_choice] = "O"
                        await grid(Squares, message)
                        if await complete(message, ways_to_win, Count, Squares):
                            close = True
                            break
                        else:
                            for i in range(1, 10):
                                if Squares[i] != "--":
                                    full_board += 1
                else:
                    await message.channel.send("------- PLAYER RETIRED -------")
                    close = True
                    break

            if not close:
                await message.channel.send("------- TIE! -------")

        elif message.content.startswith('_test'):
            await message.channel.send("Typing Speed Test")
            raw_sentence = await sentence(5)
            S = list(raw_sentence)
            lenS = len(S)
            wrong_count = 0
            for countdown in range(3, 0, -1):
                await message.channel.send(countdown)
                time.sleep(1)
            start = time.time()
            await message.channel.send(raw_sentence + "\n")
            userInput = await client.wait_for('message', check=lambda
                check: check.author == message.author and check.channel == message.channel)
            user_sentence = userInput.content + " "
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

            seconds = str(end - start) + ' seconds'
            percent = str(per) + ' percent correct'
            characters = str(len(X)) + ' characters or 5 words'
            wrongCount = str(wrong_count) + ' wrong characters'
            wpm = str(((len(X) / 5) - wrong_count) / ((end - start) / 60)) + ' is your Net WPM / Score'
            result = seconds + "\n" + percent + "\n" + characters + "\n" + wrongCount + "\n" + wpm
            await message.channel.send(result)

        elif message.content.startswith('_hangman'):
            tries = 8
            await message.channel.send("--------------- HANGMAN ---------------- \n")
            send = "You have " + str(tries) + " tries to guess the word; use 'quit' to retire"
            await message.channel.send(send)
            word = await random_word()
            lw = list(str(word))
            l = len(word)
            a = []
            for i in range(0, l):
                a.append("-")
            await message.channel.send(" ".join(a))
            while tries != 0:
                await message.channel.send("Guess a letter or the word:")
                m = await client.wait_for('message', check=lambda
                    check: check.author == message.author and check.channel == message.channel)
                if m.content != 'quit':
                    g = m.content
                    if g in lw:
                        c = await indexAll(lw, g)
                        for ya in c:
                            del a[ya]
                            a.insert(ya, g)
                        send = "Yup, " + str(g) + " is in the word!"
                        await message.channel.send(send)
                        send = " ".join(a) + " \n"
                        await message.channel.send(send)
                        if a == lw:
                            await message.channel.send("GREAT JOB! You won!")
                            break
                    elif g == word:
                        await message.channel.send("GREAT JOB! You won!")
                        break
                    elif g not in lw:
                        tries -= 1
                        send = str(g) + " is not in the word. Please try again. You have " + str(
                            tries) + " more tries.\n"
                        await message.channel.send(send)
                else:
                    tries = 0
            else:
                send = "GAME OVER! You lost. Try again next time! The correct word was " + word
                await message.channel.send(send)

        elif message.content.startswith("_poll"):
            poll = message.content[6:]
            poll = poll.split(":")
            poll = poll[0].split(None, 0) + poll[1].split(";")
            des = ""
            count = 0
            for i in poll[1:]:
                count += 1
                des += str(count) + ":" + i + "\n"
            embed = discord.Embed(title=poll[0], description=des, color=0xFF2C3B)
            msg = await message.channel.send(embed=embed)
            emoji = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
            for i in range(0, count):
                await msg.add_reaction(emoji[i])

        elif message.content.startswith("_2048"):
            channel = message.channel
            await channel.send("use 'quit' to quit")
            gridFull = False
            largestLength = 1
            WASD = {"w": -4, "a": -1, "s": 4, "d": 1}
            side_spots = {"w": [1, 2, 3, 4], "a": [1, 5, 9, 13], "s": [13, 14, 15, 16], "d": [4, 8, 12, 16]}
            square = {1: "--", 2: "--", 3: "--", 4: "--", 5: "--", 6: "--", 7: "--", 8: "--", 9: "--", 10: "--",
                      11: "--", 12: "--",
                      13: "--",
                      14: "--", 15: "--", 16: "--"}
            gS = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: "", 11: "", 12: "", 13: "",
                  14: "", 15: "", 16: ""}

            async def grid(spots):
                send = "\n" + spots[1] + gS[1] + "  " + spots[2] + gS[2] + "  " + spots[3] + gS[3] + "  " + spots[4] + \
                       gS[4]
                send = send + "\n" + spots[5] + gS[5] + "  " + spots[6] + gS[6] + "  " + spots[7] + gS[7] + "  " + \
                       spots[8] + gS[8]
                send = send + "\n" + spots[9] + gS[9] + "  " + spots[10] + gS[10] + "  " + spots[11] + gS[11] + "  " + \
                       spots[12] + gS[12]
                send = send + "\n" + spots[13] + gS[13] + "  " + spots[14] + gS[14] + "  " + spots[15] + gS[15] + "  " + \
                       spots[16] + gS[16]
                await channel.send(send)

            async def score(square):
                score = 0
                for i in square:
                    if square[i] != '--':
                        score += int(square[i])
                score = "score: " + str(score)
                await channel.send(score)

            async def play(wasd, squares, sideSpots, gS, largestLength):
                await channel.send("Pick a direction (wasd):")
                direction = await client.wait_for('message', check=lambda
                    check: check.author == message.author and check.channel == message.channel)
                direction = direction.content
                if direction == "quit":
                    return True
                for letter in wasd:
                    if direction == letter:
                        for k in range(1, 4):
                            for j in squares:
                                if squares[j] != "--" and j not in sideSpots[letter] and squares[j + wasd[letter]] == \
                                        squares[j]:
                                    gS[j + wasd[letter]] = gS[j]
                                    squares[j + wasd[letter]] = str(int(squares[j]) * 2)
                                    squares[j] = "--"
                                    gS[j] = ""
                                    for l in range(1, largestLength):
                                        gS[j] += " "
                                elif squares[j] != "--" and j not in sideSpots[letter] and squares[
                                    j + wasd[letter]] == "--":
                                    gS[j + wasd[letter]] = gS[j]
                                    squares[j + wasd[letter]] = squares[j]
                                    squares[j] = "--"
                                    gS[j] = ""
                                    for l in range(1, largestLength):
                                        gS[j] += " "

            while True:
                upGrid = False
                openChoices = []
                gridSize = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
                for i in square:
                    if square[i] == "--":
                        openChoices.append(i)
                    elif square[i] == "2048":
                        await channel.send("------- YOU WON! -------")
                        await grid(square)
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
                    largestLength += 1
                if openChoices:
                    nextLetter = random.choice(openChoices)
                    square[nextLetter] = "2"
                else:
                    gridFull = True
                await grid(square)
                g1 = square
                if await play(WASD, square, side_spots, gS, largestLength):
                    await channel.send("------- YOU QUIT! -------")
                    await score(square)
                    break
                if g1 == square and gridFull:
                    await channel.send("------- YOU LOST! -------")
                    await score(square)
                    break
client.run("your token here")
