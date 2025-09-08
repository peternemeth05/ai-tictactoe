
from functions import *
import copy

def minimax_ai(board, player):
    best_move = None
    best_score = None
    for move in get_all_legal_moves(board):
        board = copy.deepcopy(board)
        make_move(player, board, move)

        opp = "O" if player == "X" else "X"
        score = minimax_score(board, opp, player)

        if best_score is None or score > best_score:
            best_move = move
            best_score = score

    print(best_move)
    return( best_move)




def minimax_score(board, player_to_move, player_to_opt):
    winner = get_winner(board)

    if winner is not None:
        if winner == player_to_opt:
            return 10
        else:
            return -10
        
    elif is_board_full(board):
        return 0
    
    legal_moves = get_all_legal_moves(board)

    scores = []

    for move in legal_moves:
        board = copy.deepcopy(board)
        make_move(player_to_move, board, move)

        opp = "O" if player_to_move == "X" else "X"
        opp_best_response_score = minimax_score(board, opp ,player_to_opt)
        scores.append(opp_best_response_score)

    if player_to_move == player_to_opt:
        return max(scores)
    else:
        return min(scores)

        