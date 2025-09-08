import random
from functions import *

def human_player(board, player):
    x_co_ord = int(input("X?: "))
    y_co_ord = int(input("Y?: "))
    return (x_co_ord, y_co_ord)

def random_ai_move(board, player):
    move_map = {0: [0,0], 1: [1,0], 2: [2,0],
                3: [0,1], 4: [1,1], 5: [2,1],
                6: [0,2], 7: [1,2], 8: [2,2]}
    
    rand_move = int(random.uniform(0,9))

    return move_map[rand_move]

def blocks_their_winning_moves_ai(board, player):
    opp = "O" if player == "X" else "X"

    their_winning_move = find_owns_winning_moves_ai(board, opp)
    if their_winning_move:
        return their_winning_move
    else:
        return random_ai_move(board)
    

def find_owns_winning_moves_ai(board,player):
    my_winning_move = finds_winning_moves_ai(board,player)
    if my_winning_move:
        return my_winning_move
    else:
        return random_ai_move(board,player)
    

def finds_all_winning_moves_ai(board, player):
    opp = "O" if player == "X" else "X"
    my_winning_move = finds_winning_moves_ai(board, player)
    if my_winning_move:
        return my_winning_move

    their_winning_move = finds_winning_moves_ai(board, opp)
    if their_winning_move:
        return their_winning_move
    
    return random_ai_move(board,player)



def finds_winning_moves_ai(board, player):
    all_line_coords = get_all_line_coords()

    for line in all_line_coords:
        
        n_me = 0
        n_them = 0
        n_new = 0
        last_new_coord = None

        for [x,y] in line:
            value = board[y][x]
            if value == player:
                n_me +=1
            elif value == ' ':
                n_new +=1
                last_new_coord = [x,y]
            else:
                n_them +=1

        if n_me == 2 and n_new == 1:
            return last_new_coord

    

    



