from tkinter import *
import random
import time
from ball import Ball

from pong_bar import Pongbar


tk = Tk()

tk.title("Pong For One")
screen = Canvas(tk, width=600, height=400, bd=0, bg='grey')
screen.pack()
label = screen.create_text(5, 5, anchor=NW, text="Score: ", font=("Courier New Bold",20))
tk.update()
bar = Pongbar(screen, 'black')
ball = Ball(screen, 'green', 35, bar)



while ball.dropped == False:
    ball.draw_ball()
    bar.draw_bar()
    screen.itemconfig(label, text="Score: "+str(ball.score))
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)


# Game Over
go_label = screen.create_text(250,200,text="GAME OVER",font=("Courier New Bold",50))
tk.update()
time.sleep(5.00)

