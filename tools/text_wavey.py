import math

import pygame


class textWavey:
    def __init__(self, font, message, fontcolor, amount=10):
        self.base = font.render(message, 0, fontcolor)
        print("base:", self.base)
        self.steps = range(0, self.base.get_width(), 2)
        self.amount = amount
        self.size = list(self.base.get_rect().inflate(0, amount).size)
        self.size[1] += 130
        self.offset = 0.0

    def animate(self):
        s = pygame.Surface(self.size)
        s.set_colorkey((0, 0, 0))
        height = self.size[1] + 5
        self.offset += 0.3
        for step in self.steps:
            src = pygame.Rect(step, 0, 2, height)
            dst = list(src.move(0, math.cos(self.offset + step * .02) * self.amount))
            dst[1] += 40
            s = s.convert_alpha()

            s.blit(self.base, dst, src)
        return s
