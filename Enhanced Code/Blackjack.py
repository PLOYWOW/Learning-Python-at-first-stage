import random

class Player():
    #Data = Dealer,Player
    #Action = Keep Card, Calculate -> Check21
    d = []
    p = []

    def __init__(self):
        #print("Can run")
        pass

    def keep_card(self,dearler,player):
        print("Keep Card")
        if len(Player.d) <= 1:
            self.dd = dearler
        self.pp = player
        if len(Player.d) <= 1:
            Player.d.append(self.dd)
        Player.p.append(self.pp)
        #print(Player.d)
        #print(Player.p)
        #pass

class Card():
    #Data = ไพ่ -> Number
    #Action = -
    def __init__(self):
        #ไพ่ 13 ใบ
        self.c1 = 1 #1 #1
        self.c2 = 2 #2 #2
        self.c3 = 3 #3 #3
        self.c4 = 4 #4 #4
        self.c5 = 5 #5 #5
        self.c6 = 6 #6 #6
        self.c7 = 7 #7 #7
        self.c8 = 8 #8 #8
        self.c9 = 9 #9 #9
        self.cj = 10 #J #10
        self.ck = 10 #Q #11
        self.cq = 10 #K #12
        self.a1 = 1 #A #13
        self.a11 = 11 #A #13

class RandomCard(Card):
    #Data = มาจาก Card()
    #Action = Random Card, A = 1 or 11?
    def __init__(self):
        print("Random")
        pass

    def random_card(self):
        self.dealer = random.randint(1,13)
        self.player = random.randint(1,13)
        print("#Random Original: Dealer get ",self.dealer," Player get ",self.player)
        
        #Dealer
        if len(Player.d) <= 2:
            if self.dealer == 11: #Q
                self.dealer = 10
                #self.dealer = Card.ck
            else:
                if self.dealer == 12: #K
                    self.dealer = 10
                else:
                    if self.dealer == 13:
                        if Compare.sum_d <= 10:
                            self.dealer = 11
                        if Compare.sum_d > 10:
                            self.dealer = 1
        #Player
        if self.player == 11: #Q
            self.player = 10
            #self.dealer = Card.ck
        else:
            if self.player == 12: #K
                self.player = 10
            else:
                if self.player == 13:
                    if Compare.sum_p <= 10:
                        self.player = 11
                    if Compare.sum_p > 10:
                        self.player = 1
        
        print("#Random Final: Dealer get ",self.dealer," Player get ",self.player)
        add_card = Player()
        add_card.keep_card(self.dealer,self.player)
        #Player.calculate_sum()
        CalSum()

    #def __init__(self):
        #pass
    #def random_card(self, player1, player2):
        #Random

class CalSum():
    #Data = -
    #Action = Calculate number, Check = 21?, Check Dealer & Player < >?

    def __init__(self):
        print("Current ","Dealer: ",Player.d,"Player: ",Player.p)
        print("Cal Sum")
        self.sum_d = 0
        self.sum_p = 0
        for i in range(len(Player.d)):
            self.sum_d = self.sum_d + Player.d[i]
        print("Total of Dealer = ",self.sum_d)

        for j in range(len(Player.p)):
            self.sum_p = self.sum_p + Player.p[j]
        print("Total of Player = ",self.sum_p)
        #summd = self.sum_d
        #summp = self.sum_p
        #check_21 = Compare.check21(summd,summp)
        #Compare.check21(self.sum_d,self.sum_p)
        print("Compare21")
        if len(Player.p) >= 2:
            Check21(self.sum_d,self.sum_p)
        #pass

class Check21():
    def __init__(self,dealer21,player21):
        self.d21 = dealer21
        self.p21 = player21
        print("Check 21")
        if self.p21 == 21:
            print("Player = 21, Player wins")
        if self.p21 > 21:
            print("Player > 21, Player loses")
        if self.p21 < 21:
            print("Player < 21, Keep Going -> Make a decision")
            self.choose = input("Type 'D' to draw card or type 'C to compare card with dealer: ")
            if self.choose == "D":
                print("Draw Card")
                player_random = RandomCard()
                player_random.random_card()
            if self.choose == "C":
                print("Compare Card with dealer")
                Compare(self.d21,self.p21)

class Compare():
    def __init__(self,compare_dealer,compare_player):
        self.cp_d = compare_dealer
        self.cp_p = compare_player
        print("Dealer: ",self.cp_d)
        print("VS")
        print("Player: ",self.cp_p)
        if self.cp_p < self.cp_d:
            print("Player Loses")
        if self.cp_p > self.cp_d:
            print("Player Wins")
        if self.cp_p == self.cp_d:
            print("Player = Dealer, Can't find the winner")
        #print("Compareeeee")
        #pass



        # = 21 -> Win
        # > 21 -> Lose "Bust"
        # < 21 -> Keep Going 1)Draw Card 2)Not Draw Card -> wait to compare with dealer
    
    #def check():

Player()
random1 = RandomCard()
random1.random_card()
#print("First Card: Dealer get ",random1.dealer," Player get ",random1.player)
random2 = RandomCard()
random2.random_card()
#print("Second Card: Dealer get ",random2.dealer," Player get ",random2.player)
#ck21 = Check21(CalSum.sum_p)
#Check21(CalSum.sum_p)





    

