""" initial values and source folders"""

import os
import pygame
from pathlib import Path
import pygame_gui

# TITLE
import loader

title = "AltıKod GameDesigner"
# SCREEN
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)


# DIRS
base_dir = Path(".")
resource_dir = base_dir / "resources"
images_dir = resource_dir / "images"
bg_dir = images_dir / "backgrounds"
gfx_dir = images_dir / "gfx"
gui_dir = images_dir / "gui"
sprite_dir = images_dir / "sprites"
music_dir = resource_dir / "musics"
sound_dir = resource_dir / "sounds"
theme_dir = resource_dir / "themes"
font_dir = resource_dir / "fonts"

# INITS
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = "TRUE"  # Ekranı ortala
pygame.display.set_caption(title)
screen = pygame.display.set_mode(SCREEN_SIZE)
SCREEN_RECT = screen.get_rect()

# LOAD RESOURCES
FONTS = loader.load_all_fonts(font_dir)
MUSIC = loader.load_all_fonts(music_dir)
SFX = loader.load_all_fonts(sound_dir)
BACKGROUND = loader.load_all_images(bg_dir)
IMAGE = loader.load_all_fonts(gfx_dir)
