from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("1000x600")  # Set window size

# Create canvas for background
canvas = Canvas(window, width=1000, height=600)
canvas.place(x=0, y=0)  # Use place instead of pack

# Add background image
img = Image.open('images/background.png')
img = img.resize((1000, 600))
photo = ImageTk.PhotoImage(img)
background = canvas.create_image(0, 0, image=photo, anchor=NW)
canvas.image = photo  # Keep reference

# Create frames using grid layout
top_left = Frame(window, bg='', width=500, height=110)  # Set explicit size
top_left.grid(row=0, column=0, columnspan=4)

WIDTH = 9
HEIGHT = 6

# Add padding to all_cards
all_cards = Button(top_left, width=WIDTH, height=HEIGHT, bg='white')
all_cards.grid(row=0, column=0, padx=(10, 5), pady=(10, 5))

# Add padding to card1
card1 = Button(top_left, width=WIDTH, height=HEIGHT, bg='yellow')
card1.grid(row=0, column=1, padx=(5, 5), pady=(10, 5))

# Add padding to card2
card2 = Button(top_left, width=WIDTH, height=HEIGHT, bg='white')
card2.grid(row=0, column=2, padx=(5, 5), pady=(10, 5))

# Add padding to card3
card3 = Button(top_left, width=WIDTH, height=HEIGHT, bg='yellow')
card3.grid(row=0, column=3, padx=(5, 5), pady=(10, 5))



window.mainloop()