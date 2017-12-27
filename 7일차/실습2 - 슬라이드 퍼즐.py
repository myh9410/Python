0def get_number():
    num = input("Type the number you want to move(Type 0 to quit): ")
    while not (num.isdigit() and 0 <= int(num) <= 15):
        num = input("Type the number you want to move(Type 0 to quit): ")
    return int(num)

def create_init_board():
0
def set_goal_board():
    return [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]

def print_board(board):
    for row in board:
        for item in row:
            if item == 0:
                print("  ",end = " ")
            elif 10 <= item <= 15:
                print(item,end=" ")
            else:
                print(str(item).rjust(2),end=" ")
        print()
        
def find_position(num,board):
    for i in range(len(board)):
        for j in range(len(board)):
            if num == board[i][j]:
                return (i,j)

def move(pos,opened,board):
    (x,y) = pos
    if opened == (x-1,y) or opened == (x+1,y) or \
       opened == (x,y-1) or opened == (x,y+1):
        board[opened[0]][opened[1]] = board[x][y]
        board[x][y] = 0
        return (pos,board)
    else:
        print("Can't move! Try again.")
        return (opened,board)

def sliding_puzzle():
    board = create_init_board()
    goal = set_goal_board()
    opened = (3,3)
    while True:
        print_board(board)
        if board == goal:
            print("Congratulations!")
            break
        num = get_number()
        if num == 0:
            break
        pos = find_position(num,board)
        (opened,board) = move(pos,opened,board)
        print("Please come again.")
sliding_puzzle()
