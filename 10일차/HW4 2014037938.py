#이름 : 문용호
#학번 : 2014037938
#반 : 목요일
#과제 : BLACKJACK(계속)
import random

def fresh_deck():
    suits = {"Spade", "Heart", "Diamond", "Club"}
    ranks = {"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"}
    deck = []
    for s in suits:
        for r in ranks:
            card = {"suit": s, "rank": r}
            deck.append(card)
    random.shuffle(deck)
    return deck
    
def hit(deck):
    if deck == []:
        deck = fresh_deck()
    return deck[0], deck[1:]

def show_cards(cards,message):
    print(message)
    for card in cards:
        print(" ", card["suit"], card["rank"])

def count_score(hand):
    score = 0
    number_of_ace = 0
    for card in hand:
        rank = card['rank']
        if rank == 'A':
            score += 11
            number_of_ace += 1
        elif rank in {'J', 'Q', 'K'}: 
            score += 10
        else: 
            score += rank
    while score > 21 and number_of_ace > 0:
        score -= 10
        number_of_ace -= 1
    return score

def more(message):
    answer = input(message)
    while not (answer == 'y' or answer == 'n'):
        answer = input(message)
    if answer == 'y':
        return True
    else:
        return False
#members.txt에 있는 사용자들을 불러오는 함수    
def load_members():
    file = open("members.txt","r")#읽기용으로 members.txt를 불러옴
    members = {}
    for line in file:#각 줄에 대해서 이름과 비밀번호 게임횟수,승리한 횟수, 칩의 갯수가 나타나도록 설정
        name, passwd, tries, wins, chips = line.strip('\n').split(',')
        members[name] = (passwd,int(tries),float(wins),int(chips))
    file.close()
    return members
#members.txt에 게임한 후 사용자들의 정보를 저장하도록 하는 함수
def store_members(members):
    file = open("members.txt","w")#쓰기용으로 members.txt를 불러옴
    names = members.keys()
    for name in names: #
        passwd, tries, wins, chips = members[name]
        line = name + ',' + passwd + ',' + \
               str(tries) + ',' + str(wins) + "," + str(chips) + "\n"
        file.write(line)
    file.close()
        
def login(members):
    username = input("Enter your name: (4letters max) ")
    while len(username) > 4:
        username = input("Enter your name: (4letters max) ")
    trypassword = input("Enter your password: ")
    if username in members.keys():#members의 키중에 username이 있음
        if trypassword == members[username][0]:
            print("you played ",int(members[username][1])," games and won ",int(members[username][2])," of them.")
            print("your all-time winning percentage is","{0:.2f}".format(divide(members[username][2],members[username][1])),"%")
            #승률계산하여 %로 보여주되 아래 divide함수 정의한 것에서  분모가 0인 오류를 방지
            if int(members[username][3]) >= 0:
                print("you have",int(members[username][3]),"chips")
            else:
                print("you owe",int(members[username][3]),"chips")
            return username, trypassword, members[username][1], members[username][2], members[username][3], members
        else:
            return login(members)
    else:
        members[username] = (trypassword,0,0,0)#username을 members 사전에 추가
        return username, trypassword,0,0,0, members
def divide(x,y): return x/y*100if y>0 else 0

def show_top5(members):
    print("----")
    sorted_members = sorted(members.items(),key=lambda x: x[1][3],reverse=True)
                     #칩의 갯수를 역순으로 정렬
    print("All-time Top 5 based on the number of chips earned")
    #sorted_members[:5]의 원소 차례대로 보여주 0이하는 무시
    if len(sorted_members) >= 5:#for문 이용해서 모든 사용자들에 대해서 chip의 갯수를 검사 후 그중 5명만 나타나도록 설정
        for i in range(5):#0~4
            if sorted_members[i][1][3] > 0:#칩 갯수가 0이상
                print(i+1, ".", sorted_members[i][0], " : ", sorted_members[i][1][3])
    else:#플레이어 수가 5명이 안될때는 그 인원수만 나타나도록 설정
        for i in range(len(sorted_members)):
            if sorted_members[i][1][3] > 0:
                print(i+1,".", sorted_members[i][0], " : ", sorted_members[i][1][3])
                
def blackjack():
    print("Welcome to SMaSH Casino!")
    username, trypassword, tries, wins, chips, members = login(load_members())
    deck = fresh_deck()
    chips = 0
    today_game = 0#처음에 오늘 게음 수를 0으로 설정해준 다음 게임 한판 할때마다 1씩 추가해줌
    today_win = 0 #처음에 오늘 승리 수를 0으로 설정해준 다음 게임에서 이길때마다 1씩 추가해줌
    while True:
        print("-----")
        dealer = []
        player = []
        card, deck = hit(deck)
        player.append(card)
        card, deck = hit(deck)
        dealer.append(card)
        card, deck = hit(deck)
        player.append(card)
        card, deck = hit(deck)
        dealer.append(card)        
        print("My cards are:")
        print(" ", "****", "**")
        print(" ", dealer[1]["suit"], dealer[1]["rank"])
        show_cards(player, "Your cards are:")
        score_player = count_score(player)
        score_dealer = count_score(dealer)
        if score_player == 21:
            print("Blackjack! You won.")
            today_win += 1
            chips += 2
            print("Chips =",chips)
        else:
            while score_player < 21 and more("Hit? (y/n) "):
                card, deck = hit(deck)
                player.append(card)
                score_player = count_score(player)
                print(" ", card["suit"], card["rank"])
            if score_player > 21:
                print("You bust! I won.")
                chips -= 1
                print("Chips = ",chips)
                today_game += 1
            else:
                while score_dealer <= 16:
                    card, deck = hit(deck)
                    dealer.append(card)
                    score_dealer = count_score(dealer)
                show_cards(dealer, "My cards are:")
                if score_dealer > 21:
                    print("I bust! You won.")
                    chips += 1
                    today_game += 1
                    today_win += 1
                elif score_dealer == score_player:
                    print("We draw.")
                    today_game += 1
                    today_win += 0.5
                elif score_dealer > score_player:
                    print("I won.")
                    chips -= 1
                    today_game += 1
                else:
                    print("You won.")
                    chips += 1
                    today_game += 1
                    today_win += 1
                print("Chips =",chips)
        if not more("Play more? (y/n) "):
            break
    tries += today_game#총 게임 횟수에 오늘 게임플레이 수를 추가
    wins += today_win#총 승리 수에 오늘 승리수를 추가
    members[username] = (trypassword,tries,wins,chips) # 플레이어의 정보에 바뀐 tries와 wins를 추가
    store_members(members)
    print("you played", today_game, "games and won ", today_win, "of them.")
    print("your winning percentage today is","{0:.2f}".format(divide(today_win,today_game)),"%")
    show_top5(members)
    print("Bye!")

blackjack()
