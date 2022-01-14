import random

class Deck:
    def __init__(self):
        self.deck = []
        color=["C","D","H","S"]
        number=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        i=0
        while i < 4:
            o=0
            while o < 13:
                z=list([number[o],color[i]])
                o=o+1
                self.deck.append(z)
            i=i+1

class Player:

    def __init__(self,player_name):
        self.hand = []
        self.card_drawn = 0
        self.player_name = player_name

    def draw(self,deck_):
        if self.card_drawn < 5:
            z=deck_.deck
            y=random.randint(0,len(z)-1)
            x = deck_.deck[y]
            self.hand.append(x)
            deck_.deck.remove(x)
            self.card_drawn = self.card_drawn+1
        else:
            print("Cant draw more cards.")
        
    def check(self):
        i=0
        s=0
        while i < len(self.hand):
            x = self.hand[i][0]
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
                x=int(self.hand[i][0])
            s=s+x
            i=i+1
        if s == 21:
            return("21")
        elif s > 21:
            return("bust")
        else:
            return(str(s))
            
    def show(self):
        output = []
        i=0
        while i < len(self.hand):
            z=self.hand[i][1]
            if z =="S":
                z="♠"
            elif z =="C":
                z="♣"
            elif z =="D":
                z="♦"
            elif z =="H":
                z="♥"
            s=self.hand[i][0]+z
            output.append(s)
            i=i+1
        print(self.player_name+"'s cards : "+str(output))
    
    def turn(self,num):
        pass

class Dealer(Player):
    def __init__(self,player_name):
        super().__init__(player_name)

    def show_some(self):
        output=[]
        z=self.hand[0][1]
        if z =="S":
            z="♠"
        elif z =="C":
            z="♣"
        elif z =="D":
            z="♦"
        elif z =="H":
            z="♥"
        s=self.hand[0][0]+z
        output.append(s)
        output.append("XX")
        print(self.player_name+"'s cards : "+str(output))

class Game():
    def __init__(self):
        pass
    def play(self):
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
        print("")
        self.player_list=[]
        deck = Deck()
        player_no = int(player_no)
        i=0
        while i < player_no-1:
            X="Player"+str(i)
            x=Player("player "+str(i+1))
            self.player_list.append(x)
            i=i+1
        dealer = Dealer("dealer")
        self.player_list.append(dealer)
        i=0
        while i < len(self.player_list):
            self.player_list[i].draw(deck)
            self.player_list[i].draw(deck)
            i=i+1

        x = 0
        while x < len(self.player_list)-1 :
            print(str(self.player_list[x].player_name)+"'s turn.")
            self.player_list[len(self.player_list)-1].show_some()
            self.player_list[x].show()
            o=0
            while o==0:
                choice = input(str(self.player_list[x].player_name)+" please choose [H]it [S]tay : ")
                if choice == "H" : 
                    self.player_list[x].draw(deck)
                    self.player_list[x].show()
                elif choice == "S" :
                    y=self.player_list[x].check()
                    print(y)
                    if y=="bust":
                        print(str(self.player_list[x].player_name)+" is out.\n")
                        self.player_list.remove(self.player_list[x])
                        x=x-1
                    elif y=="21":
                        print(str(self.player_list[x].player_name)+" won. :3\n")
                        self.player_list.remove(self.player_list[x])
                        x=x-1
                        
                    print("next player.\n")
                    o=1
                else :
                    print("please choose H or S only !")
            x=x+1

        print("dealer's turn.\n")
        dealer.show()
        y=dealer.check()
        if y=="bust":
            print("all remaining players win! :3")
        elif y=="21":
            print("all remaining players loose! T^T")
        else:
            y=int(y)
            if y>17:
                z=int(y)
            else:
                dealer.draw(deck)
                dealer.show()
                y=dealer.check()
                if y=="bust":
                    print("all remaining players win! :3")
                    exit()
                elif y=="21":
                    print("all remaining players loose! T^T")
                else:
                    z=int(y)
            self.player_list.remove(dealer)
            i=0
            while i < len(self.player_list):
                print("checking"+str(self.player_list[i].player_name))
                a=int(self.player_list[i].check())
                if a=="bust":
                    print("bust")
                else:
                    if a > z: 
                        print(str(self.player_list[i].player_name)+"won!")
                    else:
                        print(str(self.player_list[i].player_name)+"lost!")
                    i=i+1

blackjack = Game()
blackjack.play()
