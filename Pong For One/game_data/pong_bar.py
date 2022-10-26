from tkinter import *
import random


class Pongbar:
    def __init__(self, screen, color):
        self.screen = screen
        self.id = screen.create_rectangle(0,0, 100, 10, fill=color)
        self.screen.move(self.id, 200, 350)
        self.dx = 0
        self.screen.bind_all('<KeyPress-Left>', self.move_left)
        self.screen.bind_all('<KeyPress-Right>', self.move_right)


    def draw_bar(self):
        self.screen.move(self.id, self.dx, 0)
        pos = self.screen.coords(self.id)
        if pos[0] <= 0:
            self.dx = 0
        if pos[2] >= 600:
            self.dx = 0

            


    def move_left(self, evt):
        self.dx = -3


    def move_right(self, evt):
        self.dx = 3
    