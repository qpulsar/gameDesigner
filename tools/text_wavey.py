import math

import pygame

class textWavey:
    def __init__(self, font, message, fontcolor, amount=10):
        self.base = font.render(message, 0, fontcolor)
        self.steps = range(0, self.base.get_width(), 2)
        self.amount = amount
        self.size = self.base.get_rect().inflate(0, amount).size
        self.offset = 0.0

    def animate(self):
        s = pygame.Surface(self.size)
        height = self.size[1]+5
        self.offset += 0.3
        for step in self.steps:
            src = pygame.Rect(step, 0, 2, height)
            dst = src.move(0, math.cos(self.offset + step * .02) * self.amount)
            s.blit(self.base, dst, src)
        return s
