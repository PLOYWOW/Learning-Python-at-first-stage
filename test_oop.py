class Card():
    def __init__(self):
        self.x = 1
        self.y = 2

class GM():
    def __init__(self,decx):
        self.decx = decx
        #print(self.decx.x, self.decx.y)
    def card(self):
        print(self.decx.x, self.decx.y)

test = Card()
hi = GM(test)
hi.card()


#print(test.name)