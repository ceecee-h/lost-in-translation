import pygame as pg
from constants import *

pg.init()
hex_chars = '0123456789ABCDEFabcdef'
class InputBox:

    def __init__(self, x, y, w, h, text='', length=2, next=None, prev=None):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.length = length
        self.txt_surface = INPUT_FONT.render(text, True, self.color)
        self.active = False
        self.next = next
        self.prev = prev
        
    def setNext(self, next):
        self.next = next

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                elif event.key == pg.K_BACKSPACE:
                    if len(self.text) == 0:
                        self.active = False
                        if self.prev:
                            self.prev.active = True
                            self.prev.handle_event(event)
                    self.text = self.text[:-1]
                elif len(self.text) < self.length:
                    if event.unicode in hex_chars:       
                        self.text += event.unicode
                else:
                    # spill over to next box
                    if self.next:
                        self.next.active = True
                    self.active = False
        # Re-render the text.                
        self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        self.txt_surface = INPUT_FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(100, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
