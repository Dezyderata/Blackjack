from pprint import pprint
from deck import Deck
from player import Player
from os import system, name

def clear():
    _ = system('clear')
def first_cards(person_cards, deck):
    person_sum = 0
    person_cards.append(deck.pick_a_card())
    person_sum += person_cards[0][2]
    person_cards.append(deck.pick_a_card())
    person_sum += person_cards[1][2]
    return person_sum

def print_card(card):
    '''
    function printing a card
    '''
    space = 0
    if len(card[1])%2 == 0: 
        spaces = int((9 - len(card[1]))/2) * " "
        print(" --------- ")
        print("|    {}    |".format(card[0]))
        print("|         |")
        print("|" + spaces + "{}".format(card[1]) + spaces + " |")
        print("|         |")
        print(" --------- ")
    else:
        spaces = int((9 - len(card[1]))/2) * " " 
        print(" --------- ")
        print("|    {}    |".format(card[0]))
        print("|         |")
        print("|" + spaces + "{}".format(card[1]) + spaces + "|")
        print("|         |")
        print(" --------- ")

def print_table(ans):
    print("Player cards: ")
    for card in player_cards:
        print_card(card)
    print("Dealer card: ")
    if ans:
        print_card(dealer_cards[0])
    else:
        for card in dealer_cards:
            print_card(card)

def check_for_win():
    if player_sum == 21:
        print("You win!")
        player.win(bet)
        return True
    elif player_sum > 21:
        print("You lost!")
        return True
    else:
        return False

ans = True
deck = Deck()
deck.shuffle_deck()
player = Player()

while ans:
    bet = 0
    player_cards = []
    dealer_cards = []
    player_sum = 0
    dealer_sum = 0
    bet = player.bet()

    player_sum = first_cards(player_cards, deck)
    dealer_sum = first_cards(dealer_cards, deck)
    print_table(True)
    print("bet: {}, and player balance: {}".format(bet, player.balance))

    value = 2
    while player.hit_or_stay():
        player_cards.append(deck.pick_a_card())
        player_sum += player_cards[value][2]
        clear()
        print_table(True)
        if check_for_win():
            break
        value += 1
    print_table(False)
    if player_sum < 21 and player_sum > dealer_sum:
        value = 2
        while dealer_sum < player_sum or dealer_sum < 21:
            dealer_cards.append(deck.pick_a_card())
            dealer_sum += dealer_cards[value][2]
            clear()
            print_table(False)
            if player_sum < dealer_sum and dealer_sum <= 21:
                print("Player lost")
                break
            elif dealer_sum > 21:
                print("Player win!")
                player.win(bet)
                break
            else:
                value += 1
    print_table(False)
    ans = player.play_again()
