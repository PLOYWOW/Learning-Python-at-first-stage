class One_room:
    def __init__(self): #ask for room number
        self.room_number = input("Your room number : ")
        self.number_of_people = int(input(f"Number of people in room {self.room_number} : "))
        self.people_list = []
        self.p_name = []
        self.pay_list=[]
        self.pay_list.clear()
        self.p_name.clear()
        self.people_list.clear()
        
    def asking(self): #ask people to fill the informations
        for i in range(self.number_of_people): 
            self.people = input("What is your name : ")
            self.day = int(input(f"Day that {self.people} lives in room {self.room_number} : "))
            self.people_list.append([self.people_list,self.day])
            self.p_name.append(self.people)

    def paying(self):
        for i in range(self.number_of_people):
            self.you_pay = int(input(f"Enter amount of your money {self.p_name[i]} : "))
            self.pay_list.append(self.you_pay)

class Price:
    def __init__(self): #ask for price
        self.price = int(input("Total Price : "))
    
    def get_day_and_resident(self,people): #get day data and resident name
        self.d = []
        self.d.clear()
        self.num_peo=people.number_of_people
        self.pd = 0
        self.pay_each=[]
        self.pay_each.clear()
        for i in range(self.num_peo):
            self.day_i = people.people_list[i][1]
            self.d.append(self.day_i)
            self.pd += self.day_i
        
    def calcu_price(self,people): #calculate price and output
        self.one_ratio = self.price/self.pd
        for j in range(len(self.d)):
            self.pay = self.d[j] * self.one_ratio
            self.round_pay = round(self.pay,2)
            self.pay_each.append(self.round_pay)
            self.r_name = people.p_name[j]
            print(f"{self.r_name} must pay {self.round_pay} for room {people.room_number}")
    
    def changes(self,people): #return changes
        for i in range(len(self.d)):
            self.you_ = people.pay_list[i]
            self.r_name=people.p_name[i]
            if self.you_<self.pay:
                self.change = self.pay-self.you_
                print(f"{self.r_name} must add more {self.change} money")
            elif self.you_>self.pay:
                self.change = self.you_-self.pay
                print(f"{self.r_name} will receive {self.change} changes")
            elif self.you_==self.pay:
                print(f"{self.r_name} will get nothing back")

def all_in_one():
    D1 = One_room()
    D1.asking()
    D1.paying()
    D2 = Price()
    D2.get_day_and_resident(D1)
    D2.calcu_price(D1)
    D2.changes(D1)
    Again = input("Do you want to use this with another room? : ")
    if Again == "Yes":
        all_in_one()
    else:
        exit()

all_in_one()