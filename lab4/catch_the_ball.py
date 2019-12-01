from tkinter import *
from random import randrange as rnd, choice
import math
import time

global n
n = 0

root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

def main():
    canv.bind('<Button-1>', click)
    new_ball()
    mainloop()
    if n > 5:
        print("All")
    else:
        print(str(n))

colors = ['red','orange','yellow','green','blue']
def new_ball():
    global x, y, r, n
    canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    root.after(1000,new_ball)


def distance_calculation(a, b, c, d):
    x = a - c
    y = b - d
    if x < 0:
        pass
    if y < 0:
        pass
    e = x*x+y*y
    f = math.sqrt(e)
    return (f)


def click(event):
    global n
    if n < 5:
        if distance_calculation(event.x, event.y, x, y) <= r:
            print('Ok')
            n += 1
    else:
        print("The End!")



main()