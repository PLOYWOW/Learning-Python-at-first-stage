class Bill():
    def __init__(self):
        pass

#เก็บ Total Amount
    def total_amount(self, monthly_rate):
        self.monthly_rate = monthly_rate
    
#เก็บ Bill Period
    def period(self, bill_period):
        self.bill_period = bill_period
        
#คิดตัง 
    def calculation(self, day1, day2): 
        self.day1 = day1
        self.day2 = day2
        total_day = int(self.day1) + int(self.day2)
        percent1 = int(self.day1)/total_day
        percent2 = int(self.day2)/total_day
        pay1 = percent1*(int(self.monthly_rate))
        pay1_int = int(pay1)
        pay2 = percent2*(int(self.monthly_rate))
        pay2_int = int(pay2)
        pay = [pay1_int,pay2_int]
        return pay
        
#ออกบิล
    def bill_printing(self,pay_final, name1, name2):
        self.pay_final = pay_final
        self.name1 = name1
        self.name2 = name2
        print("***************_____Bill_____***************")
        print("Bill for",self.bill_period,"Rental is as following")
        print(self.name1,"pays:",self.pay_final[0])
        print(self.name2,"pays:",self.pay_final[1])

bill = Bill()
bill.total_amount(input("Enter the total amount: "))
bill.period(input("What is the bill period? E.g. June 25: "))
rentor1_name = input("What is your name? ")
print("How many days did",str(rentor1_name),"stay? ", end='')
rentor1_day = input()
rentor2_name = input("What is the name of the other roommate? ")
print("How many days did",str(rentor2_name),"stay? ", end='')
rentor2_day = input()
final_pay = bill.calculation(rentor1_day,rentor2_day)
bill.bill_printing(final_pay,rentor1_name,rentor2_name)
