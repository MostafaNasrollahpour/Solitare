from tkinter import *
from PIL import Image, ImageTk

from cards import Cards

window = Tk()
window.geometry("1000x600")  # Set window size

cards = Cards()

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

WIDTH = 80
HEIGHT = 120


# Add padding to all_cards
all_cards_img = ImageTk.PhotoImage(Image.open(cards.get_back()).resize((WIDTH, HEIGHT)))
all_cards = Button(top_left, width=WIDTH, height=HEIGHT, bg='white', image=all_cards_img)
all_cards.grid(row=0, column=0, padx=(10, 5), pady=(10, 5))

# Add padding to card1
card1_img = ImageTk.PhotoImage(Image.open(cards.get_card()).resize((WIDTH, HEIGHT)))
card1 = Button(top_left, width=WIDTH, height=HEIGHT, bg='yellow',image=card1_img)
card1.grid(row=0, column=1, padx=(5, 5), pady=(10, 5))

# Add padding to card2
card2_img = ImageTk.PhotoImage(Image.open(cards.get_card()).resize((WIDTH, HEIGHT)))
card2 = Button(top_left, width=WIDTH, height=HEIGHT, bg='white',image=card2_img)
card2.grid(row=0, column=2, padx=(5, 5), pady=(10, 5))

# Add padding to card3
card3_img = ImageTk.PhotoImage(Image.open(cards.get_card()).resize((WIDTH, HEIGHT)))
card3 = Button(top_left, width=WIDTH, height=HEIGHT, bg='yellow', image=card3_img)
card3.grid(row=0, column=3, padx=(5, 5), pady=(10, 5))



window.mainloop()