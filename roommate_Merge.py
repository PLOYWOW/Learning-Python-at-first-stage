class People:
    def __init__(self):
        pass
    def owner_room(self,name):
        self.name = name
        #return self.name
    def roommate(self,roommate_name):
        self.roommate_name = roommate_name
        #return self.roommate_name

class Room:
    def __init__(self):
        pass
    def checkbill(self):
        self.price = int(input("Enter the total amount: "))
        self.bill = input("What is the bill period? ")
    def owner_check(self):
        self.owner_name = input("What is your name? ")
        self.stay1 = int(input(f"How many days did {self.owner_name} stay? "))
    def roommate_check(self):
        self.roommate_name = input("What is the name of the other roommate? ")
        self.stay2 = int(input(f"How many days did {self.roommate_name} stay? "))
    def calculate(self):
        sum_of_date = self.stay1 + self.stay2
        money1 = (self.stay1 * self.price) // sum_of_date
        money2 = (self.stay2 * self.price) // sum_of_date
        print(self.bill[12:])
        print(f"{self.owner_name} pays : {money1}")
        print(f"{self.roommate_name} pays : {money2}")

room = Room()
room.checkbill()
room.owner_check()
room.roommate_check()
room.calculate()


