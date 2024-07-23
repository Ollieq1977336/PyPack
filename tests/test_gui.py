from pypack.gui.button import pack_button
from pypack.gui.window import initialize_window
from pypack.gui.start import start_window

window = initialize_window("My App", "300x200")

def buttonClicked():
	print("Hello, world!")

pack_button(window, "Click me!", buttonClicked)

start_window(window)
