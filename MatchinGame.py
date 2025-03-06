import time
from tkinter import *
from random import randint

class ButtonWrapper:
    def __init__(self, id="", row=-1, col=-1, c=""):
        self.ID = id
        self.ROW = row
        self.COL = col
        self.COLOR = c
        self.BUTTON_OBJ = None

""" Check if two buttons have been clicked and if they are a match """
def check_match():
    global buttons
    clicked = [b for b in buttons.values() if b.BUTTON_OBJ['relief'] == "sunken"]
    
    if len(clicked) >= 2:
        if clicked[0].BUTTON_OBJ['bg'] == clicked[1].BUTTON_OBJ['bg']:
            # It's a match
            clicked[0].BUTTON_OBJ.configure(fg='black', bg='black', relief='raised')
            clicked[1].BUTTON_OBJ.configure(fg='black', bg='black', relief='raised')
        else:
            clicked[0].BUTTON_OBJ.configure(fg='SystemButtonFace', bg='SystemButtonFace', relief='raised')
            clicked[1].BUTTON_OBJ.configure(fg='SystemButtonFace', bg='SystemButtonFace', relief='raised')

""" If a button is pushed, draw the correct colors """
def button_pushed(pushed_id):
    global buttons
    buttons[pushed_id].BUTTON_OBJ.configure(bg=buttons[pushed_id].COLOR, relief="sunken")
    buttons[pushed_id].BUTTON_OBJ.after(1500, check_match)

def close_options(top):
    top.destroy()

""" Save the new Row and Col values to the global game variables """
def save_options(r, c):
    global rows, cols
    if (r * c) % 2 != 0:
        c += 1  # Ensure even number of tiles
    rows, cols = r, c
    reset_game()

""" Draw and handle the options menu """
def options():
    top = Toplevel(root)
    top.geometry("250x250")

    row_val, col_val = StringVar(), StringVar()

    Label(top, text="Rows:").pack()
    row = Entry(top, width=25, textvariable=row_val)
    row.pack()

    Label(top, text="Columns:").pack()
    col = Entry(top, width=25, textvariable=col_val)
    col.pack()

    save = Button(top, text="Save", command=lambda: save_options(int(row_val.get()), int(col_val.get())))
    close = Button(top, text="Close", command=lambda: close_options(top))
    save.pack(pady=5, side=TOP)
    close.pack(pady=5, side=TOP)

""" Reset the game with a properly paired grid """
def reset_game():
    global buttons, rows, cols

    if (rows * cols) % 2 != 0:
        cols += 1  # Ensure even number of total tiles

    # Clear previous buttons
    for b in buttons.values():
        b.BUTTON_OBJ.destroy()
    
    buttons = {}  # Clear button dictionary

    # Create new buttons
    for i in range(rows):
        for j in range(cols):
            id = (i * cols) + j
            b = ButtonWrapper(id=str(id), row=i, col=j)
            b.BUTTON_OBJ = Button(root, text="     ", command=lambda bid=b.ID: button_pushed(bid), height=3, width=7)
            buttons[b.ID] = b

    # Assign colors to tiles in pairs
    ids = list(range(rows * cols))
    while len(ids) > 1:
        a, b = ids.pop(randint(0, len(ids) - 1)), ids.pop(randint(0, len(ids) - 1))
        color = colors[randint(0, len(colors) - 1)]
        buttons[str(a)].COLOR = color
        buttons[str(b)].COLOR = color

    # Configure button display
    for b in buttons.values():
        b.BUTTON_OBJ.configure(fg='SystemButtonFace', bg='SystemButtonFace', relief='raised')
        b.BUTTON_OBJ.grid(row=b.ROW, column=b.COL)

""" Main Program Setup """
rows, cols = 5, 6
buttons = {}
root = Tk()
colors = ['red', 'green', 'blue', 'cyan', 'yellow', 'magenta']

menubar = Menu(root)
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='New Game', command=reset_game)
file.add_command(label='Options', command=options)
file.add_separator()
file.add_command(label='Exit', command=root.destroy)

root.config(menu=menubar)
reset_game()
root.mainloop()
