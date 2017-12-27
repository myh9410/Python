#설계프로젝트
#게임명 : 프리셀(FREECELL)
#작성자 : 문용호
#학번 : 201403793

# 게임 방법
#각각 네 가지 홈 셀에 같은 무늬의 카드 13장으로 이루어진 4개의 카드 스택을 만듭니다. 카드 스택을 다 쌓게 되면 게임에서 승리합니다.

    #셀 : 카드를 보관할 수 있는 공간

    #프리셀 : 카드를 임시로 놓아둘 수 있는 곳

    #홈셀 : 게임에서 승리하기 위해 카드스택을 쌓는 곳

#각 열의 맨 아래에 있는 카드를 빼내 다음과 같은 방법으로 옮깁니다.

    #열 → 프리셀
    #   각 프리셀에는 하나의 카드만 둘 수 있다.

    #열 → 열 or 프리셀 → 열
    #   열에는 카드를 내림차순으로 순서대로 놓아야 합니다.
    #   서로 다른 색의 카드를 번갈아 놓아야 합니다.

    #열 → 홈 셀
    #   각 스택은 에이스로 시작되는 같은 무늬의 카드로 이루어져야 합니다.

#게임이 종료되면 새로운 게임을 시작할 것인지 물어본다.
import random

def deck() :#카드가 52장 들어있는 덱을 만들어줌.
    suits = {"♡", "◇", "♧", "♤"}
    ranks = {"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"}
    deck = []
    for i in suits:
        for j in ranks:
            deck.append({"suit":i, "rank":j})
    random.shuffle(deck)
    return deck

def show_main_board(card):#총 8줄로 카드가 7장씩 4줄 6장씩 4줄로 나타나도록 설정.
    print()
    max = 0#줄의 길이
    for i in range(8):#각 행에 대해서
        if int(len(card[i])) >= max:#선택한 행의 열의 카드의 수가 max보다 크거나 같으면
            max = len(card[i])#max와 선택한 열의 카드 수를 같게 설정.
    for i in range(max):#max까지 카드검사를 해서
        for j in range(8):
            if int(len(card[j])) >= i+1:#len(card[i])까지는 카드를 내주고
                print(card[j][i],"  ",end = "  ")
            else:#그 외의 경우 다음과 같이 내줌.(" ㅇ   " 는 줄맞춤 오류 방지)
                print(" ㅇ   ",end="   ")
        print()

def show_freecell_board(freecell):#프리셀 보드를 보여주는 함수.
    print()
    print("Freecell : ", end = " ")
    for i in range(len(freecell)):
        print(freecell[i], "  ", end = " ")
    print()

def show_homecell_board(homecell):#홈셀 보드를 보여주는 함수.
    print("Homecell : ", end = " ")
    for i in range(len(homecell)):
        print(homecell[i], "  ", end = " ")
    print()
        
def compare(card1,card2):#card1 == xi[1:3],card2 == xj[1:3]  card1<card2 면 True
                         #card['rank']의 크기를 비교해 주는 함수. - 카드를 옮길때 자신보다 하나 큰 숫자에만 카드를 옮길 수 있다. - 는 조건에 사용함.
    return (card1=="A " and card2 == "2 ") or (card1=="10" and card2=="J ") or (card1=="J " and card2=="Q ") or (card1=="Q " and card2=="K ") or (card1[0].isdigit() and card2[0].isdigit() and int(card2)-int(card1)==1)

def more(message):#게임을 더 할것인지의 여부를 물음
    answer = input(message)
    while not (answer == 'y' or answer == 'n'):#y/n 아닐경우 다시 입력
        answer = input(message)
    if answer == 'y':#'y'일 경우 새 게임 진행
        return True
    else:#'n'의 경우 게임 종료
        return False
    
