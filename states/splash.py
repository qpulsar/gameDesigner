""" Splash Ekranı"""
import pygame

import config
from states._State import _State
from tools.text_wavey import textWavey


class Splash(_State):
    """This State is updated while our game shows the splash screen."""

    def __init__(self):
        _State.__init__(self)
        self.next = "MAINMENU"
        self.timeout = 5
        self.cover = pygame.Surface(config.SCREEN_SIZE).convert()
        self.cover.fill(0)
        self.cover_alpha = 256
        self.alpha_step = 2
        self.image = config.BACKGROUND['splash_bg']
        self.rect = self.image.get_rect(center=config.SCREEN_RECT.center)
        self.mesaj = "GAME DESIGNER"
        #create our fancy text renderer
        bigfont = pygame.font.Font(None, 60)
        white = 255, 255, 255
        self.renderer = textWavey(bigfont, self.mesaj, white, 16)
        self.text = self.renderer.animate()

    def update(self, surface, keys, current_time, time_delta):
        """Updates the splash screen."""
        self.current_time = current_time
        surface.blit(self.image, self.rect)
        self.cover.set_alpha(self.cover_alpha)
        self.cover_alpha = max(self.cover_alpha - self.alpha_step, 0)
        surface.blit(self.cover, (0, 0))
        self.text = self.renderer.animate()
        surface.blit(self.text, (300, 200))
        if self.current_time - self.start_time > 1000.0 * self.timeout:
            self.done = True

    def get_event(self, event):
        """Get events from Control. Currently changes to next state on any key
        press."""
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
            self.done = True
