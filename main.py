"""
BÖTE GAME DESIGNER

"""
import pygame
from pygame.locals import *

import pygame_gui
from pygame_gui.elements import UIButton, UIImage
from pygame_gui.windows import UIFileDialog
from pygame_gui.core.utility import create_resource_path
import os


class BoardGame:
    win_width = 800
    win_height = 600

    # DIRS
    resource_dir = "./resources/"
    images_dir = os.path.join(resource_dir, "images")
    bg_dir = os.path.join(images_dir, "backgrounds")
    gui_dir = os.path.join(images_dir, "gui")
    sprite_dir = os.path.join(images_dir, "sprites")
    music_dir = os.path.join(resource_dir, "musics")
    sound_dir = os.path.join(resource_dir, "sounds")
    theme_dir = os.path.join(resource_dir, "themes")

    def __init__(self):
        print("__init__")
        pygame.init()

        pygame.display.set_caption('BoardGame')
        self.window_surface = pygame.display.set_mode((self.win_width, self.win_height))
        self.ui_manager = pygame_gui.UIManager((800, 600), self.theme_dir + '/theme_1.json')

        self.background = pygame.Surface((self.win_width, self.win_height))
        self.background.fill(self.ui_manager.ui_theme.get_colour('dark_bg'))

        self.deneme_button = UIButton(relative_rect=pygame.Rect(-180, -60, 150, 30),
                                      text='Deneme',
                                      manager=self.ui_manager,
                                      anchors={'left': 'right',
                                               'right': 'right',
                                               'top': 'bottom',
                                               'bottom': 'bottom'})

        self.clock = pygame.time.Clock()
        self.is_running = True

    def run(self):
        while self.is_running:
            time_delta = self.clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

                if event.type == pygame.USEREVENT:
                    print(event.user_type)
                    print(pygame_gui.UI_BUTTON_PRESSED)
                    if (event.user_type == pygame_gui.UI_BUTTON_PRESSED):
                        print("Denedim")
                        self.deneme_button.set_text("Denedim")

            self.ui_manager.update(time_delta)

            self.window_surface.blit(self.background, (0, 0))
            self.ui_manager.draw_ui(self.window_surface)

            pygame.display.update()


if __name__ == '__main__':
    app = BoardGame()
    app.run()
