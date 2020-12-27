""" Kaynak dosyları yükleyen fonksiyonlar"""

import os

import pygame


def load_all_files(directory, accept=("*.*",)):
    """Create a dictionary of paths to music files in given directory
    if their extensions are in accept."""
    files = {}
    for file in os.listdir(directory):
        name, ext = os.path.splitext(file)
        if ext.lower() in accept:
            files[name] = os.path.join(directory, file)
    return files


def load_all_fonts(directory, accept=(".ttf",)):
    return load_all_files(directory, accept)


def load_all_movies(directory, accept=(".mpg",)):
    return load_all_files(directory, accept)


def load_all_music(directory, accept=(".wav", ".mp3", ".ogg", ".mdi")):
    return load_all_files(directory, accept)


def load_all_sfx(directory, accept=(".wav", ".mp3", ".ogg", ".mdi")):
    return load_all_files(directory, accept)


def load_all_images(directory, colorkey=(255, 0, 255), accept=(".png", ".jpg", ".bmp")):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name] = img
    return graphics
