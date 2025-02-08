from tkinter import *

from cards import Cards
from init_widgets import init_window , init_left_frame, init_right_frame

window = Tk()

cards = Cards()

init_window(window)

init_left_frame(window, cards)

init_right_frame(window, cards)


window.mainloop()