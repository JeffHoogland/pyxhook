"""
A simple example of hooking the keyboard on Linux using pyxhook

Any key pressed prints out the keys values, program terminates when spacebar is pressed
"""


import pyxhook
import time

def kbevent( event ):
    print event
    
    if event.Ascii == 32:
        global running
        running = False

hookman = pyxhook.HookManager()
hookman.KeyDown = kbevent
hookman.HookKeyboard()
hookman.start()
    
running = True

while running:
    time.sleep(0.1)
    
hookman.cancel()
