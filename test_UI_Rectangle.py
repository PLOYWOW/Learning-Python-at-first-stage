from tkinter import *
window = Tk()
window.title("Rectangle Game")
window.geometry("1000x1000")
w = Canvas(window, width=40, height=40)
w.create_rectangle(100, 100, 110, 110, fill="blue", outline = 'blue')
w.grid(row=2,column=10)
window.mainloop()