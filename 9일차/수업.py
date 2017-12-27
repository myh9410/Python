cash = {'50000' : 2, '10000' : 7, '5000' : 0, '1000' : 3}
#사전 사용법 >>>  {<키> : <표현식>}(중괄호로 둘러싸고 쉼표로 구분)
#10000원짜리 보고싶으면 -- cash['10000']
#cash["10000"] -=1             >>> 10000원짜리 한장 뺄 수 있음
#cash["100000"]                >>> 없는거 입력하면 에러
#'2000' in cash                >>> False
#del cash["1000"]              >>> cash내에서 1000원짜리 다 지워짐(없는거 지우려하면 에러)
#del >>> cash내 쌍을 지움

#for c in cash: print(c)       >>> 돈의 종료이 세로줄로 나열됨
#for c in cash: print(cash[c]) >>> 돈의 갯수 세로줄로 나열됨

#요구사항
#에이스 - 11로카운트하다가 21이 넘으면 1로 카운트하도록 설정
#참여자가 bust로 진경우를 제외하고는 딜러의 카드를 다 보여준다.
#칩의 갯수 : 0에서 시작 이기면+1 지면-1 블랙잭+2
#매라운드마다 칩의 갯수 보여줌
#카드게임할때 필요한 함수들 미리 정의해두면 편함.

#fresh_deck() - 새로운 카드 1벌을 섞어서 내줌.
#52장의 카드 - 리스트로 표현
#for s in suit:
#    for r in rank:

#hit(deck)
#맨 처음부터 뽑아주도록함 - deck[0],deck[1:]
def hit(deck):
    if deck == []:
        deck = fresh_deck()
    return deck[0],deck[1:]


#count_score(cards) - 카드의 인수들을 받아 합해서 점수를 내어줌.
def count_score(cards):
    score = 0
    for card in cards:
        #card 값을 평가하여 score에 더함(A = 11)
    #score가 21이 넘고 A가 있으면 score를 재조정(10점 빼줌)(10점 빼고 나서 A또있으면 또 빼줌)
    return score


#show_cards(cards,message)
def show_Cards(cards,message):
    print(message)
    for card in cards:
        print("  ", card["suit"], card["rank"])


#more(message)
def more(message):
    answer = input(message)
    while not (answer == 'y' or answer == 'n'):
        answer = input(message)
    if answer == 'y':
        return True
    else:
        return False

