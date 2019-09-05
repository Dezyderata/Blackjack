from pprint import pprint
class Player():
    def __init__(self):
        '''
        Player creation with default account balance
        '''
        self.balance = 100
    def bet(self):
        '''
        Player has the ability to determine the amount of the bet. Bet should be an integer
        '''
        while True:
            try:
                bet = int(input("How much do you want to bet? "))
            except ValueError:
                print("It wasn't correct value! Please try again!")
                continue
            if bet > self.balance:
                print("You don't have enough money! Your actual account balance: {}".format(self.balance))
                continue
            else:
                self.balance -= bet
                return bet

    def win(self, win):
        '''
        Set correct account balance after wining
        '''
        self.balance += win

    def decision(self):
        '''
        Player has the ability to take additional card or to stay.
        Correct answers are yes or no. Font size is irrelevant.
        '''
        while True:
            ans = input("Do you want to Hit(yes) or Stay(no)?")
            if ans.lower() == 'yes':
                return True
            elif ans.lower() == 'no':
                return False
            else:
                print("I didn't get your decision! Please try again!")
