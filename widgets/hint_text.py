import pygame as pg
from constants import *

pg.init()

class HintText:

    def __init__(self, x, y, w, h, text='', length=2):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.length = length
        self.txt_surface = HINT_FONT.render(text, True, self.color)
        self.script_surface = HINT_FONT.render('Binary Translation', True, self.color)


    def handle_event(self, event):
        pass

    def update(self):
        # Resize the box if the text is too long.
        width = max(100, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.script_surface, (self.rect.x+5, self.rect.y+5))
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+30))
        # Blit the rect.
        #pg.draw.rect(screen, self.color, self.rect, 2)
