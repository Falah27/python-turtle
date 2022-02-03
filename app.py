from tkinter import mainloop
import turtle

colors =['red', 'green', 'cyan', 'orange', 'yellow', 'white']
f=turtle.Pen()
r=turtle.Screen()
r.bgcolor("black")

for i in  range(360):
    f.pencolor(colors[i%6])
    f.width(i//100+1)
    f.forward(i)
    f.left(61)
mainloop()