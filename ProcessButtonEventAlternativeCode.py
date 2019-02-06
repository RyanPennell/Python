import sys
import tkinter
from tkinter import * # Import all definitions from tkinter
class ProcessButtonEvent:
	def __init__(self):
		window = Tk() # Create a window
		btOK = Button(window, text = "OK", fg = "red",
			command = self.processOK )
		btCancel = Button(window, text = "Cancel", bg = "yellow",
			command = self.processCancel )
		btOK.pack() # Place the OK button in the window
		btCancel.pack() # Place the Cancel button in the window place button
		window.mainloop() # Create an event loop event loop
def processOK(self):
	print("OK button is clicked") #process OK
def processCancel(self):
	print("Cancel button is clicked")

ProcessButtonEvent() # Create an object to invoke _ _init_ _ method
