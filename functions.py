def new_board() -> list:
    return [[' ' for _ in range(3)] for _ in range(3)]


def render(board):
    print("     0  1  2")
    print("   -----------")

    for y in range(3):
        print(f'{y} |  ', end='')

        for x in range(3):
            print(board[y][x], end = '  ')
            pass

        print('|')
    print("   -----------")




def get_move(board, player):
    print()
    try: 
        x_coord = int(input("What is your move's X coordinate?: "))
        y_coord = int(input("What is your move's Y coordinate?: "))

        return [x_coord, y_coord]
    except ValueError:
       # print("Error, please input number 0 -> 2 \n")
        return get_move()
    
    
def make_move(board, move_coords, player):
    x_coord, y_coord = move_coords

    if board[y_coord][x_coord] == " ":
        board[y_coord][x_coord] = player
        return board
    else:
        #print("someone has already played there!")
        return False # FIX: Return the board unmodified


def get_winner(board):
    all_line_coords = get_all_line_coords()

    for line in all_line_coords:
        line_values = [board[y][x] for (x,y) in line]
        if len(set(line_values)) == 1 and line_values[0] != " ":
            return line_values[0]

    return None

def get_all_line_coords():

    cols = []
    for x in range(0, 3):
        col = []
        for y in range(0, 3):
            col.append((x, y))
        cols.append(col)

    rows = []
    for y in range(0, 3):
        row = []
        for x in range(0, 3):
            row.append((x, y))
        rows.append(row)

    diagonals = [
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    return( cols + rows + diagonals)


def is_board_full(board):
    for col in board:
        for sq in col:
            if sq is " ":
                return False
    return True

def get_all_legal_moves(board):
    legal_moves = []
    for y, row in enumerate(board):
        for x, val in enumerate(row):
            if val == ' ':
                legal_moves.append([x,y])
    return legal_moves
