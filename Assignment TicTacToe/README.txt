My program is simulating the TicTacToe Game for two players and display the state table of each players at the end of the game.


display_board(board) -> display the game board in the console when the function is called

check_in_game(board) -> check if there is still some places in the board, return a boolean

check_win(board) -> check if any players won the game during the turn, return a boolean

main() -> here the real game is happening, the board is displayed evry turn and the players are asked to enter the position 
that they want for their piece. All the previous function are called here and the states table of the players are created and displayed.