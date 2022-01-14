
class Renter:
    def __init__(self,name):
        self.name = name
        self.day = 0
        self.payment = 0

    def get_name(self):
        return(self.name)

    def get_day(self):
        return(self.day)
    
    def set_day(self,day):
        self.day = day

    def set_payment(self,payment):
        self.payment = payment

    def get_payment(self):
        return(self.payment)

class Dorm:
    def __init__(self):
        self.occupants = []
        self.rental_fee = 0

    def set_rent(self,rent):
        self.rental_fee = rent

    def add_occupants(self,renter):
        self.occupants.append(renter)

    def calculate(self):
        renter_no = len(self.occupants)
        i = 0
        s = 0
        while i < renter_no:
            s = s+self.occupants[i].get_day()
            i = i+1
        p = self.rental_fee/s
        i=0
        while i < renter_no:
            r = self.occupants[i]
            d = r.get_day()
            r.set_payment(d*p)
            i=i+1

room = Dorm()

room.set_rent(int(input("Enter the total amount of rent : ")))
renter_no = int(input("Number of occupants : "))
d = input("What is the bill period? E.g. 22 Feb : ")

i = 0
while i < renter_no:
    x = Renter(input("Renter no. "+str(i+1)+"'s Name : "))
    x.set_day(int(input(str(x.get_name())+"'s day(s) of stay : ")))
    room.add_occupants(x)
    i = i+1

room.calculate()

print(d)
i = 0
while i < renter_no:
    y = room.occupants[i]
    print(str(y.get_name())+"'s rent : "+str(y.get_payment()))
    i = i+1
