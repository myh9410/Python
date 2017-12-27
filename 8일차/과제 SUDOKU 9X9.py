#3번째 과제
#수독 9X9
#이름 : 문용호
#학번 : 2014037938
import random

################################################################################
#1.수독정답만들기
#정답 만들기 1단계
def create_board(): #수독 보드를 만들어줌
    seed = [1,2,3,4,5,6,7,8,9]
    random.shuffle(seed)
    row0 = seed[:]
    row1 = seed[3:6] + seed[6:9] + seed[0:3]
    row2 = seed[6:9] + seed[0:3] + seed[3:6] 
    row3 = seed[1:2] + seed[2:3] + seed[0:1] + seed[4:5] + seed[5:6] + seed[3:4] + seed[7:8] + seed[8:9] + seed[6:7]
    row4 = seed[4:5] + seed[5:6] + seed[3:4] + seed[7:8] + seed[8:9] + seed[6:7] + seed[1:2] + seed[2:3] + seed[0:1]
    row5 = seed[7:8] + seed[8:9] + seed[6:7] + seed[1:2] + seed[2:3] + seed[0:1] + seed[4:5] + seed[5:6] + seed[3:4]
    row6 = seed[2:3] + seed[0:1] + seed[1:2] + seed[5:6] + seed[3:4] + seed[4:5] + seed[8:9] + seed[6:7] + seed[7:8]
    row7 = seed[5:6] + seed[3:4] + seed[4:5] + seed[8:9] + seed[6:7] + seed[7:8] + seed[2:3] + seed[0:1] + seed[1:2]
    row8 = seed[8:9] + seed[6:7] + seed[7:8] + seed[2:3] + seed[0:1] + seed[1:2] + seed[5:6] + seed[3:4] + seed[4:5]
    return [row0,row1,row2,row3,row4,row5,row6,row7,row8]
#정답 만들기 2단계
def shuffle_ribons(board): #보드를 top,mid,bottom으로 나누어서 무작위로 섞어줌
    top,mid,bottom = board[:3],board[3:6],board[6:9]
    random.shuffle(top)
    random.shuffle(mid)
    random.shuffle(bottom)
    board = top + mid + bottom
    return board
################################################################################
#2.가로/세로 바꾸기
def transpose(board): #가로줄과 세로줄을 바꾸어 주는 함수
    transposed = [[],[],[],[],[],[],[],[],[]]
    for i in board:
        c = 0
        for j in i:
            transposed[c].append(j)
            c = c + 1
    return transposed

#수독 정답 만들기 총정리
def create_solution_board(): #transpose를 이용해 가로줄과 세로줄을 섞어준후 무작위로 섞어준 후 다시 transpose로 바꾸어줌.
    return transpose(shuffle_ribons(transpose(shuffle_ribons(create_board()))))
################################################################################
#3.퍼즐 보드 만들기
#난이도 입력받기
def get_level(): #상,중,하 중 난이도 선택(빈칸 갯수 : 상 - 40개 중 - 34개 하 - 28개)
    level = input("난이도 (상,중,하)중에서 하나 선택하여 입력 : ")
    while level not in {'상','중','하'} :
        level = input("난이도 (상,중,하)중에서 하나 선택하여 입력 : ")
    if level == '하' : return 28
    elif level == '중' : return 34
    elif level == '상' : return 40
#정답 보드 복제 하기
def copy_board(board): #정답보드와 문제를 풀 보드를 구분하기위해 복제
    board_clone = []
    for row in board :
        row_clone = row[:]
        board_clone.append(row_clone)
    return board_clone
#퍼즐 보드 만들기
def make_holes(board,no_of_holes):
    holeset = set()
    while no_of_holes > 0:
        i = random.randint(0,8)
        j = random.randint(0,8)
        if (i+1,j+1) not in holeset : #보드에서 가로줄과 세로줄이 1부터 시작함
            board[i][j] = 0
            holeset.add((i+1,j+1))
            no_of_holes -= 1
    return board, holeset
################################################################################
#4.입출력
#보드 보여주기
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
#정수 입력받기       
def get_integer(txt,minimum,maximum):
    i = input(txt)
    while not (i.isdigit() and minimum<= int(i) <=maximum):
        i = input(txt)
    return int(i)
################################################################################
        
def sudokumini():
    solution = create_solution_board()               
    no_of_holes = get_level()                        
    puzzle = copy_board(solution)                    
    (puzzle,holeset) = make_holes(puzzle,no_of_holes)
    show_board(puzzle)                                
    while True:
        i = get_integer("가로줄번호(1~9): ",1,9)       
        j = get_integer("세로줄번호(1~9): ",1,9)
        if (i,j) not in holeset:                      
            print('빈칸이 아닙니다. ')
            continue
        n = get_integer("숫자 (1~9): ",1,9)           
        sol = solution[i-1][j-1]     #보드에서 가로줄과 세로줄을 입력받을때 1부터 입력받으므로 sol의 값이 보드에서i-1,j-1의위치번호에 있는 수가 되도록 한다.
        if n == sol :                                 
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
