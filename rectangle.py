import random
from tkinter import *

class Window():
    def __init__(self):
        window = Tk()
        window.title("Rectangle Game")
        window.geometry("800x800")
        lb = Label(window, text="Guess the Rectangle", font=("Arial Bold", 50))
        lb.pack()
        w = Canvas(window, width=200, height=200)
        i=0
        while i < 200:
            o=0
            while o < 200:
                if o%20==0:
                    w.create_rectangle(o, i, o+10, i+10, fill='black', outline = 'white')
                else:
                    w.create_rectangle(o, i, o+10, i+10, fill='black', outline = 'white')
                o=o+10
            i=i+10
        w.pack()
        window.mainloop()
    def write_pixel(self,x,y):
        pass







class Rectangle():
    def __init__(self):
        self.x1 = random.randint(0,20)
        self.y1 = random.randint(0,20)
        o=0
        while o==0:
            y_2 = random.randint(0,20)
            if y_2>self.y1:
                o=1
        o=0
        while o==0:
            x_2 = random.randint(0,20)
            if x_2>self.x1:
                o=1
        self.x2 = x_2
        self.y2 = y_2
    def show(self):
        print("x is between "+str(self.x1)+" and "+str(self.x2)+"\ny is between "+str(self.y1)+" and "+str(self.y2)+".")
        i=0
        while i<self.x2-self.x1:

            i=i+1

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
        if (x>=x1 and x<=x2) and (y>=y1 and y<=y2):
            print("correct!")
        else:
            print("incorrect!")
        Rectangle.show()

#rectangle1 = Rectangle()
#rectangle1.show()
#Player1 = Player(input("Guess X : "),input("Guess Y : "))
##Checker1 = Checker()
#Checker1.check(Player1,rectangle1)
Window1 = Window()
