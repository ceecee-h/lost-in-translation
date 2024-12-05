import pygame as pg

pg.init()
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 80)

class SubmitButton:

    def __init__(self, x, y, w, h, action):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.txt_surface = FONT.render('SUBMIT', True, self.color)
        self.action = action


    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the submit button
            if self.rect.collidepoint(event.pos):
                # call action
                self.action()

    def update(self):
        # Resize the box if the text is too long.
        width = max(100, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
