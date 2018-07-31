from tkinter import *
from tkinter import filedialog, messagebox
from itertools import cycle
from PIL import Image, ImageTk
from math import floor
import os, win32api, time

class Windows(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master = master
        self.browse_window()

    def browse_window(self):
        # Folder path to the folder containing users pictures
        self.folder_path = StringVar()

        # Create Objects
        Label(text="Select a folder containing your image files").pack(side=TOP, anchor=W, fill=X)
        Entry(width=50, state="disabled", text=self.folder_path).pack(side=LEFT, anchor=W)
        Button(text="Browse", command=self.find_folder).pack(side=LEFT, anchor=W)
        Button(text="Start Slide Show", comman=self.start).pack(side=BOTTOM, fill=X, anchor=W)

    def find_folder(self):
        # Allow user to select a directory and store it in global var called folder_path
        global folder_path
        try:
            filename = filedialog.askdirectory()
            self.folder_path.set(filename)
            directory = filename
        except:
            messagebox.showerror("Error", "There was an error opening " + filename + "\n")

    def start(self):
        if self.folder_path.get() == "":
            messagebox.showerror("Error", "Select your image folder before starting the slide show.")
        else:
            self.slide_window()

    def slide_window(self):
        slides = Toplevel()
        self.show()
        slides.title('SlideShow')
        picture_list = []

        extensions = ['.png', '.jpeg', '.bmp', '.jpg']
        for file in os.listdir(self.folder_path.get()):
            for extension in extensions:
                if file.endswith(extension):
                    picture_list.append(self.folder_path+"/"+file)
        if not picture_list:
            messagebox.showeror("Error", "no files with compatible extensions found in " + self.folder_path)
        else:
            self.images = cycle((PhotoImage(Image.open(pic)), pic)
                                for pic in picture_list)
            self.display = Label(self)
            self.display.pack()

    def show(self):
        next_im, im_name = next(self.images)
        self.display.config(image=next_im)
        self.title(im_name)
        self.after(self.delay, self.run)

# Window Created
root = Tk()

# Window size (half the users screen resolution by default)
#root.geometry(str(int(floor(win32api.GetSystemMetrics(0)/2))) + "x" + str(int(floor(win32api.GetSystemMetrics(1)/2))))
root.geometry("400x100")

# Instance creation and execution
app = Windows(root)
app.after()
app.mainloop()
