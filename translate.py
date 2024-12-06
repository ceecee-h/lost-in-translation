# Example file showing a basic pygame "game loop"
import pygame as pg
from state_manager import StateManager
   
# pygame setup
pg.init()
screen = pg.display.set_mode((1000, 1000))
clock = pg.time.Clock()
running = True   
# pages

manager = StateManager()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # handle events
        manager.handle_event(event)

    # update
    manager.update()
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    manager.draw(screen)

    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()