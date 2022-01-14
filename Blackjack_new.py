import random

class Card():
    #Shuffle Card
    def __init__(self):
        self.card = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]*4
        print("Before Shuffle: ",self.card)
        random.shuffle(self.card)
        print("After Shuffle: ",self.card)

class Player():
    #Keep Card & Show Card & Calculate sum of cards & เลือก "จั่วเพิ่ม" or "compare w/ dealer"
    Dealer_card = []
    Player_card = []
    def __init__(self):
        print(self.Dealer_card, self.Player_card)

    def show_card(self):
        print("Dealer: ",self.Dealer_card)
        print("Player: ",self.Player_card)

class Dealer(Player):
    def __init__(self):
        pass
    def current_card(self,shuffled_card):
        self.shuffled_card = shuffled_card
        #print("Yay!",self.shuffled_card)
        print("Yay!", self.shuffled_card)
        return "1"
#แจกไพ่ให้ Player
    def distribute(self):
        pass
        
#Check =21? >21? <21? 
    def compare21(self):
        pass

#Compare player's card with dealer's card
    def compare_dealer(self):
        pass

class Rule():
    def __init__(self):
        pass
    #Judge result
    def judgement(self):
        pass

C = Card()
distribute = Dealer()
#distribute.current_card(C.card)
print(distribute.current_card(C.card))

