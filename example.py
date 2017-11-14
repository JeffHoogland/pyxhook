"""
A simple example of hooking the keyboard on Linux using pyxhook

Any key pressed prints out the keys values, program terminates when spacebar
is pressed.
"""
from __future__ import print_function

# Libraries we need
import pyxhook
import time


# This function is called every time a key is presssed
def kbevent(event,parameters):
	global running
	# print key info
	print(event)
	parameters['test']=2
	# If the ascii value matches spacebar, terminate the while loop
	if event.Ascii == 32:
		running = False

test_parameters={'test':1}

print('Parameters before press:'+str(test_parameters))
# Create hookmanager
hookman = pyxhook.HookManager()
# Define our callback to fire when a key is pressed down
hookman.KeyDown = kbevent
# Define our parameters for callback function
hookman.KeyDownParameters = test_parameters
# Hook the keyboard
hookman.HookKeyboard()
# Start our listener
hookman.start()

# Create a loop to keep the application running
running = True
while running:
	time.sleep(0.1)
# Use parametrs without global
print('Parameters after press:'+str(test_parameters))
# Close the listener when we are done
hookman.cancel()
