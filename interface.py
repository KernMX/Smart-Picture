from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from math import floor

import os, sys, argparse, json, colorsys, win32api

class Window(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        # Giving the window a title
        self.master.title("Smart Picture")

        # create the widgets shown in the GUI
        self.create_widgets()

    # Widget Creation
    def create_widgets(self):
        self.create_menu()
        self.create_radios()
        self.image_browser()

    # Individual Widget type Creation
    def create_radios(self):
        # Create Objects
        self.normal = Radiobutton(text="Normal", value=1)
        self.pixel_art = Radiobutton(text="Pixel Art", value=2)
        label = Label(text="Select a conversion type")

        # Place Objects
        label.grid(column=0, row=0, columnspan=2)
        self.normal.grid(column=0, row=1)
        self.pixel_art.grid(column=1, row=1)


    def image_browser(self):
        # Folder path to the folder containing users pictures
        self.folder_path = StringVar()

        # Create Objects
        self.pathtxt = Entry(width=50, state="disabled", text=self.folder_path)
        self.browse = Button(text="Browse", command=self.find_folder)
        label = Label(text="Select a folder containing your image files")

        # Place Objects
        label.grid(column=4, row=0, columnspan=2)
        self.pathtxt.grid(column=5, row=1)
        self.browse.grid(column=4, row=1)

    def create_menu(self):
        # Create the menu
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # Create the menu items
        Start = Menu(menu)
        Exit = Menu(menu)

        # Add commands to our menu options
        Start.add_command(label="Start", command=self.Begin)
        Exit.add_command(label="Exit", command=self.Quit)

        # Add in options and commands for the menu d
        menu.add_cascade(label="Start", menu=Start)
        menu.add_cascade(label="Exit", menu=Exit)

    def image_canvas():
        return

    # Commands for window widgets
    # Application Quit
    def Quit(self):
        exit()

    def Begin(self):
        self.image_canvas()

        extensions = ('.png', '.jpeg', '.bmp')
        text = Label(self, text="Starting")

    def find_folder(self):
        # Allow user to select a directory and store it in global var called folder_path
        global folder_path
        try:
            filename = filedialog.askdirectory()
            self.folder_path.set(filename)
        except:
            messagebox.showerror("Error", "There was an error opening " + filename + "\n")

# Window Created
root = Tk()

# Window size (half the users screen resolution by default)
root.geometry(str(int(floor(win32api.GetSystemMetrics(0)/2))) + "x" + str(int(floor(win32api.GetSystemMetrics(1)/2))))

# Instance creation and execution
app = Window(root)
app.mainloop()