##########################################################################################################################################
def freecell():
    while True:#반복되게 함수 돌림.
        print("         ----        ")
        print("Welcome to FREECELL game!")
        print("made by Moon Yong Ho")
        #처음에 프리셀과 홈셀을 빈 리스트로 내줌.
        freecell = [[],[],[],[]]
        homecell = [[],[],[],[]]
        card = [[],[],[],[],[],[],[],[]]#메인보드의 카드를 보여줄 리스트 
        carddeck = deck()
        for i in range(4):
            for j in range(7):#card를 리스트로 받음(0~3).
                card[i].append(carddeck[0]["suit"]+str(carddeck[0]["rank"]).ljust(2))
                carddeck = carddeck[1:]#받은 카드를 제외한 나머지를 carddeck으로 받음
        for i in range(4,8):
            for j in range(6):#card를 리스트로 받음(4~7)
                card[i].append(carddeck[0]["suit"]+str(carddeck[0]["rank"]).ljust(2))
                carddeck = carddeck[1:]
        while True:
            #홈셀에 카드를 다 넣으면 게임 종료. "게임에서 승리하셨습니다! 안녕히 가십시오."라는 문구를 보여줌.
            if len(homecell[0]) == 13 and len(homecell[1]) == 13 and len(homecell[2]) == 13 and len(homecell[3]) == 13:
                print()
                print("게임에서 승리하셨습니다! 안녕히 가십시오.")
                break
            show_main_board(card)#카드 52장이 있는 main_board와 빈 리스트인 freecell_board,homecell_board를 보여준다.
            show_freecell_board(freecell)
            show_homecell_board(homecell)
            r = input("카드를 옮기시겠습니까? 아니면 프리셀의 카드를 꺼내시겠습니까?(카드를 옮긴다. = 1, 프리셀의 카드를 꺼낸다. = 2)")
            while not (r == "1" or r == "2"):#잘못 입력 시 재입력
                print("다시 입력해주세요.")
                r = input("카드를 옮기시겠습니까? 아니면 프리셀의 카드를 꺼내시겠습니까?(카드를 옮긴다. = 1, 프리셀의 카드를 꺼낸다. = 2)")
            if r == "1":#"카드를 옮긴다."선택
                s = input("어떤 열의 카드를 옮기시겠습니까?(카드는 자동으로 제일 아래의 카드가 선택됩니다.)(왼쪽부터 1 ~ 8)")
                while not (s == "1" or s == "2" or s == "3" or s == "4" or s == "5" or s == "6" or s == "7" or s == "8"):
                    print("다시 입력해주세요")#잘못 입력 시 재입력
                    s = input("어느 열의 카드를 옮기시겠습니까?(왼쪽부터 1 ~ 8)")
                if s == "1":#첫번째 열의 카드를 선택했을 때.
                    x1 = card[0][len(card[0])-1]#첫번 째 열의 제일 마지막 카드를 x1으로 설정
                    t = input(x1 + "를 어디로 옮기시겠습니까?(1번 = 다른 열, 2번 = 프리셀, 3번 = 홈셀)")
                    while not (t == "1" or t == "2" or t == "3"):
                        print("다시 입력해주세요")#잘못 입력 시 재입력
                        t = input(x1 + "를 어디로 옮기시겠습니까?(1번 = 다른 열, 2번 = 프리셀, 3번 = 홈셀)")
                    if t == "1":
                        u = input(x1 + "를 어느 열로 옮기시겠습니까?(왼쪽부터 1~8)")
                        while not (u == "1" or u == "2" or u == "3" or u == "4" or u == "5" or u == "6" or u == "7" or u == "8"):
                            print("다시 입력해주세요")#잘못 입력 시 재입력
                            u = input(x1 + "를 어느 열로 옮기시겠습니까?(왼쪽부터 1~8)")
                        #이동 시킨 카드는 다른 열의 가장 끝 부분으로 이동된다. remove 와 append 메소드 이용.
                        if u == "1":
                            card[0].remove(x1)
                            card[0].append(x1)
                        elif u == "2":#1열의 카드를 선택해서 2열로 옮김
                            if card[int(u)-1] == []:#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                                card[0].remove(x1)
                                card[1].append(x1)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x2 = card[1][len(card[1])-1]
                                if (((x1[0] == "♡" or x1[0] == "◇") and (x2[0] == "♧" or x2[0] == "♤")) or ((x1[0] == "♧" or x1[0] == "♤") and (x2[0] == "♡" or x2[0] == "◇"))) and (compare(x1[1:3],x2[1:3])):
                                    card[0].remove(x1)
                                    card[1].append(x1)
                                else :#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print()
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")
                        elif u == "3":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[0].remove(x1)
                                card[2].append(x1)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x3 = card[2][len(card[2])-1]
                                if (((x1[0] == "♡" or x1[0] == "◇") and (x3[0] == "♧" or x3[0] == "♤")) or ((x1[0] == "♧" or x1[0] == "♤") and (x3[0] == "♡" or x3[0] == "◇"))) and (compare(x1[1:3],x3[1:3])):
                                    card[0].remove(x1)
                                    card[2].append(x1)
                                else :#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print()
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")                
                        elif u == "4":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[0].remove(x1)
                                card[3].append(x1)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x4 = card[3][len(card[3])-1]
                                if (((x1[0] == "♡" or x1[0] == "◇") and (x4[0] == "♧" or x4[0] == "♤")) or ((x1[0] == "♧" or x1[0] == "♤") and (x4[0] == "♡" or x4[0] == "◇"))) and (compare(x1[1:3],x4[1:3])):
                                    card[0].remove(x1)
                                    card[3].append(x1)
                                else :#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print()
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")               
                        elif u == "5":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[0].remove(x1)
                                card[4].append(x1)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x5 = card[4][len(card[4])-1]
                                if (((x1[0] == "♡" or x1[0] == "◇") and (x5[0] == "♧" or x5[0] == "♤")) or ((x1[0] == "♧" or x1[0] == "♤") and (x5[0] == "♡" or x5[0] == "◇"))) and (compare(x1[1:3],x5[1:3])):
                                    card[0].remove(x1)
                                    card[4].append(x1)
                                else :#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print()
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")                
                        elif u == "6":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[0].remove(x1)
                                card[5].append(x1)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x6 = card[5][len(card[5])-1]
                                if (((x1[0] == "♡" or x1[0] == "◇") and (x6[0] == "♧" or x6[0] == "♤")) or ((x1[0] == "♧" or x1[0] == "♤") and (x6[0] == "♡" or x6[0] == "◇"))) and (compare(x1[1:3],x6[1:3])):
                                    card[0].remove(x1)
                                    card[5].append(x1)
                                else :#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print()
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")         
                        elif u == "7":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[0].remove(x1)
                                card[6].append(x1)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x7 = card[6][len(card[6])-1]
                                if (((x1[0] == "♡" or x1[0] == "◇") and (x7[0] == "♧" or x7[0] == "♤")) or ((x1[0] == "♧" or x1[0] == "♤") and (x7[0] == "♡" or x7[0] == "◇"))) and (compare(x1[1:3],x7[1:3])):
                                    card[0].remove(x1)
                                    card[6].append(x1)
                                else :#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print()
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")              
                        else: #u == "8"#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[0].remove(x1)
                                card[7].append(x1)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x8 = card[7][len(card[7])-1]
                                if (((x1[0] == "♡" or x1[0] == "◇") and (x8[0] == "♧" or x8[0] == "♤")) or ((x1[0] == "♧" or x1[0] == "♤") and (x8[0] == "♡" or x8[0] == "◇"))) and (compare(x1[1:3],x8[1:3])):
                                    card[0].remove(x1)
                                    card[7].append(x1)
                                else :#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print()
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")
                    if t == "2":#"프리셀을 선택했을 때"
                        #프리셀에 첫칸이 비어있으면 카드를 넣고, 아닐 경우 바로 다음 칸에 카드를 넣는 형식; 한 칸에 한장밖에 못넣음.
                        if freecell[0] == []:
                            card[0].remove(x1)
                            freecell[0].append(x1)
                        elif freecell[1] == []:
                            card[0].remove(x1)
                            freecell[1].append(x1)
                        elif freecell[2] == []:
                            card[0].remove(x1)
                            freecell[2].append(x1)
                        elif freecell[3] == []:
                            card[0].remove(x1)
                            freecell[3].append(x1)
                        else :#4개의 프리셀에 카드가 다 들어가 있는 경우 카드를 더이상 받을 수 없다고 print하고 다시 2번째 while True로 돌아감.
                            print("freecell에 더이상 카드를 넣을 수 없습니다.")            
                    if t == "3":#"홈셀을 선택했을 때"
                        #같은 모양끼리만 넣을 수 있는데 카드를 그냥 홈셀에 넣으면 자동으로 분류되어서 들어감.
                        #홈셀이 비어있으면 "A"밖에 못넣음. A가 들어있으면 위에서 정의한 compare함수로 1큰 숫자들을 순차적으로 넣도록 설정함.
                        if x1[0] == "♡" and ((homecell[0] == [] and x1[1:3] == "A ") or (homecell[0] != [] and compare(homecell[0][len(homecell[0])-1][1:3],x1[1:3]))):
                            card[0].remove(x1)
                            homecell[0].append(x1)
                        elif x1[0] == "◇" and ((homecell[1] == [] and x1[1:3] == "A ") or (homecell[1] != [] and compare(homecell[1][len(homecell[1])-1][1:3],x1[1:3]))):
                            card[0].remove(x1)
                            homecell[1].append(x1)
                        elif x1[0] == "♧" and ((homecell[2] == [] and x1[1:3] == "A ") or (homecell[2] != [] and compare(homecell[2][len(homecell[2])-1][1:3],x1[1:3]))):
                            card[0].remove(x1)
                            homecell[2].append(x1)
                        elif x1[0] == "♤" and ((homecell[3] == [] and x1[1:3] == "A ") or (homecell[3] != [] and compare(homecell[3][len(homecell[3])-1][1:3],x1[1:3]))):
                            card[0].remove(x1)
                            homecell[3].append(x1)
                        else:
                            print("홈셀에 카드를 넣을 수 없습니다.(카드는 오름차순으로만 넣을 수 있습니다.)")
