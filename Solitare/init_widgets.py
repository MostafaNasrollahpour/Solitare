from tkinter import *
from PIL import Image, ImageTk

from cards import Cards


def init_window(window: Tk):
    window.geometry("1000x600")  # Set window size

    # Create canvas for background
    canvas = Canvas(window, width=1000, height=600)
    canvas.place(x=0, y=0)

    # Add background image
    img = Image.open('images/background.png')
    img = img.resize((1000, 600))
    photo = ImageTk.PhotoImage(img)
    background = canvas.create_image(0, 0, image=photo, anchor=NW)
    canvas.image = photo  # Keep reference


def init_left_frame(window: Tk, cards: Cards):
    # Create frames using grid layout
    top_left = Frame(window, bg='', width=500, height=110)  # Set explicit size
    top_left.grid(row=0, column=0, columnspan=4)

    WIDTH = 80
    HEIGHT = 120

    # Store references to the images
    top_left.images = []

    # Add padding to all_cards
    all_cards_img = ImageTk.PhotoImage(Image.open(cards.get_back()).resize((WIDTH, HEIGHT)))
    top_left.images.append(all_cards_img)  # Keep reference
    all_cards = Button(top_left, width=WIDTH, height=HEIGHT, image=all_cards_img)
    all_cards.grid(row=0, column=0, padx=(10, 5), pady=(10, 5))

    # Add padding to card1
    card1_img = ImageTk.PhotoImage(Image.open(cards.get_card()).resize((WIDTH, HEIGHT)))
    top_left.images.append(card1_img)  # Keep reference
    card1 = Button(top_left, width=WIDTH, height=HEIGHT, image=card1_img)
    card1.grid(row=0, column=1, padx=(5, 5), pady=(10, 5))

    # Add padding to card2
    card2_img = ImageTk.PhotoImage(Image.open(cards.get_card()).resize((WIDTH, HEIGHT)))
    top_left.images.append(card2_img)  # Keep reference
    card2 = Button(top_left, width=WIDTH, height=HEIGHT, image=card2_img)
    card2.grid(row=0, column=2, padx=(5, 5), pady=(10, 5))

    # Add padding to card3
    card3_img = ImageTk.PhotoImage(Image.open(cards.get_card()).resize((WIDTH, HEIGHT)))
    top_left.images.append(card3_img)  # Keep reference
    card3 = Button(top_left, width=WIDTH, height=HEIGHT, image=card3_img)
    card3.grid(row=0, column=3, padx=(5, 5), pady=(10, 5))


def init_right_frame(window: Tk, cards: Cards):
    #Create frames using grid layout
    top_right = Frame(window, bg='', width=500, height=110)  # Set explicit size
    top_right.grid(row=0, column=4, columnspan=4, padx=(220, 0))

    WIDTH = 80
    HEIGHT = 120

    # Store references to the images
    top_right.images = []

    # Add padding to spades
    spades_img = ImageTk.PhotoImage(Image.open(cards.get_spades()).resize((WIDTH, HEIGHT)))
    top_right.images.append(spades_img)  # Keep reference
    spades = Button(top_right, width=WIDTH, height=HEIGHT, image=spades_img)
    spades.grid(row=0, column=0, padx=(10, 5), pady=(10, 5))

    # Add padding to heart
    heart_img = ImageTk.PhotoImage(Image.open(cards.get_heart()).resize((WIDTH, HEIGHT)))
    top_right.images.append(heart_img)  # Keep reference
    heart = Button(top_right, width=WIDTH, height=HEIGHT, image=heart_img)
    heart.grid(row=0, column=1, padx=(5, 5), pady=(10, 5))

    # Add padding to clubs
    clubs_img = ImageTk.PhotoImage(Image.open(cards.get_clubs()).resize((WIDTH, HEIGHT)))
    top_right.images.append(clubs_img)  # Keep reference
    clubs = Button(top_right, width=WIDTH, height=HEIGHT, image=clubs_img)
    clubs.grid(row=0, column=2, padx=(5, 5), pady=(10, 5))

    # Add padding to diamonds
    diamonds_img = ImageTk.PhotoImage(Image.open(cards.get_diamonds()).resize((WIDTH, HEIGHT)))
    top_right.images.append(diamonds_img)  # Keep reference
    diamonds = Button(top_right, width=WIDTH, height=HEIGHT, image=diamonds_img)
    diamonds.grid(row=0, column=3, padx=(5, 5), pady=(10, 5))
    