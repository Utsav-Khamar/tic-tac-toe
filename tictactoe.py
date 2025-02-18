import random, time

def playerwins(board, mv):

    if board[1] == mv and board[2] == mv and board[3] == mv: #bottom row
        return True
    elif board[4] == mv and board[5] == mv and board[6] == mv: #middle
        return True
    elif board[7] == mv and board[8] == mv and board[9] == mv: #above row
        return True
    elif board[1] == mv and board[4] == mv and board[7] == mv: #left column
        return True
    elif board[2] == mv and board[5] == mv and board[8] == mv: #middle column
        return True
    elif grid[3] == mv and board[6] == mv and board[9] == mv: #right column
        return True
    elif board[7] == mv and board[5] == mv and board[3] == mv: #diagonal
        return True
    elif board[1] == mv and board[5] == mv and board[9] == mv: #diagonal
        return True
    else:
        return False

def computermove(board, emptSpace, cp, usr):
    #check if computer wins
    print()
    for ele in emptSpace:
        board[ele] = cp
        if playerwins(board, cp):
            return ele
        else:
            board[ele] = " "

    #check to make sure that opponent doesn't win
    for ele in emptSpace:
        board[ele] = usr
        if playerwins(board, usr):

            return ele
        else:
            board[ele] = " "

    #play the remaining moves
    return random.choice(emptSpace)



print("\n\nWelcome to the game of Tic Tac Toe:")
while True:
    print("Choose x,o or q to exit:")
    userInput = input().strip()

    if userInput == "q" or userInput == "Q":
        break
    elif userInput == "x" or userInput == "X":
        user = "x"
        computer = "o"
    elif userInput == "o" or userInput == "O":
        user = "o"
        computer = "x"
    else:
        print("Enter valid input")
        continue

    print("remember to put your input like a numpad on your keyboard")
    print("7 | 8 | 9")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("1 | 2 | 3")
    print("\n\n\n")

    emptySpace = [1,2,3,4,5,6,7,8,9]
    start = ""
    if random.randint(0,1)==0:
        start = user
    else:
        start = computer

    grid = {
        7: " ", 8: " ", 9: " ",
        4: " ", 5: " ", 6: " ",
        1: " ", 2: " ", 3: " "
    }

    if start == computer:
        print("We'll start with computer's move.")
    else:
        print("You start the game")

    currentMove = start
    while emptySpace:
        win = False
        if currentMove==computer:
            print("Computer plays:")
            time.sleep(1)
            #move = random.choice(emptySpace) #computerPlays(grid)

            move  = computermove(grid, emptySpace, computer, user)
            emptySpace.remove(move)
            grid[move] = computer
            win = playerwins(grid, computer)

        else:
            print("Enter your move:")
            move = int(input())

            if move not in emptySpace:
                print("That's an illegal move, computer already played that. Play another move")
                continue
            else:
                emptySpace.remove(move)
                grid[move] = user

                win = playerwins(grid, user)

        print("{} | {} | {}".format(grid[7], grid[8], grid[9]))
        print("---------")
        print("{} | {} | {}".format(grid[4], grid[5], grid[6]))
        print("---------")
        print("{} | {} | {}".format(grid[1], grid[2], grid[3]))
        print()

        if currentMove==computer:
            if win:
                print("Computer won")
                break
            else:
                currentMove=user
        else:
            if win:
                print("You won")
                break
            else:
                currentMove=computer

        if not emptySpace and not win:
            print("It's a draw.")










