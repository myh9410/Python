import random

############################################################################
#실습1 - 수독정답만들기
#1-1 정답 만들기 1단계
def create_board():
    seed = [1,2,3,4]
    random.shuffle(seed)
    row0 = seed[:]
    row1 = seed[2:] + seed[:2]
    row2 = seed[1:2] + seed[0:1] + seed[3:4] + seed[2:3]
    row3 = seed[3:4] + seed[2:3] + seed[1:2] + seed[0:1]
    return [row0,row1,row2,row3]
#1-1-2 정답 만들기 2단계
def shuffle_ribons(board):
    top,bottom = board[:2],board[2:]
    random.shuffle(top)
    random.shuffle(bottom)
    board = top + bottom
    return board
############################################################################
#실습2 - 가로/세로 바꾸기
def transpose(board):
    transposed = [[],[],[],[]]
    for x in board:
        i = 0
        for e in x:
            transposed[i].append(e)
            i = i + 1
    return transposed

#수독 정답 만들기 총정리
def create_solution_board():
    return transpose(shuffle_ribons(transpose(shuffle_ribons(create_board()))))
############################################################################
#3 - 퍼즐 보드 만들기
#실습3
#3-1 난이도 입력받기
def get_level():
    level = input("난이도 (상,중,하)중에서 하나 선택하여 입력 : ")
    while level not in {'상','중','하'} :
        level = input("난이도 (상,중,하)중에서 하나 선택하여 입력 : ")
    if level == '하' : return 6
    elif level == '중' : return 8
    elif level == '상' : return 10
#3-2 정답 보드 복제 하기
def copy_board(board):
    board_clone = []
    for row in board :
        row_clone = row[:]
        board_clone.append(row_clone)
    return board_clone
############################################################################
#실습4 - 퍼즐 보드 만들기
def make_holes(board,no_of_holes):
    holeset = set()
    while no_of_holes > 0:
        i = random.randint(0,3)
        j = random.randint(0,3)
        if (i+1,j+1) not in holeset : 
            board[i][j] = 0
            holeset.add((i+1,j+1))
            no_of_holes -= 1
    return board, holeset
#4 - 입출력
#실습5 - 보드 보여주기
def show_board(board):
    for i in range(len(board) + 1):
        if i == 0:
            print("+",end = "  ")
        else:
            print(i,end = "  ")
    print("")
    for i in range(len(board)) :
        print(i+1,end = "  ")
        for j in range(len(board)) :
            if board[i][j] == 0 :
                print('.',end = "  ")
            else:
                print(board[i][j],end = "  ")
        print("")
#실습6 - 정수 입력받기       
def get_integer(txt,minimum,maximum):
    i = input(txt)
    while not (i.isdigit() and minimum<= int(i) <=maximum):
        i = input(txt)
    return int(i)
########################################################################
        
def sudokumini():
    solution = create_solution_board()                #1
    no_of_holes = get_level()                         #2
    puzzle = copy_board(solution)                     #3
    (puzzle,holeset) = make_holes(puzzle,no_of_holes) #4,5
    show_board(puzzle)                                #6
    while True:
        i = get_integer("가로줄번호(1~4): ",1,4)       #7-A
        j = get_integer("세로줄번호(1~4): ",1,4)
        if (i,j) not in holeset:                      #7-B
            print('빈칸이 아닙니다. ')
            continue
        n = get_integer("숫자 (1~4): ",1,4)           #7-C
        sol = solution[i-1][j-1]
        if n == sol :                                 #7-D
            puzzle[i-1][j-1] = sol
            show_board(puzzle)
            holeset.remove((i,j))
            no_of_holes -= 1
        else:
            print(n,"가 아닙니다. 다시 해보세요.")
        if no_of_holes== 0:                           #종료조건검사
            print("잘 하셨습니다. 또 들리세요.")
            break
sudokumini()