#아래 부터는 s == 2,3,4,5,6,7,8에 대하여 s == 1과 같은 조건을 반복!
                elif s == "2":#두번째 열의 카드를 선택했을 때.
                    x2 = card[1][len(card[1])-1]
                    t = input(x2 + "를 어디로 옮기시겠습니까?(1번 = 다른 열, 2번 = 프리셀, 3번 = 홈셀)")
                    while not (t == "1" or t == "2" or t == "3"):
                        print("다시 입력해주세요")#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                        t = input(x2 + "를 어디로 옮기시겠습니까?(1번 = 다른 열, 2번 = 프리셀, 3번 = 홈셀)")
                    if t == "1":
                        u = input(x2 + "를 어느 열로 옮기시겠습니까?(왼쪽부터 1~8)")
                        while not (u == "1" or u == "2" or u == "3" or u == "4" or u == "5" or u == "6" or u == "7" or u == "8"):
                            print("다시 입력해주세요")#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                            u = input(x2 + "를 어느 열로 옮기시겠습니까?(왼쪽부터 1~8)")
                        if u == "1":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[1].remove(x2)
                                card[0].append(x2)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x1 = card[0][len(card[0])-1]
                                if (((x2[0] == "♡" or x2[0] == "◇") and (x1[0] == "♧" or x1[0] == "♤")) or ((x2[0] == "♧" or x2[0] == "♤") and (x1[0] == "♡" or x1[0] == "◇"))) and (compare(x2[1:3],x1[1:3])):
                                    card[1].remove(x2)
                                    card[0].append(x2)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")                        
                        elif u == "2":
                            card[1].remove(x2)
                            card[1].append(x2)
                        elif u == "3":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[1].remove(x2)
                                card[2].append(x2)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x3 = card[2][len(card[2])-1]
                                if (((x2[0] == "♡" or x2[0] == "◇") and (x3[0] == "♧" or x3[0] == "♤")) or ((x2[0] == "♧" or x2[0] == "♤") and (x3[0] == "♡" or x3[0] == "◇"))) and (compare(x2[1:3],x3[1:3])):
                                    card[1].remove(x2)
                                    card[2].append(x2)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")                
                        elif u == "4":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[1].remove(x2)
                                card[3].append(x2)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x4 = card[3][len(card[3])-1]
                                if (((x2[0] == "♡" or x2[0] == "◇") and (x4[0] == "♧" or x4[0] == "♤")) or ((x2[0] == "♧" or x2[0] == "♤") and (x4[0] == "♡" or x4[0] == "◇"))) and (compare(x2[1:3],x4[1:3])):
                                    card[1].remove(x2)
                                    card[3].append(x2)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")               
                        elif u == "5":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[1].remove(x2)
                                card[4].append(x2)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x5 = card[4][len(card[4])-1]
                                if (((x2[0] == "♡" or x2[0] == "◇") and (x5[0] == "♧" or x5[0] == "♤")) or ((x2[0] == "♧" or x2[0] == "♤") and (x5[0] == "♡" or x5[0] == "◇"))) and (compare(x2[1:3],x5[1:3])):
                                    card[1].remove(x2)
                                    card[4].append(x2)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")                
                        elif u == "6":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[1].remove(x2)
                                card[5].append(x2)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x6 = card[5][len(card[5])-1]
                                if (((x2[0] == "♡" or x2[0] == "◇") and (x6[0] == "♧" or x6[0] == "♤")) or ((x2[0] == "♧" or x2[0] == "♤") and (x6[0] == "♡" or x6[0] == "◇"))) and (compare(x2[1:3],x6[1:3])):
                                    card[1].remove(x2)
                                    card[5].append(x2)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")         
                        elif u == "7":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[1].remove(x2)
                                card[6].append(x2)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x7 = card[6][len(card[6])-1]
                                if (((x2[0] == "♡" or x2[0] == "◇") and (x7[0] == "♧" or x7[0] == "♤")) or ((x2[0] == "♧" or x2[0] == "♤") and (x7[0] == "♡" or x7[0] == "◇"))) and (compare(x2[1:3],x7[1:3])):
                                    card[1].remove(x2)
                                    card[6].append(x2)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")              
                        else: #u == "8",어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[1].remove(x2)
                                card[7].append(x2)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x8 = card[7][len(card[7])-1]
                                if (((x2[0] == "♡" or x2[0] == "◇") and (x8[0] == "♧" or x8[0] == "♤")) or ((x2[0] == "♧" or x2[0] == "♤") and (x8[0] == "♡" or x8[0] == "◇"))) and (compare(x2[1:3],x8[1:3])):
                                    card[1].remove(x2)
                                    card[7].append(x2)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")
                    if t == "2":#"프리셀을 선택했을 때"
                        if freecell[0] == []:
                            card[1].remove(x2)
                            freecell[0].append(x2)
                        elif freecell[1] == []:
                            card[1].remove(x2)
                            freecell[1].append(x2)
                        elif freecell[2] == []:
                            card[1].remove(x2)
                            freecell[2].append(x2)
                        elif freecell[3] == []:
                            card[1].remove(x2)
                            freecell[3].append(x2)
                        else :#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                            print("freecell에 더이상 카드를 넣을 수 없습니다.")            
                    if t == "3":#"홈셀을 선택했을 때"
                        if x2[0] == "♡" and ((homecell[0] == [] and x2[1:3] == "A ") or (homecell[0] != [] and compare(homecell[0][len(homecell[0])-1][1:3],x2[1:3]))):
                            card[1].remove(x2)
                            homecell[0].append(x2)
                        elif x2[0] == "◇" and ((homecell[1] == [] and x2[1:3] == "A ") or (homecell[1] != [] and compare(homecell[1][len(homecell[1])-1][1:3],x2[1:3]))):
                            card[1].remove(x2)
                            homecell[1].append(x2)
                        elif x2[0] == "♧" and ((homecell[2] == [] and x2[1:3] == "A ") or (homecell[2] != [] and compare(homecell[2][len(homecell[2])-1][1:3],x2[1:3]))):
                            card[1].remove(x2)
                            homecell[2].append(x2)
                        elif x2[0] == "♤" and ((homecell[3] == [] and x2[1:3] == "A ") or (homecell[3] != [] and compare(homecell[3][len(homecell[3])-1][1:3],x2[1:3]))):
                            card[1].remove(x2)
                            homecell[3].append(x2)
                        else:#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                            print("홈셀에 카드를 넣을 수 없습니다.(카드는 오름차순으로만 넣을 수 있습니다.)")

                elif s == "3":#3번째 열의 카드를 선택했을 때.
                    x3 = card[2][len(card[2])-1]
                    t = input(x3 + "를 어디로 옮기시겠습니까?(1번 = 다른 열, 2번 = 프리셀, 3번 = 홈셀)")
                    while not (t == "1" or t == "2" or t == "3"):
                        print("다시 입력해주세요")#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                        t = input(x3 + "를 어디로 옮기시겠습니까?(1번 = 다른 열, 2번 = 프리셀, 3번 = 홈셀)")
                    if t == "1":
                        u = input(x3 + "를 어느 열로 옮기시겠습니까?(왼쪽부터 1~8)")
                        while not (u == "1" or u == "2" or u == "3" or u == "4" or u == "5" or u == "6" or u == "7" or u == "8"):
                            print("다시 입력해주세요")#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                            u = input(x3 + "를 어느 열로 옮기시겠습니까?(왼쪽부터 1~8)")
                        if u == "1":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[2].remove(x3)
                                card[0].append(x3)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x1 = card[0][len(card[0])-1]
                                if (((x3[0] == "♡" or x3[0] == "◇") and (x1[0] == "♧" or x1[0] == "♤")) or ((x3[0] == "♧" or x3[0] == "♤") and (x1[0] == "♡" or x1[0] == "◇"))) and (compare(x3[1:3],x1[1:3])):
                                    card[2].remove(x3)
                                    card[0].append(x3)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")                        
                        elif u == "2":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[2].remove(x3)
                                card[1].append(x3)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x2 = card[1][len(card[1])-1]
                                if (((x3[0] == "♡" or x3[0] == "◇") and (x2[0] == "♧" or x2[0] == "♤")) or ((x3[0] == "♧" or x3[0] == "♤") and (x2[0] == "♡" or x2[0] == "◇"))) and (compare(x3[1:3],x2[1:3])):
                                    card[2].remove(x3)
                                    card[1].append(x3)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")  
                        elif u == "3":
                            card[2].remove(x3)
                            card[2].append(x3)                
                        elif u == "4":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[2].remove(x3)
                                card[3].append(x3)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x4 = card[3][len(card[3])-1]
                                if (((x3[0] == "♡" or x3[0] == "◇") and (x4[0] == "♧" or x4[0] == "♤")) or ((x3[0] == "♧" or x3[0] == "♤") and (x4[0] == "♡" or x4[0] == "◇"))) and (compare(x3[1:3],x4[1:3])):
                                    card[2].remove(x3)
                                    card[3].append(x3)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")               
                        elif u == "5":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[2].remove(x3)
                                card[4].append(x3)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x5 = card[4][len(card[4])-1]
                                if (((x3[0] == "♡" or x3[0] == "◇") and (x5[0] == "♧" or x5[0] == "♤")) or ((x3[0] == "♧" or x3[0] == "♤") and (x5[0] == "♡" or x5[0] == "◇"))) and (compare(x3[1:3],x5[1:3])):
                                    card[2].remove(x3)
                                    card[4].append(x3)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")                
                        elif u == "6":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[2].remove(x3)
                                card[5].append(x3)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x6 = card[5][len(card[5])-1]
                                if (((x3[0] == "♡" or x3[0] == "◇") and (x6[0] == "♧" or x6[0] == "♤")) or ((x3[0] == "♧" or x3[0] == "♤") and (x6[0] == "♡" or x6[0] == "◇"))) and (compare(x3[1:3],x6[1:3])):
                                    card[2].remove(x3)
                                    card[5].append(x3)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")         
                        elif u == "7":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[2].remove(x3)
                                card[6].append(x3)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x7 = card[6][len(card[6])-1]
                                if (((x3[0] == "♡" or x3[0] == "◇") and (x7[0] == "♧" or x7[0] == "♤")) or ((x3[0] == "♧" or x3[0] == "♤") and (x7[0] == "♡" or x7[0] == "◇"))) and (compare(x3[1:3],x7[1:3])):
                                    card[2].remove(x3)
                                    card[6].append(x3)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")              
                        else: #u == "8",어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[2].remove(x3)
                                card[7].append(x3)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x8 = card[7][len(card[7])-1]
                                if (((x3[0] == "♡" or x3[0] == "◇") and (x8[0] == "♧" or x8[0] == "♤")) or ((x3[0] == "♧" or x3[0] == "♤") and (x8[0] == "♡" or x8[0] == "◇"))) and (compare(x3[1:3],x8[1:3])):
                                    card[2].remove(x3)
                                    card[7].append(x3)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")
                    if t == "2":#"프리셀을 선택했을 때"
                        if freecell[0] == []:
                            card[2].remove(x3)
                            freecell[0].append(x3)
                        elif freecell[1] == []:
                            card[2].remove(x3)
                            freecell[1].append(x3)
                        elif freecell[2] == []:
                            card[2].remove(x3)
                            freecell[2].append(x3)
                        elif freecell[3] == []:
                            card[2].remove(x3)
                            freecell[3].append(x3)
                        else :#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                            print("freecell에 더이상 카드를 넣을 수 없습니다.")            
                    if t == "3":#"홈셀을 선택했을 때"
                        if x3[0] == "♡" and ((homecell[0] == [] and x3[1:3] == "A ") or (homecell[0] != [] and compare(homecell[0][len(homecell[0])-1][1:3],x3[1:3]))):
                            card[2].remove(x3)
                            homecell[0].append(x3)
                        elif x3[0] == "◇" and ((homecell[1] == [] and x3[1:3] == "A ") or (homecell[1] != [] and compare(homecell[1][len(homecell[1])-1][1:3],x3[1:3]))):
                            card[2].remove(x3)
                            homecell[1].append(x3)
                        elif x3[0] == "♧" and ((homecell[2] == [] and x3[1:3] == "A ") or (homecell[2] != [] and compare(homecell[2][len(homecell[2])-1][1:3],x3[1:3]))):
                            card[2].remove(x3)
                            homecell[2].append(x3)
                        elif x3[0] == "♤" and ((homecell[3] == [] and x3[1:3] == "A ") or (homecell[3] != [] and compare(homecell[3][len(homecell[3])-1][1:3],x3[1:3]))):
                            card[2].remove(x3)
                            homecell[3].append(x3)
                        else:#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                            print("홈셀에 카드를 넣을 수 없습니다.(카드는 오름차순으로만 넣을 수 있습니다.)")
                elif s == "4":#4번째 열의 카드를 선택했을 때.
                    x4 = card[3][len(card[3])-1]
                    t = input(x4 + "를 어디로 옮기시겠습니까?(1번 = 다른 열, 2번 = 프리셀, 3번 = 홈셀)")
                    while not (t == "1" or t  == "2" or t == "3"):
                        print("다시 입력해주세요")#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                        t = input(x4 + "를 어디로 옮기시겠습니까?(1번 = 다른 열, 2번 = 프리셀, 3번 = 홈셀)")
                    if t == "1":
                        u = input(x4 + "를 어느 열로 옮기시겠습니까?(왼쪽부터 1~8)")
                        while not (u == "1" or u == "2" or u == "3" or u == "4" or u == "5" or u == "6" or u == "7" or u == "8"):
                            print("다시 입력해주세요")#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                            u = input(x4 + "를 어느 열로 옮기시겠습니까?(왼쪽부터 1~8)")
                        if u == "1":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[3].remove(x4)
                                card[0].append(x4)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x1 = card[0][len(card[0])-1]
                                if (((x4[0] == "♡" or x4[0] == "◇") and (x1[0] == "♧" or x1[0] == "♤")) or ((x4[0] == "♧" or x4[0] == "♤") and (x1[0] == "♡" or x1[0] == "◇"))) and (compare(x4[1:3],x1[1:3])):
                                    card[3].remove(x4)
                                    card[0].append(x4)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")                        
                        elif u == "2":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[3].remove(x4)
                                card[1].append(x4)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x2 = card[1][len(card[1])-1]
                                if (((x4[0] == "♡" or x4[0] == "◇") and (x2[0] == "♧" or x2[0] == "♤")) or ((x4[0] == "♧" or x4[0] == "♤") and (x2[0] == "♡" or x2[0] == "◇"))) and (compare(x4[1:3],x2[1:3])):
                                    card[3].remove(x4)
                                    card[1].append(x4)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")  
                        elif u == "3":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[3].remove(x4)
                                card[2].append(x4)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x3 = card[2][len(card[2])-1]
                                if (((x4[0] == "♡" or x4[0] == "◇") and (x3[0] == "♧" or x3[0] == "♤")) or ((x4[0] == "♧" or x4[0] == "♤") and (x3[0] == "♡" or x3[0] == "◇"))) and (compare(x4[1:3],x3[1:3])):
                                    card[3].remove(x4)
                                    card[2].append(x4)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")                 
                        elif u == "4":
                            card[3].remove(x4)
                            card[3].append(x4)
                        elif u == "5":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[3].remove(x4)
                                card[4].append(x4)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x5 = card[4][len(card[4])-1]
                                if (((x4[0] == "♡" or x4[0] == "◇") and (x5[0] == "♧" or x5[0] == "♤")) or ((x4[0] == "♧" or x4[0] == "♤") and (x5[0] == "♡" or x5[0] == "◇"))) and (compare(x4[1:3],x5[1:3])):
                                    card[3].remove(x4)
                                    card[4].append(x4)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")                
                        elif u == "6":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[3].remove(x4)
                                card[5].append(x4)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x6 = card[5][len(card[5])-1]
                                if (((x4[0] == "♡" or x4[0] == "◇") and (x6[0] == "♧" or x6[0] == "♤")) or ((x4[0] == "♧" or x4[0] == "♤") and (x6[0] == "♡" or x6[0] == "◇"))) and (compare(x4[1:3],x6[1:3])):
                                    card[3].remove(x4)
                                    card[5].append(x4)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")         
                        elif u == "7":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[3].remove(x4)
                                card[6].append(x4)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x7 = card[6][len(card[6])-1]
                                if (((x4[0] == "♡" or x4[0] == "◇") and (x7[0] == "♧" or x7[0] == "♤")) or ((x4[0] == "♧" or x4[0] == "♤") and (x7[0] == "♡" or x7[0] == "◇"))) and (compare(x4[1:3],x7[1:3])):
                                    card[3].remove(x4)
                                    card[6].append(x4)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")              
                        else: #u == "8",어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[3].remove(x4)
                                card[7].append(x4)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x8 = card[7][len(card[7])-1]
                                if (((x4[0] == "♡" or x4[0] == "◇") and (x8[0] == "♧" or x8[0] == "♤")) or ((x4[0] == "♧" or x4[0] == "♤") and (x8[0] == "♡" or x8[0] == "◇"))) and (compare(x4[1:3],x8[1:3])):
                                    card[3].remove(x4)
                                    card[7].append(x4)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")
                    if t == "2":#"프리셀을 선택했을 때"
                        if freecell[0] == []:
                            card[3].remove(x4)
                            freecell[0].append(x4)
                        elif freecell[1] == []:
                            card[3].remove(x4)
                            freecell[1].append(x4)
                        elif freecell[2] == []:
                            card[3].remove(x4)
                            freecell[2].append(x4)
                        elif freecell[3] == []:
                            card[3].remove(x4)
                            freecell[3].append(x4)
                        else :#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                            print("freecell에 더이상 카드를 넣을 수 없습니다.")            
                    if t == "3":#"홈셀을 선택했을 때"
                        if x4[0] == "♡" and ((homecell[0] == [] and x4[1:3] == "A ") or (homecell[0] != [] and compare(homecell[0][len(homecell[0])-1][1:3],x4[1:3]))):
                            card[3].remove(x4)
                            homecell[0].append(x4)
                        elif x4[0] == "◇" and ((homecell[1] == [] and x4[1:3] == "A ") or (homecell[1] != [] and compare(homecell[1][len(homecell[1])-1][1:3],x4[1:3]))):
                            card[3].remove(x4)
                            homecell[1].append(x4)
                        elif x4[0] == "♧" and ((homecell[2] == [] and x4[1:3] == "A ") or (homecell[2] != [] and compare(homecell[2][len(homecell[2])-1][1:3],x4[1:3]))):
                            card[3].remove(x4)
                            homecell[2].append(x4)
                        elif x4[0] == "♤" and ((homecell[3] == [] and x4[1:3] == "A ") or (homecell[3] != [] and compare(homecell[3][len(homecell[3])-1][1:3],x4[1:3]))):
                            card[3].remove(x4)
                            homecell[3].append(x4)
                        else:
                            print("홈셀에 카드를 넣을 수 없습니다.(카드는 오름차순으로만 넣을 수 있습니다.)")
                elif s == "5": #5번째 열의 카드를 선택했을 때.
                    x5 = card[4][len(card[4])-1]
                    t = input(x5 + "를 어디로 옮기시겠습니까?(1번 = 다른 열, 2번 = 프리셀, 3번 = 홈셀)")
                    while not (t == "1" or t == "2" or t == "3"):
                        print("다시 입력해주세요")#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                        t = input(x5 + "를 어디로 옮기시겠습니까?(1번 = 다른 열, 2번 = 프리셀, 3번 = 홈셀)")
                    if t == "1":
                        u = input(x5 + "를 어느 열로 옮기시겠습니까?(왼쪽부터 1~8)")
                        while not (u == "1" or u == "2" or u == "3" or u == "4" or u == "5" or u == "6" or u == "7" or u == "8"):
                            print("다시 입력해주세요")#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                            u = input(x5 + "를 어느 열로 옮기시겠습니까?(왼쪽부터 1~8)")
                        if u == "1":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[4].remove(x5)
                                card[0].append(x5)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x1 = card[0][len(card[0])-1]
                                if (((x5[0] == "♡" or x5[0] == "◇") and (x1[0] == "♧" or x1[0] == "♤")) or ((x5[0] == "♧" or x5[0] == "♤") and (x1[0] == "♡" or x1[0] == "◇"))) and (compare(x5[1:3],x1[1:3])):
                                    card[4].remove(x5)
                                    card[0].append(x5)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")                        
                        elif u == "2":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[4].remove(x5)
                                card[1].append(x5)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x2 = card[1][len(card[1])-1]
                                if (((x5[0] == "♡" or x5[0] == "◇") and (x2[0] == "♧" or x2[0] == "♤")) or ((x5[0] == "♧" or x5[0] == "♤") and (x2[0] == "♡" or x2[0] == "◇"))) and (compare(x5[1:3],x2[1:3])):
                                    card[4].remove(x5)
                                    card[1].append(x5)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")  
                        elif u == "3":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[4].remove(x5)
                                card[2].append(x5)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x3 = card[2][len(card[2])-1]
                                if (((x5[0] == "♡" or x5[0] == "◇") and (x3[0] == "♧" or x3[0] == "♤")) or ((x5[0] == "♧" or x5[0] == "♤") and (x3[0] == "♡" or x3[0] == "◇"))) and (compare(x5[1:3],x3[1:3])):
                                    card[4].remove(x5)
                                    card[2].append(x5)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")                 
                        elif u == "4":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[4].remove(x5)
                                card[3].append(x5)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x4 = card[3][len(card[3])-1]
                                if (((x5[0] == "♡" or x5[0] == "◇") and (x4[0] == "♧" or x4[0] == "♤")) or ((x5[0] == "♧" or x5[0] == "♤") and (x4[0] == "♡" or x4[0] == "◇"))) and (compare(x5[1:3],x4[1:3])):
                                    card[4].remove(x5)
                                    card[3].append(x5)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")   
                        elif u == "5":
                                card[4].remove(x5)
                                card[4].append(x5)            
                        elif u == "6":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[4].remove(x5)
                                card[5].append(x5)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x6 = card[5][len(card[5])-1]
                                if (((x5[0] == "♡" or x5[0] == "◇") and (x6[0] == "♧" or x6[0] == "♤")) or ((x5[0] == "♧" or x5[0] == "♤") and (x6[0] == "♡" or x6[0] == "◇"))) and (compare(x5[1:3],x6[1:3])):
                                    card[4].remove(x5)
                                    card[5].append(x5)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")         
                        elif u == "7":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[4].remove(x5)
                                card[6].append(x5)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x7 = card[6][len(card[6])-1]
                                if (((x5[0] == "♡" or x5[0] == "◇") and (x7[0] == "♧" or x7[0] == "♤")) or ((x5[0] == "♧" or x5[0] == "♤") and (x7[0] == "♡" or x7[0] == "◇"))) and (compare(x5[1:3],x7[1:3])):
                                    card[4].remove(x5)
                                    card[6].append(x5)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")              
                        else: #u == "8",어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[4].remove(x5)
                                card[7].append(x5)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x8 = card[7][len(card[7])-1]
                                if (((x5[0] == "♡" or x5[0] == "◇") and (x8[0] == "♧" or x8[0] == "♤")) or ((x5[0] == "♧" or x5[0] == "♤") and (x8[0] == "♡" or x8[0] == "◇"))) and (compare(x5[1:3],x8[1:3])):
                                    card[4].remove(x5)
                                    card[7].append(x5)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")
                    if t == "2":#"프리셀을 선택했을 때"
                        if freecell[0] == []:
                            card[4].remove(x5)
                            freecell[0].append(x5)
                        elif freecell[1] == []:
                            card[4].remove(x5)
                            freecell[1].append(x5)
                        elif freecell[2] == []:
                            card[4].remove(x5)
                            freecell[2].append(x5)
                        elif freecell[3] == []:
                            card[4].remove(x5)
                            freecell[3].append(x5)
                        else :#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                            print("freecell에 더이상 카드를 넣을 수 없습니다.")            
                    if t == "3":#"홈셀을 선택했을 때"
                        if x5[0] == "♡" and ((homecell[0] == [] and x5[1:3] == "A ") or (homecell[0] != [] and compare(homecell[0][len(homecell[0])-1][1:3],x5[1:3]))):
                            card[4].remove(x5)
                            homecell[0].append(x5)
                        elif x5[0] == "◇" and ((homecell[1] == [] and x5[1:3] == "A ") or (homecell[1] != [] and compare(homecell[1][len(homecell[1])-1][1:3],x5[1:3]))):
                            card[4].remove(x5)
                            homecell[1].append(x5)
                        elif x5[0] == "♧" and ((homecell[2] == [] and x5[1:3] == "A ") or (homecell[2] != [] and compare(homecell[2][len(homecell[2])-1][1:3],x5[1:3]))):
                            card[4].remove(x5)
                            homecell[2].append(x5)
                        elif x5[0] == "♤" and ((homecell[3] == [] and x5[1:3] == "A ") or (homecell[3] != [] and compare(homecell[3][len(homecell[3])-1][1:3],x5[1:3]))):
                            card[4].remove(x5)
                            homecell[3].append(x5)
                        else:#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                            print("홈셀에 카드를 넣을 수 없습니다.(카드는 오름차순으로만 넣을 수 있습니다.)")
                elif s == "6": #6번째 열의 카드를 선택했을 때.
                    x6 = card[5][len(card[5])-1]
                    t = input(x6 + "를 어디로 옮기시겠습니까?(1번 = 다른 열, 2번 = 프리셀, 3번 = 홈셀)")
                    while not (t == "1" or t == "2" or t == "3"):
                        print("다시 입력해주세요")#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                        t = input(x6 + "를 어디로 옮기시겠습니까?(1번 = 다른 열, 2번 = 프리셀, 3번 = 홈셀)")
                    if t == "1":
                        u = input(x6 + "를 어느 열로 옮기시겠습니까?(왼쪽부터 1~8)")
                        while not (u == "1" or u == "2" or u == "3" or u == "4" or u == "5" or u == "6" or u == "7" or u == "8"):
                            print("다시 입력해주세요")#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                            u = input(x6 + "를 어느 열로 옮기시겠습니까?(왼쪽부터 1~8)")
                        if u == "1":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[5].remove(x6)
                                card[0].append(x6)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x1 = card[0][len(card[0])-1]
                                if (((x6[0] == "♡" or x6[0] == "◇") and (x1[0] == "♧" or x1[0] == "♤")) or ((x6[0] == "♧" or x6[0] == "♤") and (x1[0] == "♡" or x1[0] == "◇"))) and (compare(x6[1:3],x1[1:3])):
                                    card[5].remove(x6)
                                    card[0].append(x6)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")                        
                        elif u == "2":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[5].remove(x6)
                                card[1].append(x6)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x2 = card[1][len(card[1])-1]
                                if (((x6[0] == "♡" or x6[0] == "◇") and (x2[0] == "♧" or x2[0] == "♤")) or ((x6[0] == "♧" or x6[0] == "♤") and (x2[0] == "♡" or x2[0] == "◇"))) and (compare(x6[1:3],x2[1:3])):
                                    card[5].remove(x6)
                                    card[1].append(x6)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")  
                        elif u == "3":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[5].remove(x6)
                                card[2].append(x6)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x3 = card[2][len(card[2])-1]
                                if (((x6[0] == "♡" or x6[0] == "◇") and (x3[0] == "♧" or x3[0] == "♤")) or ((x6[0] == "♧" or x6[0] == "♤") and (x3[0] == "♡" or x3[0] == "◇"))) and (compare(x6[1:3],x3[1:3])):
                                    card[5].remove(x6)
                                    card[2].append(x6)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")                 
                        elif u == "4":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[5].remove(x6)
                                card[3].append(x6)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x4 = card[3][len(card[3])-1]
                                if (((x6[0] == "♡" or x6[0] == "◇") and (x4[0] == "♧" or x4[0] == "♤")) or ((x6[0] == "♧" or x6[0] == "♤") and (x4[0] == "♡" or x4[0] == "◇"))) and (compare(x6[1:3],x4[1:3])):
                                    card[5].remove(x6)
                                    card[3].append(x6)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")   
                        elif u == "5":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[5].remove(x6)
                                card[4].append(x6)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x5 = card[4][len(card[4])-1]
                                if (((x6[0] == "♡" or x6[0] == "◇") and (x5[0] == "♧" or x5[0] == "♤")) or ((x6[0] == "♧" or x6[0] == "♤") and (x5[0] == "♡" or x5[0] == "◇"))) and (compare(x6[1:3],x5[1:3])):
                                    card[5].remove(x6)
                                    card[4].append(x6)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")       
                        elif u == "6":
                                card[5].remove(x6)
                                card[5].append(x6)
                        elif u == "7":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[5].remove(x6)
                                card[6].append(x6)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x7 = card[6][len(card[6])-1]
                                if (((x6[0] == "♡" or x6[0] == "◇") and (x7[0] == "♧" or x7[0] == "♤")) or ((x6[0] == "♧" or x6[0] == "♤") and (x7[0] == "♡" or x7[0] == "◇"))) and (compare(x6[1:3],x7[1:3])):
                                    card[5].remove(x6)
                                    card[6].append(x6)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")              
                        else: #u == "8",어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[5].remove(x6)
                                card[7].append(x6)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x8 = card[7][len(card[7])-1]
                                if (((x6[0] == "♡" or x6[0] == "◇") and (x8[0] == "♧" or x8[0] == "♤")) or ((x6[0] == "♧" or x6[0] == "♤") and (x8[0] == "♡" or x8[0] == "◇"))) and (compare(x6[1:3],x8[1:3])):
                                    card[5].remove(x6)
                                    card[7].append(x6)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")
                    if t == "2":#"프리셀을 선택했을 때"
                        if freecell[0] == []:
                            card[5].remove(x6)
                            freecell[0].append(x6)
                        elif freecell[1] == []:
                            card[5].remove(x6)
                            freecell[1].append(x6)
                        elif freecell[2] == []:
                            card[5].remove(x6)
                            freecell[2].append(x6)
                        elif freecell[3] == []:
                            card[5].remove(x6)
                            freecell[3].append(x6)
                        else :#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                            print("freecell에 더이상 카드를 넣을 수 없습니다.")            
                    if t == "3":#"홈셀을 선택했을 때"
                        if x6[0] == "♡" and ((homecell[0] == [] and x6[1:3] == "A ") or (homecell[0] != [] and compare(homecell[0][len(homecell[0])-1][1:3],x6[1:3]))):
                            card[5].remove(x6)
                            homecell[0].append(x6)
                        elif x6[0] == "◇" and ((homecell[1] == [] and x6[1:3] == "A ") or (homecell[1] != [] and compare(homecell[1][len(homecell[1])-1][1:3],x6[1:3]))):
                            card[5].remove(x6)
                            homecell[1].append(x6)
                        elif x6[0] == "♧" and ((homecell[2] == [] and x6[1:3] == "A ") or (homecell[2] != [] and compare(homecell[2][len(homecell[2])-1][1:3],x6[1:3]))):
                            card[5].remove(x6)
                            homecell[2].append(x6)
                        elif x6[0] == "♤" and ((homecell[3] == [] and x6[1:3] == "A ") or (homecell[3] != [] and compare(homecell[3][len(homecell[3])-1][1:3],x6[1:3]))):
                            card[5].remove(x6)
                            homecell[3].append(x6)
                        else:#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                            print("홈셀에 카드를 넣을 수 없습니다.(카드는 오름차순으로만 넣을 수 있습니다.)")
                elif s == "7": #7번째 열의 카드를 선택했을 때.
                    x7 = card[6][len(card[6])-1]
                    t = input(x7 + "를 어디로 옮기시겠습니까?(1번 = 다른 열, 2번 = 프리셀, 3번 = 홈셀)")
                    while not (t == "1" or t == "2" or t == "3"):
                        print("다시 입력해주세요")#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                        t = input(x7 + "를 어디로 옮기시겠습니까?(1번 = 다른 열, 2번 = 프리셀, 3번 = 홈셀)")
                    if t == "1":
                        u = input(x7 + "를 어느 열로 옮기시겠습니까?(왼쪽부터 1~8)")
                        while not (u == "1" or u == "2" or u == "3" or u == "4" or u == "5" or u == "6" or u == "7" or u == "8"):
                            print("다시 입력해주세요")#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                            u = input(x7 + "를 어느 열로 옮기시겠습니까?(왼쪽부터 1~8)")
                        if u == "1":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[6].remove(x7)
                                card[0].append(x7)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x1 = card[0][len(card[0])-1]
                                if (((x7[0] == "♡" or x7[0] == "◇") and (x1[0] == "♧" or x1[0] == "♤")) or ((x7[0] == "♧" or x7[0] == "♤") and (x1[0] == "♡" or x1[0] == "◇"))) and (compare(x7[1:3],x1[1:3])):
                                    card[6].remove(x7)
                                    card[0].append(x7)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")                        
                        elif u == "2":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[6].remove(x7)
                                card[1].append(x7)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x2 = card[1][len(card[1])-1]
                                if (((x7[0] == "♡" or x7[0] == "◇") and (x2[0] == "♧" or x2[0] == "♤")) or ((x7[0] == "♧" or x7[0] == "♤") and (x2[0] == "♡" or x2[0] == "◇"))) and (compare(x7[1:3],x2[1:3])):
                                    card[6].remove(x6)
                                    card[1].append(x6)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")  
                        elif u == "3":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[6].remove(x7)
                                card[2].append(x7)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x3 = card[2][len(card[2])-1]
                                if (((x7[0] == "♡" or x7[0] == "◇") and (x3[0] == "♧" or x3[0] == "♤")) or ((x7[0] == "♧" or x7[0] == "♤") and (x3[0] == "♡" or x3[0] == "◇"))) and (compare(x7[1:3],x3[1:3])):
                                    card[6].remove(x7)
                                    card[2].append(x7)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")                 
                        elif u == "4":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[6].remove(x7)
                                card[3].append(x7)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x4 = card[3][len(card[3])-1]
                                if (((x7[0] == "♡" or x7[0] == "◇") and (x4[0] == "♧" or x4[0] == "♤")) or ((x7[0] == "♧" or x7[0] == "♤") and (x4[0] == "♡" or x4[0] == "◇"))) and (compare(x7[1:3],x4[1:3])):
                                    card[6].remove(x7)
                                    card[3].append(x7)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")   
                        elif u == "5":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[6].remove(x7)
                                card[4].append(x7)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x5 = card[4][len(card[4])-1]
                                if (((x7[0] == "♡" or x7[0] == "◇") and (x5[0] == "♧" or x5[0] == "♤")) or ((x7[0] == "♧" or x7[0] == "♤") and (x5[0] == "♡" or x5[0] == "◇"))) and (compare(x7[1:3],x5[1:3])):
                                    card[6].remove(x7)
                                    card[4].append(x7)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")       
                        elif u == "6":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[6].remove(x7)
                                card[5].append(x7)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x6 = card[5][len(card[5])-1]
                                if (((x7[0] == "♡" or x7[0] == "◇") and (x6[0] == "♧" or x6[0] == "♤")) or ((x7[0] == "♧" or x7[0] == "♤") and (x6[0] == "♡" or x6[0] == "◇"))) and (compare(x7[1:3],x6[1:3])):
                                    card[6].remove(x7)
                                    card[5].append(x7)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")
                        elif u == "7":
                                card[6].remove(x7)
                                card[6].append(x7)              
                        else: #u == "8",어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[6].remove(x7)
                                card[7].append(x7)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x8 = card[7][len(card[7])-1]
                                if (((x7[0] == "♡" or x7[0] == "◇") and (x8[0] == "♧" or x8[0] == "♤")) or ((x7[0] == "♧" or x7[0] == "♤") and (x8[0] == "♡" or x8[0] == "◇"))) and (compare(x7[1:3],x8[1:3])):
                                    card[6].remove(x7)
                                    card[7].append(x7)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")
                    if t == "2":#"프리셀을 선택했을 때"
                        if freecell[0] == []:
                            card[6].remove(x7)
                            freecell[0].append(x7)
                        elif freecell[1] == []:
                            card[6].remove(x7)
                            freecell[1].append(x7)
                        elif freecell[2] == []:
                            card[6].remove(x7)
                            freecell[2].append(x7)
                        elif freecell[3] == []:
                            card[6].remove(x7)
                            freecell[3].append(x7)
                        else :#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                            print("freecell에 더이상 카드를 넣을 수 없습니다.")            
                    if t == "3":#"홈셀을 선택했을 때"
                        if x7[0] == "♡" and ((homecell[0] == [] and x7[1:3] == "A ") or (homecell[0] != [] and compare(homecell[0][len(homecell[0])-1][1:3],x7[1:3]))):
                            card[6].remove(x7)
                            homecell[0].append(x7)
                        elif x7[0] == "◇" and ((homecell[1] == [] and x7[1:3] == "A ") or (homecell[1] != [] and compare(homecell[1][len(homecell[1])-1][1:3],x7[1:3]))):
                            card[6].remove(x7)
                            homecell[1].append(x7)
                        elif x7[0] == "♧" and ((homecell[2] == [] and x7[1:3] == "A ") or (homecell[2] != [] and compare(homecell[2][len(homecell[2])-1][1:3],x7[1:3]))):
                            card[6].remove(x7)
                            homecell[2].append(x7)
                        elif x7[0] == "♤" and ((homecell[3] == [] and x7[1:3] == "A ") or (homecell[3] != [] and compare(homecell[3][len(homecell[3])-1][1:3],x7[1:3]))):
                            card[6].remove(x7)
                            homecell[3].append(x7)
                        else:#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                            print("홈셀에 카드를 넣을 수 없습니다.(카드는 오름차순으로만 넣을 수 있습니다.)")
                else:  #s == "8", 8번째 열의 카드를 선택했을 때.
                    x8 = card[7][len(card[7])-1]
                    t = input(x8 + "를 어디로 옮기시겠습니까?(1번 = 다른 열, 2번 = 프리셀, 3번 = 홈셀)")
                    while not (t == "1" or t == "2" or t == "3"):
                        print("다시 입력해주세요")#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                        t = input(x8 + "를 어디로 옮기시겠습니까?(1번 = 다른 열, 2번 = 프리셀, 3번 = 홈셀)")
                    if t == "1":
                        u = input(x8 + "를 어느 열로 옮기시겠습니까?(왼쪽부터 1~8)")
                        while not (u == "1" or u == "2" or u == "3" or u == "4" or u == "5" or u == "6" or u == "7" or u == "8"):
                            print("다시 입력해주세요")#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                            u = input(x8 + "를 어느 열로 옮기시겠습니까?(왼쪽부터 1~8)")
                        if u == "1":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[7].remove(x8)
                                card[0].append(x8)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x1 = card[0][len(card[0])-1]
                                if (((x8[0] == "♡" or x8[0] == "◇") and (x1[0] == "♧" or x1[0] == "♤")) or ((x8[0] == "♧" or x8[0] == "♤") and (x1[0] == "♡" or x1[0] == "◇"))) and (compare(x8[1:3],x1[1:3])):
                                    card[7].remove(x8)
                                    card[0].append(x8)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")                        
                        elif u == "2":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[7].remove(x8)
                                card[1].append(x8)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x2 = card[1][len(card[1])-1]
                                if (((x8[0] == "♡" or x8[0] == "◇") and (x2[0] == "♧" or x2[0] == "♤")) or ((x8[0] == "♧" or x8[0] == "♤") and (x2[0] == "♡" or x2[0] == "◇"))) and (compare(x8[1:3],x2[1:3])):
                                    card[7].remove(x8)
                                    card[1].append(x8)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")  
                        elif u == "3":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[7].remove(x8)
                                card[2].append(x8)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x3 = card[2][len(card[2])-1]
                                if (((x8[0] == "♡" or x8[0] == "◇") and (x3[0] == "♧" or x3[0] == "♤")) or ((x8[0] == "♧" or x8[0] == "♤") and (x3[0] == "♡" or x3[0] == "◇"))) and (compare(x8[1:3],x3[1:3])):
                                    card[7].remove(x8)
                                    card[2].append(x8)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")                 
                        elif u == "4":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[7].remove(x8)
                                card[3].append(x8)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x4 = card[3][len(card[3])-1]
                                if (((x8[0] == "♡" or x8[0] == "◇") and (x4[0] == "♧" or x4[0] == "♤")) or ((x8[0] == "♧" or x8[0] == "♤") and (x4[0] == "♡" or x4[0] == "◇"))) and (compare(x8[1:3],x4[1:3])):
                                    card[7].remove(x8)
                                    card[3].append(x8)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")   
                        elif u == "5":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[7].remove(x8)
                                card[4].append(x8)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x5 = card[4][len(card[4])-1]
                                if (((x8[0] == "♡" or x8[0] == "◇") and (x5[0] == "♧" or x5[0] == "♤")) or ((x8[0] == "♧" or x8[0] == "♤") and (x5[0] == "♡" or x5[0] == "◇"))) and (compare(x8[1:3],x5[1:3])):
                                    card[7].remove(x8)
                                    card[4].append(x8)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")       
                        elif u == "6":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[7].remove(x8)
                                card[5].append(x8)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x6 = card[5][len(card[5])-1]
                                if (((x8[0] == "♡" or x8[0] == "◇") and (x6[0] == "♧" or x6[0] == "♤")) or ((x8[0] == "♧" or x8[0] == "♤") and (x6[0] == "♡" or x6[0] == "◇"))) and (compare(x8[1:3],x6[1:3])):
                                    card[7].remove(x8)
                                    card[5].append(x8)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")
                        elif u == "7":#어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                            if card[int(u)-1] == []:
                                card[7].remove(x8)
                                card[6].append(x8)
                            else:#색이 다르고(♡,◇ = 빨강 ♤,♧ = 검정), 크기가 1작을 때의 조건
                                x7 = card[6][len(card[6])-1]
                                if (((x8[0] == "♡" or x8[0] == "◇") and (x7[0] == "♧" or x7[0] == "♤")) or ((x8[0] == "♧" or x8[0] == "♤") and (x7[0] == "♡" or x7[0] == "◇"))) and (compare(x8[1:3],x7[1:3])):
                                    card[7].remove(x8)
                                    card[6].append(x8)
                                else :
                                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                                    print("조건에 맞지 않습니다.(조건 : 카드의 색이 달라야함. 숫자가 1작은것만 붙일 수 있음.)")              
                        else: #u == "8",어떤 열에 카드가 아무것도 없으면 아무 조건없이 카드를 그 열에 넣을 수 있다.
                                card[7].remove(x8)
                                card[7].append(x8)
                    if t == "2":#"프리셀을 선택했을 때"
                        if freecell[0] == []:
                            card[7].remove(x8)
                            freecell[0].append(x8)
                        elif freecell[1] == []:
                            card[7].remove(x8)
                            freecell[1].append(x8)
                        elif freecell[2] == []:
                            card[7].remove(x8)
                            freecell[2].append(x8)
                        elif freecell[3] == []:
                            card[7].remove(x8)
                            freecell[3].append(x8)
                        else :#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                            print("freecell에 더이상 카드를 넣을 수 없습니다.")            
                    if t == "3":#"홈셀을 선택했을 때"
                        if x8[0] == "♡" and ((homecell[0] == [] and x8[1:3] == "A ") or (homecell[0] != [] and compare(homecell[0][len(homecell[0])-1][1:3],x8[1:3]))):
                            card[7].remove(x8)
                            homecell[0].append(x8)
                        elif x8[0] == "◇" and ((homecell[1] == [] and x8[1:3] == "A ") or (homecell[1] != [] and compare(homecell[1][len(homecell[1])-1][1:3],x8[1:3]))):
                            card[7].remove(x8)
                            homecell[1].append(x8)
                        elif x8[0] == "♧" and ((homecell[2] == [] and x8[1:3] == "A ") or (homecell[2] != [] and compare(homecell[2][len(homecell[2])-1][1:3],x8[1:3]))):
                            card[7].remove(x8)
                            homecell[2].append(x8)
                        elif x8[0] == "♤" and ((homecell[3] == [] and x8[1:3] == "A ") or (homecell[3] != [] and compare(homecell[3][len(homecell[3])-1][1:3],x8[1:3]))):
                            card[7].remove(x8)
                            homecell[3].append(x8)
                        else:#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                            print("홈셀에 카드를 넣을 수 없습니다.(카드는 오름차순으로만 넣을 수 있습니다.)")
            if r == "2":#프리셀에서 카드를 꺼냄.
                v = input("프리셀 몇번째 칸의 카드를 꺼내시겠습니까?(1~4)")#플레이어에게서 꺼낼 카드가 있는 칸의 번호를 받음.
                if not ((v == "1" and freecell[0] != []) or (v == "2" and freecell[1] != []) or (v == "3" and freecell[2] != []) or (v == "4" and freecell[3] != [])):
                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                    print("다시 입력해주세요")
                    continue
                w = input("선택한 카드를 어디로 옮기시겠습니까?(1열~8열)(숫자만 입력)")#카드를 붙이고자하는 열의 번호를 받음
                if not (w.isdigit() and (w == "1" or w == "2" or w == "3" or w == "4" or w == "5" or w == "6" or w == "7" or w == "8")):
                    print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                    print("다시 입력해주세요")
                else:#입력받은 w와 v 이용해서 카드를 프리셀에서 빼서 열에 넣어줌.
                    if card[int(w)-1] == []:#빈 리스트의 경우 조건없이 그냥 프리셀에서 카드를 넣어줌.
                        y = freecell[int(v)-1][0]
                        freecell[int(v)-1].remove(y)
                        card[int(w)-1].append(y)
                    else:#카드끼리 조건을 비교한 후, 조건에 맞으면 카드를 넣어준다.
                        x = card[int(w)-1][len(card[int(w)-1])-1]
                        y = freecell[int(v)-1][0]
                        if (((x[0] == "◇" or x[0] == "♡") and (y[0] == "♧" or y[0] == "♤")) or ((x[0] == "♧" or x[0] == "♤") and (y[0] == "♡" or y[0] == "◇")) and (compare(y[1:3],x[1:3]))):
                            freecell[int(v)-1].remove(y)
                            card[int(w)-1].append(y)
                        else:
                            print()#조건에 맞지 않는 경우 두번째 while True로 돌아가서 보드를 다시 보여주고 처음부터 다시 input을 받음
                            print("카드를 옮길 수 없습니다. 조건에 맞지 않습니다.(조건1 : 카드의 색이 달라야 합니다. 조건2 :옮길 카드가 붙일 카드보다 1작아야합니다.)")
        if not more("Play more? (y/n) "):#게임을 더 진행하지 않을경우 종료
            break
##########################################################################################################################################
freecell()
