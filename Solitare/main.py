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
top_left = Frame(window, bg='black', width=500, height=110)  # Set explicit size
top_left.grid(row=0, column=0, columnspan=4)

top_right = Frame(window, bg='red', width=500, height=110)  # Set explicit size
top_right.grid(row=0, column=4, columnspan=4)

window.mainloop()