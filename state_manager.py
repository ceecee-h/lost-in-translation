import pygame as pg
from widgets.input_box import InputBox
from widgets.submit_button import SubmitButton
from widgets.char_box import CharBox
from widgets.hint_text import HintText

pg.init()

class InputMode():
    
    def __init__(self):
        self.bit1 = InputBox(30, 350, 100, 100)
        self.bit2 = InputBox(190, 350, 100, 100, prev=self.bit1)
        self.bit3 = InputBox(350, 350, 100, 100, prev=self.bit2)
        self.bit4 = InputBox(510, 350, 100, 100, prev=self.bit3)
        self.bit5 = InputBox(670, 350, 100, 100, prev=self.bit4)
        self.bit1.setNext(self.bit2)
        self.bit2.setNext(self.bit3)
        self.bit3.setNext(self.bit4)
        self.bit4.setNext(self.bit5)
        
        self.bits = [self.bit1, self.bit2, self.bit3, self.bit4, self.bit5]

        self.submit = SubmitButton(300, 500, 200, 40, text='TRANSLATE', action=self.hexToChar)
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
            if len(bit.text) < 2:
                result += '?'
                continue
            byte = bytes.fromhex(bit.text)
            ascii_char = byte.decode("ASCII")
            result += ascii_char
        print('Submitted: ' + result)
        self.text = result
        self.addSwapRequest()

class StaticMode():
    
    def __init__(self, text):
        self.text = text if len(text) == 5 else text + ''.join(['?' for _ in range(5-len(text))])
        self.ch1 = CharBox(30, 350, 100, 100, text=self.text[0])
        self.ch2 = CharBox(190, 350, 100, 100, text=self.text[1])
        self.ch3 = CharBox(350, 350, 100, 100, text=self.text[2])
        self.ch4 = CharBox(510, 350, 100, 100, text=self.text[3])
        self.ch5 = CharBox(670, 350, 100, 100, text=self.text[4])
        self.chs = [self.ch1, self.ch2, self.ch3, self.ch4, self.ch5]
        self.swapRequest = False

        self.submit = SubmitButton(350, 500, 200, 40, text='RESET', action=self.addSwapRequest)
        self.hint = HintText(50, 700, 200, 200, text=self.textToBin())

    def set_text(self, text):
        self.text = text if len(text) == 5 else text + ''.join(['?' for _ in range(5-len(text))])
        for i in range(5):
            self.chs[i].text = self.text[i]
        self.hint = HintText(50, 700, 200, 200, text=self.textToBin())
    
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
        self.hint.draw(screen)
    
    def addSwapRequest(self):
        self.swapRequest = True

    def reset(self):
        self.set_text('?????')
        self.swapRequest = False
    
    def textToBin(self):
        result = ' '.join(format(x, 'b') for x in bytearray(self.text, 'ascii'))
        return result

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