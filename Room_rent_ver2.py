class Person():
    #เก็บ Name & Day
    def __init__(self,name,day):
        self.name = name
        self.day = int(day)

    def calculating(self,monthly_rate):
        self.monthly_rate = monthly_rate.monthly_rate
        total_day = int(person1.day) + int(person2.day)
        percent = self.day/total_day
        self.pay = int(percent*(int(self.monthly_rate)))

class Bill():
    #เก็บ Total Amount + เก็บ Bill Period
    def __init__(self):
        self.monthly_rate = input("Enter the total amount: ")
        self.bill_period = input("What is the bill period? E.g. June 25: ")

    def bill_printing(self,person1,person2):
        self.name1 = person1.name
        self.name2 = person2.name
        self.pay1 = person1.pay
        self.pay2 = person2.pay
        print("***************_____Bill_____***************")
        print("Bill for",self.bill_period,"Rental is as following")
        print(self.name1,"pays:",self.pay1)
        print(self.name2,"pays:",self.pay2)

bill = Bill()
person1 = Person(input("What is your name? "), input("How many days did you stay? "))
person2 = Person(input("What is the name of other roommate? "), input("How many days did he/she stay? "))
person1.calculating(bill)
person2.calculating(bill)
bill.bill_printing(person1, person2)


