from functions import *
from heuristic_ais import *
from minimax_ai import *

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

        
def play_random_ai():
    players = ["X", "O"]

    turn_number = 0 
    board = new_board()

    while True:
        current_player = players[turn_number%2] # if even X, odd O
        render(board)

        print(f"Players {current_player} turn!" )
        player_move = random_ai_move(board, current_player)
        if make_move(board, player_move, current_player):
            make_move(board, player_move, current_player)
            turn_number+=1
        
        


        winner = get_winner(board)
        if winner is not None:
            render(board)
            print(f"winner is {current_player}")
            break

        if is_board_full(board):
            render(board)
            print(f"draw")
            break

def play_winning_moves_ai():
    players = ["X", "O"]

    turn_number = 0 
    board = new_board()

    while True:
        current_player = players[turn_number%2] # if even X, odd O
        render(board)

        print(f"Players {current_player} turn!" )
        player_move = find_owns_winning_moves_ai(board, current_player)
        if make_move(board, player_move, current_player):
            make_move(board, player_move, current_player)
            turn_number+=1
        
        


        winner = get_winner(board)
        if winner is not None:
            render(board)
            print(f"winner is {current_player}")
            break

        if is_board_full(board):
            render(board)
            print(f"draw")
            break
        

def play_winning_and_blocking_moves_ai():
    players = ["X", "O"]

    turn_number = 0 
    board = new_board()

    while True:
        current_player = players[turn_number%2] # if even X, odd O
        render(board)

        print(f"Players {current_player} turn!" )
        player_move = finds_all_winning_moves_ai(board, current_player)
        if make_move(board, player_move, current_player):
            make_move(board, player_move, current_player)
            turn_number+=1
        
        


        winner = get_winner(board)
        if winner is not None:
            render(board)
            print(f"winner is {current_player}")
            break

        if is_board_full(board):
            render(board)
            print(f"draw")
            break

def play_against_winning_and_blocking_ai():
    players = ["X", "O"]

    turn_number = 0 
    board = new_board()

    while True:
        current_player = players[turn_number%2] # if even X, odd O
        render(board)

        print(f"Players {current_player} turn!" )


        if current_player == 'X':
            player_move = minimax_ai(board, current_player)
        else:
            player_move = minimax_ai(board, current_player)
        if make_move(board, player_move, current_player):
            make_move(board, player_move, current_player)
            turn_number+=1
        
        


        winner = get_winner(board)
        if winner is not None:
            render(board)
            print(f"winner is {current_player}")
            break

        if is_board_full(board):
            render(board)
            print(f"draw")
            break

if __name__ == "__main__":
    play_against_winning_and_blocking_ai()


