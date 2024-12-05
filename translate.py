# Example file showing a basic pygame "game loop"
import pygame as pg
from widgets.input_box import InputBox
from widgets.submit_button import SubmitButton

# actions
def hexToChar():
    result = ''
    for bit in bits:
        byte = bytes.fromhex(bit.text)
        ascii_char = byte.decode("ASCII")
        result += ascii_char
    print('Submitted: ' + result)

# pygame setup
pg.init()
screen = pg.display.set_mode((1000, 1000))
clock = pg.time.Clock()
running = True

bit1 = InputBox(50, 450, 100, 100)
bit2 = InputBox(250, 450, 100, 100)
bit3 = InputBox(450, 450, 100, 100)
bit4 = InputBox(650, 450, 100, 100)
bit5 = InputBox(850, 450, 100, 100)
bits = [bit1, bit2, bit3, bit4, bit5]

submit = SubmitButton(400, 650, 200, 80, action=hexToChar)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        for box in bits:
            box.handle_event(event)
        submit.handle_event(event)

    for box in bits:
        box.update()
    submit.update()
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    for box in bits:
        box.draw(screen)
    submit.draw(screen)

    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(60)  # limits FPS to 60

pg.quit()