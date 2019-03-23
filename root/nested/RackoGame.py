'''
Created on May 4, 2018

@author: Amanda Noriega

Racko game.  Get cards in order.

'''

import random
from random import shuffle
from warnings import catch_warnings

class Racko(object):
    cards = 0
    playerUser = list(range(1,11))
    playerComputer = list(range(1,11))
    cardCounter = 0
    faceUpCard = 0
    NUM_USER_CARDS = 10
    NUM_TOTAL_CARDS = 60


    def __init__(self, name):
        print('Welcome, ', name, "!")
        
        Racko.cards = list(range(1, (Racko.NUM_TOTAL_CARDS+1)));
        print('All Cards are')
        print(Racko.cards)

        
    def playGame(self):
        Racko.shuffleCards(self)
        Racko.dealCards(self)
              
        end = False
        while end == False:

            #User's turn
            print('\nYour turn...')
            if Racko.userTurn(self):
                break
                
            #Check for win    
            if Racko.checkForWinner(self):
                break
            
            #Computer's Turn
            print('\nComputer\'s Turn...')
            if Racko.computerTurn(self):
                break
            
            #Check for win    
            if Racko.checkForWinner(self):
                break
        
    
    def dealCards(self):
        i = 0
        j = 0
        while i<Racko.NUM_USER_CARDS:
            Racko.playerUser[i] = Racko.cards[j]
            Racko.playerComputer[i] = Racko.cards[j+1]
            i = i+1
            j = j+2
        
        Racko.cardCounter = 2*Racko.NUM_USER_CARDS+1
        Racko.faceUpCard = Racko.cards[2*Racko.NUM_USER_CARDS]  
          
        print("Users's cars are ", Racko.playerUser) 
        print("Computers's cars are ", Racko.playerComputer) 
            
        
    def shuffleCards(self):
        random.shuffle(Racko.cards)
        print('Shuffled Cards are now')
        print(Racko.cards)
        
    def printCards(self):
        print('Your cards are:')
        print(Racko.playerUser)
        
    def userTurn(self):
        selectedCard = 0
        Racko.printCards(self)
        print('Card face up: ', Racko.faceUpCard)
        
        while True:
            userInput = input('Press 1 for card and 2 for deck: ')
            
            if userInput == 'quit':
                print('Game Over.')
                return True
            try:
                value = int(userInput)
                if value == 1:
                    print(Racko.faceUpCard, ' selected.')
                    selectedCard = Racko.faceUpCard
                    break
                elif value == 2:
                    print('Deck card selected: ', Racko.cards[Racko.cardCounter])
                    selectedCard = Racko.cards[Racko.cardCounter]
                    Racko.cardCounter = Racko.cardCounter + 1
                    break
                else:
                    print('Invalid answer.')
            except ValueError:
                print('I do not understand.')
        
        Racko.printCards(self)
        print('Your card is ', selectedCard)
        
        while True:
            userInput = input('Where would you like to put the card? (0 for discard)')
            
            if userInput == 'quit':
                print('Game Over.')
                return True
            try:
                value = int(userInput)
                if value == 0:
                    Racko.faceUpCard = selectedCard
                    print('Discarded.')
                    break
                elif value > Racko.NUM_USER_CARDS or value < 0:
                    print('Invalid number.')
                else:
                    Racko.faceUpCard = Racko.playerUser[value-1]
                    Racko.playerUser[value-1] = selectedCard
                    break
            except ValueError:
                print('I do not understand.')
        
        Racko.printCards(self)
        
        return False    
    
    
    def computerCardDecision(self, card):
        #split into 5 sections
        #see what face card is and what section it belongs
        #if section already has items belonging to that section and in order pick from deck
        #if it doesn't pick face up card
        #see what section card belongs
        #if section already has items belonging to that section and in order discard
        #if it doesn't put in section in order
 
        print('Card face up: ', card)
        
        section = int(((card - 1) / Racko.NUM_TOTAL_CARDS)*(Racko.NUM_USER_CARDS/2))
        print('Section is '+str(section))
        
        print(Racko.playerComputer)
        print('cards in that section are ', Racko.playerComputer[section*2],' and ', Racko.playerComputer[section*2+1])
        
        if Racko.isCardInCorrectSection(self, Racko.playerComputer[section*2], section) and Racko.isCardInCorrectSection(self, Racko.playerComputer[section*2+1], section):
            print('Cards are in correct section - are they in correct order?')
            if Racko.playerComputer[section*2] > Racko.playerComputer[section*2+1]:
                print('they are out of order')
                #They are out of order
                if card < Racko.playerComputer[section*2+1]:    #replace 1 with facecard
                    temp = Racko.playerComputer[section*2]
                    Racko.playerComputer[section*2] = card
                    card = temp
                    print('swapped 1st')
                elif card > Racko.playerComputer[section*2]:    #replace 2 with facecard
                    temp = Racko.playerComputer[section*2+1]
                    Racko.playerComputer[section*2+1] = card
                    card = temp
                    print('swapped 2nd')
                else:
                    print('this card cannot help - continue')
            else:
                print('they are in order - continue')
                
        else:
            print('at least one current card is not in correct section')
            if ((not Racko.isCardInCorrectSection(self, Racko.playerComputer[section*2], section)) and
                    (not Racko.isCardInCorrectSection(self, Racko.playerComputer[section*2+1], section))):
                #both are in wrong section
                print('both cards are in wrong section')
                position = int((card - (Racko.NUM_TOTAL_CARDS/(Racko.NUM_USER_CARDS/2))*section -1)/(Racko.NUM_TOTAL_CARDS/Racko.NUM_USER_CARDS))
                print('replace position '+str(position))
                temp = Racko.playerComputer[section*2+position]
                Racko.playerComputer[section*2+position] = card
                card = temp
            elif ((not Racko.isCardInCorrectSection(self, Racko.playerComputer[section*2], section)) and
                    (card < Racko.playerComputer[section*2+1])):
                print('replace first one')
                temp = Racko.playerComputer[section*2]
                Racko.playerComputer[section*2] = card
                card = temp
            elif card > Racko.playerComputer[section*2]:
                print('replace second one')
                temp = Racko.playerComputer[section*2+1]
                Racko.playerComputer[section*2+1] = card
                card = temp      
            else:
                print('this card does not help - continue')    
                
        return card
    
    
    def computerTurn(self):
        cardStart = Racko.faceUpCard
        outputCard = Racko.computerCardDecision(self, Racko.faceUpCard)
        if cardStart == outputCard:
            #Computer must want to pull from deck
            print('Deck card selected: ', Racko.cards[Racko.cardCounter])
            selectedCard = Racko.cards[Racko.cardCounter]
            Racko.cardCounter = Racko.cardCounter + 1
            Racko.faceUpCard = Racko.computerCardDecision(self, selectedCard)
        else:
            #Computer used the faceup card, so we have a new faceup card, turn is over
            Racko.faceUpCard = outputCard;   
                    
        print('Computer')
        print(Racko.playerComputer)
        
        return False
        
    
    def checkForWinner(self):
        if Racko.areCardsInOrder(self, Racko.playerUser):
            print('Congrats - you win!')
            return True
        if Racko.areCardsInOrder(self, Racko.playerComputer):
            print('Sorry, computer won.')
            return True
        
        return False
        
        
    def areCardsInOrder(self, hand):
        for i in range(0, len(hand)-2):
            #print('Comparing ',hand[i],' and ',hand[i+1])
            if hand[i] > hand[i+1]:
                return False
            
        return True    
           
    def isCardInCorrectSection(self, card, section): 
        if (int(((card - 1) / Racko.NUM_TOTAL_CARDS)*(Racko.NUM_USER_CARDS/2))) == section:
            return True
        else:
            return False
        
        