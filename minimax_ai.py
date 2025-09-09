
from functions import *
import copy

def minimax_ai(board, player):
    #print(f"\n--- AI ({player}) is thinking... ---")
    best_move = None
    best_score = None
    legal_moves = get_all_legal_moves(board)
    move_scores = {}
    for move in legal_moves:
        board_copy = copy.deepcopy(board)
        make_move(board_copy, move, player)

        opp = "O" if player == "X" else "X"
        score = minimax_score(board_copy, opp, player)
        move_scores[tuple(move) ] = score
        #print(f"AI evaluates move {move}: final score = {score}")

        if best_score is None or score > best_score:
            best_move = move
            best_score = score


    # print("--- AI's Final Analysis ---")
    # for move, score in move_scores.items():
    #     result = "???"
    #     if score == 10: result = "Guarantees a WIN"
    #     elif score == 0: result = "Leads to a DRAW"
    #     elif score == -10: result = "Leads to a LOSS"
    #     print(f"  - Move {move}: {result} (Score: {score})")

    # print(f"-> AI chooses move: {best_move} (Highest Score)")
    return best_move

    #print(best_move)
    #if best_move is None
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
        board_copy = copy.deepcopy(board)
        make_move(board_copy, move, player_to_move)

        opp = "O" if player_to_move == "X" else "X"
        opp_best_response_score = minimax_score(board_copy, opp ,player_to_opt)
        scores.append(opp_best_response_score)

    if player_to_move == player_to_opt:
        return max(scores)
    else:
        return min(scores)

        