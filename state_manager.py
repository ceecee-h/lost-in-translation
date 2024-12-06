import pygame as pg
from widgets.input_box import InputBox
from widgets.submit_button import SubmitButton
from widgets.char_box import CharBox

pg.init()

class InputMode():
    
    def __init__(self):
        self.bit1 = InputBox(50, 450, 100, 100)
        self.bit2 = InputBox(250, 450, 100, 100)
        self.bit3 = InputBox(450, 450, 100, 100)
        self.bit4 = InputBox(650, 450, 100, 100)
        self.bit5 = InputBox(850, 450, 100, 100)
        self.bits = [self.bit1, self.bit2, self.bit3, self.bit4, self.bit5]

        self.submit = SubmitButton(400, 650, 200, 80, text='TRANSLATE', action=self.hexToChar)
        self.swapRequest = False
        self.text = ''
    
    def handle_event(self, event):
        for bit in self.bits:
            bit.handle_event(event)
        self.submit.handle_event(event)
    
    def update(self):
        for bit in self.bits:
            bit.update()
        self.submit.update()
    
    def draw(self, screen):
        for bit in self.bits:
            bit.draw(screen)
        self.submit.draw(screen)
    
    def reset(self):
        for bit in self.bits:
            bit.text = ''
        self.text = ''
        self.swapRequest = False
        
    def addSwapRequest(self):
        self.swapRequest = True
    
    # actions
    def hexToChar(self):
        result = ''
        for bit in self.bits:
            byte = bytes.fromhex(bit.text)
            ascii_char = byte.decode("ASCII")
            result += ascii_char
        print('Submitted: ' + result)
        self.text = result
        self.addSwapRequest()

class StaticMode():
    
    def __init__(self, text):
        self.text = text if len(text) == 5 else text + ''.join(['?' for _ in range(5-len(text))])
        self.ch1 = CharBox(50, 450, 100, 100, text=self.text[0])
        self.ch2 = CharBox(250, 450, 100, 100, text=self.text[1])
        self.ch3 = CharBox(450, 450, 100, 100, text=self.text[2])
        self.ch4 = CharBox(650, 450, 100, 100, text=self.text[3])
        self.ch5 = CharBox(850, 450, 100, 100, text=self.text[4])
        self.chs = [self.ch1, self.ch2, self.ch3, self.ch4, self.ch5]
        self.swapRequest = False

        self.submit = SubmitButton(400, 650, 200, 80, text='RESET', action=self.addSwapRequest)

    def set_text(self, text):
        self.text = text if len(text) == 5 else text + ''.join(['?' for _ in range(5-len(text))])
        for i in range(5):
            self.chs[i].text = self.text[i]
    
    def handle_event(self, event):
        for ch in self.chs:
            ch.handle_event(event)
        self.submit.handle_event(event)
    
    def update(self):
        for ch in self.chs:
            ch.update()
        self.submit.update()
    
    def draw(self, screen):
        for ch in self.chs:
            ch.draw(screen)
        self.submit.draw(screen)
    
    def addSwapRequest(self):
        self.swapRequest = True

    def reset(self):
        self.set_text('?????')
        self.swapRequest = False

class StateManager:
    
    def __init__(self):
        self.inputMode = InputMode()
        self.staticMode = StaticMode(text='?????')
        self.isInputMode = True
        
    def handle_event(self, event):
        if self.isInputMode:
            self.inputMode.handle_event(event)
        else:   
            self.staticMode.handle_event(event)
        if self.inputMode.swapRequest or self.staticMode.swapRequest:
            self.swapMode()
    
    def update(self):
        if self.isInputMode:
            self.inputMode.update()
        else:
            self.staticMode.update()
    
    def draw(self, screen):
        if self.isInputMode:
            self.inputMode.draw(screen)
        else:
            self.staticMode.draw(screen)
    
    def swapMode(self):
        self.staticMode = StaticMode(self.inputMode.text)
        self.inputMode = InputMode()
        self.isInputMode = not self.isInputMode