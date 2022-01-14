import random

class Card:
    def __init__(self,number,suit):
        self.suit = suit
        self.number = number
        s = self.suit
        if s =="S":
            s="♠"
        elif s =="C":
            s="♣"
        elif s =="D":
            s="♦"
        elif s =="H":
            s="♥"
        self.whole_card = str(self.number)+s
    
class Deck:
    def __init__(self):
        self.deck = []
        suit=["C","D","H","S"]
        number=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        i=0
        while i < 4:
            o=0
            while o < 13:
                z=Card(number[o],suit[i])
                o=o+1
                self.deck.append(z)
            i=i+1

class Player:

    def __init__(self,player_name,type):
        self.hand = []
        self.card_drawn = 0
        self.turn_no = 0
        self.player_name = str(player_name)
        self.status = "in"
        self.type = str(type)

    def draw(self,deck_):
        # for 21 only (loop)
        if self.card_drawn < 5:
            z=deck_.deck
            y=random.randint(0,len(z)-1)
            x = deck_.deck[y]
            self.hand.append(x)
            deck_.deck.remove(x)
            self.card_drawn = self.card_drawn+1
        else:
            print("Cant draw more cards.")
            
    def show(self):
        output = []
        i=0
        while i < len(self.hand):
            s = self.hand[i].whole_card
            output.append(s)
            i=i+1
        print(self.player_name+"'s cards : "+str(output))
    
class Dealer(Player):
    def __init__(self,player_name,type):
        super().__init__(player_name,type)

    def show_some(self):
        ## fix to like player (but with hidden card)
        output=[]
        s=self.hand[0].whole_card
        output.append(s)
        output.append("XX")
        print(self.player_name+"'s cards : "+str(output))

class Blackjack:
    def __init__(self):
        self.player_list = []
        self.dealer_card_sum = 0
    def check_player(self,player):
        i=0
        s=0
        while i < len(player.hand):
            x = player.hand[i].number
            #print("x is "+str(x))
            if x == "K":
                x=10
            elif x == "J":
                x=10
            elif x == "Q":
                x=10
            elif x == "A":
                o=0
                while o==0:
                    y = input("Your ace card's value (1 or 11) : ")
                    if y == "1":
                        x=1
                        o=1
                    elif y == "11":
                        x=11
                        o=1
                    else:
                        print("please re-enter the value (1 or 11 only) !")
            else:
                x=int(player.hand[i].number)
            s=s+x
            i=i+1
        if s == 21:
            #print(str(player.player_name)+" won. :3\n")
            #player.status = "out"
            return("21")
        elif s > 21:
            #print(str(player.player_name)+" lost. T^T\n")
            #player.status = "out"      
            return("bust") 
        else:
            return(int(s))          
    def turn(self,player,deck,dealer):
        ### dont forget to  +1 player's turn no
        if player.status == "in":
            if player.type == "player":
                if player.turn_no == 0:
                    ### turn 0
                    #print("test in turn 0 player")
                    player.draw(deck)
                    player.draw(deck)
                    player.turn_no=player.turn_no+1
                elif player.turn_no == 1:
                    ### turn 1
                    print("===o===o===o===o===")
                    print(str(player.player_name)+"'s turn.")
                    dealer.show_some()
                    player.show()
                    o=0
                    while o==0:
                        choice = input(str(player.player_name)+" please choose [H]it [S]tay : ")
                        if choice == "H" : 
                            player.draw(deck)
                            player.show()
                        elif choice == "S" :
                            o=1
                        ### Easter Egg
                        elif choice == "E" :
                            print("Hello im an easter egg UwU")
                        else :
                            print("please choose H or S only !")
                    s = self.check_player(player)
                    print(s)
                    if s == "21":
                        print(str(player.player_name)+" won. :3\n")
                        player.status = "out"
                    elif s == "bust":
                        print(str(player.player_name)+" lost. T^T\n")
                        player.status = "out"   
                    else:
                        print("")
                    player.turn_no=player.turn_no+1
                else:
                    ### turn 2
                    print("===o===o===o===o===")
                    print("checking"+str(player.player_name))
                    a = self.check_player(player)
                    z = self.dealer_card_sum
                    if a == "21":
                        print(str(player.player_name)+" won. :3\n")
                        player.status = "out"
                    elif a == "bust":
                        print(str(player.player_name)+" lost. T^T\n")
                        player.status = "out"   
                    else:
                        if int(a) > z: 
                            print(str(player.player_name)+"won!\n")
                            player.status = "out"
                        else:
                            print(str(player.player_name)+"lost!\n")
                            player.status = "out"      
            else:
                if player.turn_no == 0:
                    ### turn 0
                    #print("test in turn 0 dealer")
                    player.draw(deck)
                    player.draw(deck)
                    player.turn_no=player.turn_no+1
                elif player.turn_no == 1:
                    ### turn 1
                    #print("test in turn 1 dealer")
                    print("===o===o===o===o===")
                    print("dealer's turn.")
                    dealer.show()
                    print("")
                    y=self.check_player(dealer)
                    if y=="bust":
                        print("all remaining players win! :3")
                        exit()
                    elif y=="21":
                        print("all remaining players loose! T^T")
                        exit()
                    else:
                        y=self.dealer_card_sum
                    player.turn_no=player.turn_no+1
                else:
                    pass

game = Blackjack()

print("╒═════ Blackjack ═════╕\n")
o=0
while o==0:
    player_no=int(input("Amount of players : "))
    if player_no <= 1:
        print("Too few players, please re-enter number.")
    elif player_no > 10:
        print("Too many players, please re-enter number.")
    else:
        o=1
        #print(player_no)
        print("")

i=0
while i < player_no-1:
    #print(i)
    x="Player"+str(i+1)
    x= Player(x,"player")
    game.player_list.append(x)
    i=i+1

#print(game.player_list)

deck = Deck()
dealer = Dealer("dealer","dealer")
game.player_list.append(dealer)

#print(game.player_list)

i=0
while i < 3:
    o=0
    while o < player_no:
        #print(o)
        #print(game.player_list[o].player_name)
        game.turn(game.player_list[o],deck,dealer)
        o=o+1
    i=i+1
