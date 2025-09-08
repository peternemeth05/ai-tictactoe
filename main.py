from functions import *

def play():
    players = ["X", "O"]

    turn_number = 0 
    board = new_board()

    while True:
        current_player = players[turn_number%2] # if even X, odd O
        render(board)

        print(f"Players {current_player} turn!" )
        player_move = get_move()
        make_move(board, player_move, current_player)


        winner = get_winner(board)
        if winner is not None:
            render(board)
            print(f"winner is {current_player}")
            break

        if is_board_full(board):
            render(board)
            print(f"draw")
            break

        turn_number+=1

        
def random_ai():



if __name__ == "__main__":


