import random
from tkinter import *

class Rectangle():
    def __init__(self):
        self.x1 = random.randint(0,19)
        self.y1 = random.randint(0,19)
        o=0
        while o==0:
            y_2 = random.randint(0,19)
            if y_2>self.y1:
                o=1
        o=0
        while o==0:
            x_2 = random.randint(0,19)
            if x_2>self.x1:
                o=1
        self.x2 = x_2
        self.y2 = y_2
        #print("x is between "+str(self.x1)+" and "+str(self.x2)+"\ny is between "+str(self.y1)+" and "+str(self.y2)+".")
    def show(self):
        #print("x is between "+str(self.x1)+" and "+str(self.x2)+"\ny is between "+str(self.y1)+" and "+str(self.y2)+".")
        i=0
        return([self.x1,self.x2,self.y1,self.y2])

class Player():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Checker():
    def __init__(self):
        pass
    def check(self,Player,Rectangle):
        x = int(Player.x)
        y = int(Player.y)
        x1 = Rectangle.x1
        x2 = Rectangle.x2
        y1 = Rectangle.y1
        y2 = Rectangle.y2
        Rectangle.show()
        if (x>=x1 and x<=x2) and (y>=y1 and y<=y2):
            return("correct!")
        else:
            return("incorrect!")

class Rectangle_Game():
    def __init__(self):
        self.window = Tk()
        self.window.title("Rectangle Game")
        self.window.geometry("400x400")
        lb = Label(self.window, text="Guess the Rectangle", font=("Arial Bold", 20))
        lb.grid(row=1,column=2)
        lb1 = Label(self.window, text="Guess X", font=("Arial", 16))
        lb1.grid(row=5,column=1)
        lb2 = Label(self.window, text="Guess Y", font=("Arial", 16))
        lb2.grid(row=6,column=1)
        self.w = Canvas(self.window ,bg='black', width=200, height=200)
        self.w.grid(row=2,column=2)
        txt = Entry(self.window, width="20")
        txt.grid(column=2, row=5)
        txt2 = Entry(self.window, width="20")
        txt2.grid(column=2, row=6)
        i=0
        while i < 200:
            o=0
            while o < 200:
                if o%20==0:
                    self.w.create_rectangle(o, i, o+10, i+10, fill='black', outline = 'white')
                else:
                    self.w.create_rectangle(o, i, o+10, i+10, fill='black', outline = 'white')
                o=o+10
            i=i+10
        rectangle1 = Rectangle()
        def click():
            player1 = Player(int(txt.get()),int(txt2.get()))
            checker1 = Checker()
            lb.configure(text=checker1.check(player1,rectangle1))
            x = rectangle1.show()
            x1 =x[0]*10
            x2 =x[1]*10
            y1 =x[2]*10
            y2 =x[3]*10
            i=y1
            while i<y2+10:
                o=x1
                while o<x2+10:
                    #print(str(o)+str(i))
                    self.w.create_rectangle(o, i, o+10, i+10, fill='green')
                    o=o+10
                i=i+10
            self.w.create_rectangle(player1.x*10, player1.y*10, player1.x*10+10, player1.y*10+10, fill='red')
            

        bt= Button(self.window, text="Check Answer", bg="Orange", fg="white", command=click)
        bt.grid(column=2,row=7)
        self.window.mainloop()





#rectangle1 = Rectangle()
#rectangle1.show()
#player1 = Player(input("Guess X : "),input("Guess Y : "))
#checker1 = Checker()
#Checker1.check(Player1,rectangle1)
Game = Rectangle_Game()
