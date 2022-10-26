from tkinter import *
import random

class Ball:
    def __init__(self, screen, color, size, bar):
        self.screen = screen
        self.bar = bar
        self.id = screen.create_oval(10, 10, size, size, fill=color)
        self.screen.move(self.id, 245, 100)
        self.dx = random.randrange(-3,3)
        self.dy = -1
        self.dropped = False
        self.score = 0

        

    def draw_ball(self):
        
        self.screen.move(self.id, self.dx, self.dy)
        pos = self.screen.coords(self.id)
        if pos[1] <= 0:
            self.dy = 3
        if pos[3] >= 400:
            self.dropped = True
        if pos[0] <= 0:
            self.dx = 3
        if pos[2] >= 600:
            self.dx = -3
        if self.made_contact(pos) == True:
            self.dy = -3
            self.dx = random.randrange(-3,3)
            self.score += 1

    def made_contact(self, pos):
        bar_pos = self.screen.coords(self.bar.id)
        if pos[2] >= bar_pos[0] and pos[0] <= bar_pos[2]:
            if pos[3] >= bar_pos[1] and pos[3] <= bar_pos[3]:
                return True
        return False

