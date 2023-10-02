import tkinter as tk
from tkinter import ttk

# Set up the window
window = tk.Tk()
window.title("ATM App")
mainScreen = tk.Frame(master=window, height=300, width=300)

mainScreen.columnconfigure(0, weight=1)
mainScreen.columnconfigure(1, weight=4)
mainScreen.columnconfigure(2, weight=4)
mainScreen.columnconfigure(3, weight=1)

username_label = ttk.Label(mainScreen, text="Username")
username_label.grid(column=2, row=2)

username_entry = ttk.Entry(mainScreen)
username_entry.grid(column=3, row=2)

password_label = ttk.Label(mainScreen, text="Password")
password_label.grid(column=2, row=3)

password_entry = ttk.Entry(mainScreen)
password_entry.grid(column=3, row=3)

keyPad = tk.Frame(master=window, background="grey")
keyPad.columnconfigure(0, weight=4)
keyPad.columnconfigure(1, weight=4)
keyPad.columnconfigure(2, weight=4)

one_button = ttk.Button(keyPad, text="1")
one_button.grid(column=0, row=1, sticky=tk.NW, padx=0, pady=0)

two_button = ttk.Button(keyPad, text="2")
two_button.grid(column=1, row=1, sticky=tk.N, padx=0, pady=0)

three_button = ttk.Button(keyPad, text="3")
three_button.grid(column=2, row=1, sticky=tk.NE, padx=0, pady=0)

four_button = ttk.Button(keyPad, text="4")
four_button.grid(column=0, row=2, sticky=tk.W, padx=0, pady=0)

five_button = ttk.Button(keyPad, text="5")
five_button.grid(column=1, row=2, sticky=tk.N, padx=0, pady=0)

six_button = ttk.Button(keyPad, text="6")
six_button.grid(column=2, row=2, sticky=tk.E, padx=0, pady=0)

seven_button = ttk.Button(keyPad, text="7")
seven_button.grid(column=0, row=3, sticky=tk.W, padx=0, pady=0)

eight_button = ttk.Button(keyPad, text="8")
eight_button.grid(column=1, row=3, sticky=tk.N, padx=0, pady=0)

nine_button = ttk.Button(keyPad, text="9")
nine_button.grid(column=2, row=3, sticky=tk.E, padx=0, pady=0)

back_button = ttk.Button(keyPad, text="<-")
back_button.grid(column=0, row=4, sticky=tk.SW, padx=0, pady=0)

zero_button = ttk.Button(keyPad, text="0")
zero_button.grid(column=1, row=4, sticky=tk.S, padx=0, pady=0)

enter_button = ttk.Button(keyPad, text="Enter")
enter_button.grid(column=2, row=4, sticky=tk.SE, padx=0, pady=0)

mainScreen.pack()


keyPad.pack()

# Run the application
window.mainloop()

