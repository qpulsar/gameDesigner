""" Menü Ekranı"""
import pygame
import pygame_gui
from pygame_gui.elements import UIButton

import config
from states._State import _State


class MainMenu(_State):
    """This State is updated while our game shows the splash screen."""

    def __init__(self):
        _State.__init__(self)
        self.next = "SPLASH"
        self.timeout = 5
        self.cover = pygame.Surface(config.SCREEN_SIZE).convert()
        self.cover.fill(0)
        self.cover_alpha = 256
        self.alpha_step = 2
        self.image = config.BACKGROUND['menu_bg']
        self.rect = self.image.get_rect(center=config.SCREEN_RECT.center)

        # Her ekranın kendi manager'ı olsun
        self.ui_manager = pygame_gui.UIManager(config.SCREEN_SIZE, config.theme_dir / 'theme_1.json')

        self.design_btn = UIButton(relative_rect=pygame.Rect(-435, -400, 300, 70),
                                   text='Oyun Tasarla',
                                   manager=self.ui_manager,
                                   anchors={'left': 'right',
                                            'right': 'right',
                                            'top': 'bottom',
                                            'bottom': 'bottom'})
        self.play_btn = UIButton(relative_rect=pygame.Rect(-435, -300, 300, 70),
                                 text='Oyun Oyna',
                                 manager=self.ui_manager,
                                 anchors={'left': 'right',
                                          'right': 'right',
                                          'top': 'bottom',
                                          'bottom': 'bottom'})

    def update(self, surface, keys, current_time, time_delta):
        """Updates the splash screen."""
        self.current_time = current_time
        surface.blit(self.image, self.rect)
        self.cover.set_alpha(self.cover_alpha)
        self.cover_alpha = max(self.cover_alpha - self. alpha_step, 0)
        surface.blit(self.cover, (0, 0))

        self.ui_manager.update(time_delta)
        self.ui_manager.draw_ui(config.screen)

    def get_event(self, event):
        """Get events from Control. Currently changes to next state on any key
        press."""
        if event.type == pygame.QUIT:
            self.is_running = False

        # Olayları kontrol et
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.design_btn:
                    self.next = "GAMETYPE"
                    self.done = True

        # GUI olaylarını işler
        self.ui_manager.process_events(event)
