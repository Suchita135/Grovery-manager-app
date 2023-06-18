from tkinter import *

import PIL as pl
from InventoryFrontEnd import *
from BillingFrontEnd import *


# making the class
class App():

    def __init__(self, root):
        super().__init__()
        self.root = root
        self.root.title('Home Page')
        self.root.geometry("805x450")

        self.img = pl.Image.open('images/image.png')
        self.bg = pl.ImageTk.PhotoImage(self.img)

        self.label = Label(self.root, image=self.bg)
        self.label.place(x=0, y=0)

        self.label1 = Label(self.root, text="Welcome to the homepage!", font=("Arial", 65))
        self.label1.grid(row=0, column=1)

        self.label2 = Label(self.root, text="Grocery Store Software", font=("Arial", 30))
        self.label2.grid(row=1, column=1)

        self.b1 = Button(self.root, text="Bill a purchase", command=self.billingWindow, height=5, width=35)
        self.b1.grid(row=2, column=1)

        self.b2 = Button(self.root, text="Inventory Management", command=self.inventoryWindow, height=5, width=35)
        self.b2.grid(row=3, column=1)

    # open billing window function
    def billingWindow(self):
        self.new_window = Toplevel(self.root)
        Bill_App(self.new_window)
        # self.app = Bill_App(self.new_window)

    # open inventory window function
    def inventoryWindow(self):
        self.new_window = Toplevel(self.root)
        frontInventory(self.new_window)
        # self.app = frontInventory(self.new_window)


# creating instance of the class if main.py running
if __name__ == "__main__":
    root = Tk()
    obj = App(root)
    root.mainloop()
