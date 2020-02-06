import random
import time

#display the game board
def display_board(board):
    print("_________________", end = '\n')

    i = 0
    while i < 7:
        print("| ", board[i], " |", board[i+1], " |",  board[i+2], " |")
        i+=3

    print("_________________", end = '\n')

#check if there is still some empty spaces in the board
def check_in_game(board):
    in_game = False
    for e in board:
        if e == " ":
            in_game = True
            break
    return in_game

#check if a player won the game or not
def check_win(board):
    if board[0] == board[1] and board[1] == board[2] and board[0] != " ":
        return board[0]
    elif board[3] == board[4] and board[4] == board[5] and board[3] != " ":
        return board[3]
    elif board[6] == board[7] and board[7] == board[8] and board[6] != " ":
        return board[6]
    elif board[0] == board[3] and board[3] == board[6] and board[0] != " ":
        return board[0]
    elif board[1] == board[4] and board[4] == board[7] and board[1] != " ":
        return board[1]
    elif board[2] == board[5] and board[5] == board[8] and board[2] != " ":
        return board[2]
    elif board[0] == board[4] and board[4] == board[8] and board[0] != " ":
        return board[0]
    elif board[2] == board[4] and board[4] == board[6] and board[2] != " ":
        return board[2]
    else:
        return None


#main function of the game
def main():

    #creating the board, the states table and the boolean values that we need
    board = [" "]*9
    in_game = True
    win = False
    winner = None
    round_turn = True
    Otab = []
    Xtab = []

    #main loop of the game, display the board and ask the players to enter their position
    while in_game and not win:
        display_board(board)

        #fiiling the states table
        tab = []
        for i in range(len(board)):
            if board[i] == " ":
                tab.append("Empty")
            else:
                tab.append("Full")

        #asking the player for his wanted position
        completed = False
        while not completed:
            '''index = random.randrange(9)
            if board[index] == " ":
                #completed = True'''
            src = input("Please enter a number between zero to eight to place your piece !")
            if board[int(src)] == " ":
                completed = True
            else:
                print("Please enter a valid number")

        if round_turn:
            board[int(src)] = 'O'
            Otab.append(tab)
            round_turn = False
        else:
            board[int(src)] = 'X'
            Xtab.append(tab)
            round_turn = True

        #checking the game state
        in_game = check_in_game(board)
        winner = check_win(board)
        if winner:
            win = True


    #displaying the winner and the state table
    if not win:
        display_board(board)
        print("It's a DRAW !!")
    else:
        display_board(board)
        print(winner, " Won The GAAME !")

    print('\n')
    print("Here is the state table for O player : ", end='\n')
    for i in range(len(Otab)):
        print("Turn ", i, " =", Otab[i], end='\n')

    print('\n')
    print("Here is the state table for X  player : ", end='\n')
    for i in range(len(Xtab)):
        print("Turn ", i, " =", Xtab[i], end='\n')

    print('\n')
    print(winner, " won the game.")


#testing funtion
def test():
    board = [0]*9
    for i in range(len(board)):
        board[i] = i
    display_board(board)

#test()
main()