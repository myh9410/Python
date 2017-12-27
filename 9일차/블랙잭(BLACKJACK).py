import random
################################################################################
def fresh_deck():
    suits = {"Spade", "Heart", "Diamond", "Club"}
    ranks = {"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"}
    deck = []
    for s in suits:
        c = 0
        for r in ranks:
            deck.append({"suit": s, "rank": r})
            c = c + 1
    random.shuffle(deck)
    return deck
################################################################################
def hit(deck):
    if deck == []:
        deck = fresh_deck()
    return deck[0],deck[1:]
################################################################################
def count_score(cards):
    score = 0
    Ace = 0
    for card in cards:
        c = card['rank']
        if c == "J" or c == "Q" or c == "K":
            score += 10
        elif c == "A":
            score += 11
            Ace += 1
        else:
            score += int(c)    
    while score > 21 and not Ace == 0:
        score -= 10
        Ace -= 1
    return score
################################################################################
def show_cards(cards,message):
    print(message)
    for card in cards:
        print("  ",card["suit"], card["rank"])
################################################################################
def more(message):
    answer = input(message)
    while not (answer == 'y' or answer == 'n'):
        answer = input(message)
    if answer == 'y':
        return True
    else:
        return False
################################################################################
def blackjack():
    chips = 0
    while True :
        print("----")
        print("Welcome to SMaSH Casino!")
        deck = fresh_deck()
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
        print("My cards are: ")
        print("  ", "****", "**")
        print("  ", dealer[1]["suit"], dealer[1]["rank"])
        show_cards(player, "Your cards are: ")
        score_player = count_score(player)
        score_dealer = count_score(dealer)
        if score_player == 21 :
            chips +=2
            print("BLACKJACK!!!  You won")
            print("Chips =" ,chips)
        else: #score_player != 21
            while score_player < 21 and more("hit?(y/n)"):
                card, deck = hit(deck)
                player.append(card)
                show_cards(player, "Your cards are: ")
                score_player = count_score(player)
                if score_player > 21:
                    chips -=1
                    print("You bust!  I won.")
                    print("Chips =" ,chips)
            while score_dealer <= 16:
                card, deck = hit(deck)
                dealer.append(card)
                score_dealer = count_score(dealer)
            if score_dealer > 21:
                show_cards(dealer, "My cards are: ")
                chips +=1
                print("I bust.  You won")
                print("Chips =" ,chips)
            elif score_dealer == 21:
                show_cards(dealer, "My cards are: ")
                chips -=1
                print("BLACKJACK!!!  I won")
                print("Chips =" ,chips)    
            elif score_player == score_dealer:
                show_cards(dealer, "My cards are: ")
                print("We draw.")
                print("Chips =" ,chips)
            elif score_player > score_dealer :
                show_cards(dealer, "My cards are: ")
                chips +=1
                print("You won")
                print("Chips =" ,chips)
            else:
                show_cards(dealer, "My cards are: ")
                chips -=1
                print("I won")
                print("Chips =" ,chips)
        if not more("more game?(y/n)"):
            print("GOODBYE")
            break
print(blackjack())
            
