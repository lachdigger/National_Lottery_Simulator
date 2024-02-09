import random

warningMessage1 = "Are you sure you want to enter a number greater than 59. If you do you will be facing a 0% chance of winning a prize. \n Please enter y if you choose to lose money or n to rethink your decision : "


def lotteryModel(numbers, amountOfGames):
    prize1Count = 0
    prize2Count = 0
    prize3Count = 0
    prize4Count = 0
    prize5Count = 0
    prize6Count = 0

    if amountOfGames < 0:
        amountOfGames = 1

    for i in range(0, amountOfGames):
        # code for one round.
        # last number will always be the bonus one.
        global prizeLevel
        prizeLevel = 0
        gameNumbers = []
        # randomly generates 6 numbers
        for j in range(0, 6):
            random_number = random.randint(0, 59)
            gameNumbers.append(random_number)
        # check names

        for k in range(0, len(gameNumbers)):
            if int(numbers[k]) == int(gameNumbers[k]):
                # print("you have won a prize")
                if k == 0 and prizeLevel == 0:
                    prize1Count += 1
                    prizeLevel = 1
                elif k == 1 and prizeLevel == 1:
                    prize2Count += 1
                    prizeLevel = 2
                elif k == 2 and prizeLevel == 2:
                    prize3Count += 1
                    prizeLevel = 3
                elif k == 3 and prizeLevel == 3:
                    prize4Count += 1
                    prizeLevel = 4
                elif k == 4 and prizeLevel == 4:
                    prize5Count += 1
                    prizeLevel = 5
                elif k == 5 and prizeLevel == 5:
                    prize6Count += 1
                    prizeLevel = 6

    return [prize1Count, prize2Count, prize3Count, prize4Count, prize5Count, prize6Count]


amountOfRounds = int(input("Please enter the amount of games you would like to run : "))
inputNumbers = []
while len(inputNumbers) < 6:
    try:
        num = int(input("please input a number: "))
    except:
        print("INVALID -- please enter a number")
        continue

    if num > 59:
        if input(warningMessage1) == "y":
            inputNumbers.append(num)
            continue
        else:
            print("good choice")
            continue
    elif 59 > num > 0:
        inputNumbers.append(num)
        continue
    elif num < 0:
        print("please enter a number greater than 0")
        continue

    inputNumbers.append(input("please input a number: "))

# print(lotteryModel(inputNumbers,1000000))
result = lotteryModel(inputNumbers,amountOfRounds)

for i in range(0, 6):
    print(f"\nyou have won {result[i]} many {i} level prizes \n")
