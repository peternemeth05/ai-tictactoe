from functions import *
from heuristic_ais import *
from minimax_ai import *
import itertools

PLAYER_MAP = {
    "human": get_move,  # The human player uses get_move to ask for input
    "random": random_ai_move,
    "winning": find_owns_winning_moves_ai,
    "blocking": blocks_their_winning_moves_ai,
    "minimax": minimax_ai
}

AI_PLAYER_MAP = {
    "random": random_ai_move,
    "winning": find_owns_winning_moves_ai,
    "blocking": blocks_their_winning_moves_ai,
    "minimax": minimax_ai
}

def play(player1_type, player2_type):

    # find the functions
    try:
        player1_func = PLAYER_MAP[player1_type]
        player2_func = PLAYER_MAP[player2_type]
    except KeyError:
        print("Error: Invalid player type specified.")
        print(f"Available types are: {list(PLAYER_MAP.keys())}")
        return

    players = ["X", "O"]

    turn_number = 0 
    board = new_board()

    while True:
        current_player = players[turn_number%2] # if even X, odd O
        render(board)

        print(f"Players {current_player} turn!" )

        if current_player == 'X':
            player_move = player1_func(board, current_player)
        else:
            player_move = player2_func(board, current_player)

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


def play_silent(player1_func, player2_func):

    """
    Plays a single game of Tic-Tac-Toe without any console output.
    This version is robust and handles illegal moves by forcing a forfeit.

    Args:
        player1_func: The function for player 'X'.
        player2_func: The function for player 'O'.

    Returns:
        str: The winner ('X', 'O') or 'draw'.
    """
    players = {
        "X": player1_func,
        "O": player2_func
    }
    board = new_board()
    turn_number = 0

    while True:
        current_symbol = "X" if turn_number % 2 == 0 else "O"
        current_player_func = players[current_symbol]

        # AI gets its move
        move = current_player_func(board, current_symbol)

        # Handle cases where an AI might fail to produce a move
        if move is None:
            # This can happen if the board is full or there's a bug.
            # The other player wins by forfeit.
            return "O" if current_symbol == "X" else "X"

        # Make the move and check if it was successful
        move_successful = make_move(board, move, current_symbol)

        if move_successful:
            turn_number += 1
        else:
            # The AI made an illegal move (e.g., on an occupied square).
            # This is a bug in that AI's logic, so it forfeits.
            return "O" if current_symbol == "X" else "X"

        # Check for a winner or a draw
        winner = get_winner(board)
        if winner:
            return winner
        if is_board_full(board):
            return "draw"



def run_tournament(num_games = 10):
    """
    Pits every AI agsints everyother AI (and itself) and prints the results
    """
    ai_names = list(AI_PLAYER_MAP.keys())
    all_results = {name: {} for name in ai_names}

    # Use itertools.product to get all combinations of players
    for p1_name, p2_name in itertools.product(ai_names, repeat=2):
        p1_func = AI_PLAYER_MAP[p1_name]
        p2_func = AI_PLAYER_MAP[p2_name]

        matchup_results = {"X": 0, "O": 0, "draw": 0}

        print(f"--- Running Matchup: {p1_name} (X) vs. {p2_name} (O) ---")

        for i in range(num_games):
            print(f"\r  Game {i + 1}/{num_games}", end="")
            winner = play_silent(p1_func, p2_func)
            if winner == "X":
                matchup_results["X"] += 1
            elif winner == "O":
                matchup_results["O"] += 1
            else:
                matchup_results["draw"] += 1
        
        print("\r  ...Done!                     ")
        all_results[p1_name][p2_name] = matchup_results
        

        # Calculate and print percentages
        p1_win_pct = (matchup_results["X"] / num_games) * 100
        p2_win_pct = (matchup_results["O"] / num_games) * 100
        draw_pct = (matchup_results["draw"] / num_games) * 100

        print(f"  Results after {num_games} games:")
        print(f"    -> {p1_name} (X) wins: {p1_win_pct:.1f}% ({matchup_results['X']} games)")
        print(f"    -> {p2_name} (O) wins: {p2_win_pct:.1f}% ({matchup_results['O']} games)")
        print(f"    -> Draws: {draw_pct:.1f}% ({matchup_results['draw']} games)")

    return all_results, ai_names, num_games

def display_summary_graph(all_results, ai_names, num_games):
    """
    Calculates overall win rates and displays them as an ASCII bar chart.
    """
    print("\n\n--- AI Power Rankings (Overall Win Rate) ---")
    
    power_scores = {name: 0 for name in ai_names}

    # Calculate total wins for each AI
    for p1_name, p2_name in itertools.product(ai_names, repeat=2):
        # Add wins when playing as Player 1 (X)
        power_scores[p1_name] += all_results[p1_name][p2_name]['X']
        # Add wins when playing as Player 2 (O)
        power_scores[p2_name] += all_results[p1_name][p2_name]['O']

    # Calculate percentages
    total_games_played = len(ai_names) * num_games * 2 # Each AI plays as X and O
    win_percentages = {
        name: (wins / total_games_played) * 100
        for name, wins in power_scores.items()
    }

    # Sort by percentage for a clean ranking
    sorted_ais = sorted(win_percentages.items(), key=lambda item: item[1], reverse=True)

    # Display the graph
    max_name_len = max(len(name) for name in ai_names)
    for name, pct in sorted_ais:
        bar_length = int(pct / 2) # Scale the bar length
        bar = '█' * bar_length
        print(f"{name:>{max_name_len}} | {pct:5.1f}% | {bar}")


def display_results_table(all_results, ai_names, num_games):
    """
    Displays the tournament results in a formatted ASCII table.
    """
    print("\n\n--- Tic-Tac-Toe AI Tournament Results ---")
    print(f"({num_games} games per matchup)\n")

    col_width = max(len(name) for name in ai_names) + 6

    # Print header row
    header = f"{'Player (X)':<{col_width}} |"
    for name in ai_names:
        header += f" {name:<{col_width-2}} |"
    print(header)
    print("-" * len(header))

    # Print each player's results against others
    for p1_name in ai_names:
        row_str = f"{p1_name:<{col_width}} |"
        for p2_name in ai_names:
            results = all_results[p1_name][p2_name]
            p1_wins = results['X']
            p2_wins = results['O']
            draws = results['draw']
            
            # Format: 90W - 0L - 10D
            cell_str = f"{p1_wins}W - {p2_wins}L - {draws}D"
            row_str += f" {cell_str:<{col_width-2}} |"
        print(row_str)
    
    print("-" * len(header))
    print("Read as: Row Player (X) vs. Column Player (O)")


if __name__ == "__main__":



# EDIT THIS LINE TOO PIT DIFFERNT BOTS/HUMANS AGAINST EACHOTHER
    # play(player1_type = "minimax", player2_type = "human")

    # "human": get_move,  # The human player uses get_move to ask for input
    # "random": random_ai_move,
    # "winning": find_owns_winning_moves_ai,
    # "blocking": blocks_their_winning_moves_ai,
    # "minimax": minimax_ai


    results, names, games = run_tournament(10)

    display_results_table(results, names, games)
    display_summary_graph(results, names, games)



