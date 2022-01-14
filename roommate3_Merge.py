class Roommate:
    def __init__(self,name,days):
        self.name = name
        self.days = days

    def pay(self,mate_date):
        amount = (int(self.days) * total) / (mate_date + self.days)
        return amount

total = int(input("Enter the total amount: "))
bill = input("What is the bill period? E.g. Oct 12: ")

name_person1 = input("What is your name? ")
days_person1 = int(input(f"How many days did {name_person1} stay? "))

name_person2 = input("What is yout roommate name? ")
days_person2 = int(input(f"How many days did {name_person2} stay? "))

person1 = Roommate(name_person1,days_person1)
person2 = Roommate(name_person2,days_person2)

print(bill)
print(f"{name_person1} pays: {person1.pay(days_person2)}")
print(f"{name_person2} pays: {person2.pay(days_person1)}")

