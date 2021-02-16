# Backjack
import random


class Card(): 

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def showcard(self):
        print(f"{self.value} of {self.suit} ")

    def getValue(self):
        if self.value in ["J", "Q", "K"]:
            return 10
        else:
            return self.value

    def getSuit(self):
        return self.suit

class Deck(): 
    def __init__(self):
        suits = ["hearts", "spades", "clubs", "diamonds"]
        values = ["1","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = []
        for value in values:
            for suit in suits:
                self.cards.append(Card(value,suit))

    def shuffle(self):
        random.shuffle(self.cards)
        return self

    def drawTop(self):
        return self.cards.pop()

class Player():
    def __init__(self):
        self.hand = []
        self.numberOfCards = 0

    def addCard(self, card):
        self.hand.append(card)
        self.numberOfCards += 1
    
    def hit(self, deck):        
        self.addCard(deck.drawTop())
            
    def hold(self):
        pass

    def pointTotal(self):
        self.points1 = 0
        self.points2 = 0
        for i in range(self.numberOfCards):
            if (self.hand[i].getValue() == 1):
                self.points1 += 11
                self.points2 += 1
            else: 
                
                self.points1 += int(self.hand[i].getValue())
                self.points2 += int(self.hand[i].getValue())

        return min([self.points1, self.points2], key=lambda x:x-21)

    def showHand(self):
        for i in range(self.numberOfCards):
            self.hand[i].showcard()


deck = Deck()
deck.shuffle()
player = Player()
dealer = Player()

dealer.hit(deck)
#dealer.hand[0].showcard()
dealer.hit(deck)
player.hit(deck)
player.hit(deck)
print("Player's cards:")
player.showHand()
print("Dealer's up card:")
dealer.hand[0].showcard()

print(f" Player's Total points {player.pointTotal()}")

playerPoints = player.pointTotal()
count_hold = 0
while(not(playerPoints >= 21) and count_hold < 2):
    
    option = input("Would you like to hit(input 1) or hold(input other than 1)?")
    if(option == "1"):
        count_hold = 0
        player.hit(deck)
        print(f"Player received : {player.hand[player.numberOfCards-1].value} of {player.hand[player.numberOfCards-1].suit}") 
        playerPoints = player.pointTotal()
    else:
        player.hold()
        count_hold += 1
    if(dealer.pointTotal() < 17):
        dealer.hit(deck)
        print("Dealer did hit a card!")
    else:
        print("Dealer did hold!")
    if(dealer.pointTotal()>= 21):
        break

if(playerPoints > 21):
    if(dealer.pointTotal() > 21):
        print("Tie!")
    else:
        print("Dealer wins")
else:
    if(playerPoints == 21):
        if(dealer.pointTotal() > 21):
            print("Player Wins!")
        elif (dealer.pointTotal() == 21):
            print("Tie!")
        else:
            print("Player Wins!")
    else:
        if(dealer.pointTotal() > 21):
            print("Player Wins!")
        elif (dealer.pointTotal() == 21):
            print("Dealer Wins!")
        else:
            if(playerPoints > dealer.pointTotal()):
                print("Player Wins!")
            elif(playerPoints == dealer.pointTotal()):
                print("Tie!")
            else:
                print("Dealer Wins!")
    
print("Player's cards:")
player.showHand()
print(f" Player's Total points {player.pointTotal()}")
print("Dealer's cards:")
dealer.showHand()
print(f" Dealer's Total points {dealer.pointTotal()}")
