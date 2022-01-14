class Roommate():
    def __init__(self,name,days):
        self.name = name
        self.days = int(days)
    
    def pay(self,mate_days,total_amount):
        amount = int((self.days/(int(self.days+mate_days)))*int(total_amount))
        return amount