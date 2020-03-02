import pygame
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data1', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def sprite_sheet(name, len_x, len_y, count=(0, 0), pos=(0, 0)):  # Cut animation sheet
    sheet = load_image(name, -1)
    sheet_rect = sheet.get_rect()

    len_sprite_x, len_sprite_y = len_x, len_y  # Len of cut
    sprite_rect_x, sprite_rect_y = pos  # Beginning of cut

    if count == (0, 0):
        count = (sheet_rect.height // len_y, sheet_rect.width // len_x)

    sprites = []
    for i in range(count[0]):
        for j in range(count[1]):
            sheet.set_clip(pygame.Rect(sprite_rect_x, sprite_rect_y, len_sprite_x, len_sprite_y))
            sprite = sheet.subsurface(sheet.get_clip())
            sprites.append(sprite)
            sprite_rect_x += len_sprite_x

        sprite_rect_y += len_sprite_y
        sprite_rect_x = 0
    return sprites
