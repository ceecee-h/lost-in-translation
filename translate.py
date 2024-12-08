import pygame as pg
from state_manager import StateManager
   
# pygame setup
pg.init()
screen = pg.display.set_mode((800, 800))
clock = pg.time.Clock()
bg = pg.image.load("assets/bg_800.png")
running = True

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
    screen.blit(bg, (0, 0))

    # RENDER YOUR GAME HERE
    manager.draw(screen)

    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()