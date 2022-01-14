class People_in_dorm:
    def __init__(self):
        self.room_number=input("Your room number : ")
        self.number_of_people=int(input("Number of people in this room : "))
        self.people_list=[]
        self.p_name=[]
        self.p_name.clear()
        self.people_list.clear()
        for i in range(self.number_of_people):
            self.people=input("What is your name : ")
            self.day=int(input(f"Day that {self.people} lives in this room : "))
            self.people_list.append([self.people_list,self.day])
            self.p_name.append(self.people)

class Price:
    def __init__(self):
        self.price=int(input("Total Price : "))
    def calcu_price(self,people):
        self.d=[]
        self.d.clear()
        self.num_peo=people.number_of_people
        self.pd=0
        for i in range(self.num_peo):
            self.day_i=people.people_list[i][1]
            self.d.append(self.day_i)
            self.pd+=self.day_i
        self.one_ratio=self.price/self.pd
        for j in range(len(self.d)):
            self.pay=self.d[j]*self.one_ratio
            self.r_name=people.p_name[j]
            print(f"{self.r_name} must pay {self.pay} for room {people.room_number}")

def all_in_one():
    D1=People_in_dorm()
    D2=Price()
    D2.calcu_price(D1)
    Again=input("Do you want to use this with another room? : ")
    if Again=="Yes":
        all_in_one()
    else:
        exit()

all_in_one()