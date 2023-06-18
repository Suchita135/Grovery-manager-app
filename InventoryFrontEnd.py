from tkinter import *
from Inventory_Backend import *

#creating class
class frontInventory():


    # Initialization function
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.root.title('Grocery Inventory side')

        #Creating all lables
        self.label1 = Label(self.root, text="Pdt code")
        self.label1.grid(row=0, column=0)

        self.label2 = Label(self.root, text="Pdt Name")
        self.label2.grid(row=1, column=0)

        self.label3 = Label(self.root, text="Category")
        self.label3.grid(row=0, column=2)

        self.label4 = Label(self.root, text="Qty")
        self.label4.grid(row=1, column=2)

        self.label5 = Label(self.root, text="Price")
        self.label5.grid(row=0, column=4)

        #Creating entry fields
        self.code_text = IntVar()
        self.e1 = Entry(self.root, textvariable=self.code_text)
        self.e1.grid(row=0, column=1)

        self.name_text = StringVar()
        self.e2 = Entry(self.root, textvariable=self.name_text)
        self.e2.grid(row=1, column=1)

        options = ['Fruit and Veg', 'Dairy', 'Bakery', 'Packaged foods']
        self.cat_text = StringVar()
        self.cat_text.set('Select')
        self.e3 = OptionMenu(self.root, self.cat_text, *options)
        self.e3.grid(row=0, column=3)

        self.qty_text = StringVar()
        self.e4 = Entry(self.root, textvariable=self.qty_text)
        self.e4.grid(row=1, column=3)

        self.price_text = DoubleVar()
        self.e5 = Entry(self.root, textvariable=self.price_text)
        self.e5.grid(row=0, column=5)

        #Listbox to display items
        self.listDisplay = Listbox(self.root, height=8, width=50)
        self.listDisplay.grid(row=2, column=0, rowspan=8, columnspan=4)

        #scroll bar configured with list box
        self.scroll = Scrollbar(self.root)
        self.scroll.grid(row=2, column=4, rowspan=8)
        self.listDisplay.configure(yscrollcommand=self.scroll.set)
        self.scroll.configure(command=self.listDisplay.yview)

        # binding function to when listbox selection changes
        self.listDisplay.bind('<<ListboxSelect>>', self.getSelected)

        #Creating all buttons
        self.b1 = Button(self.root, text="View all", command=self.viewCommand)
        self.b1.grid(row=2, column=5)

        self.b2 = Button(self.root, text="Search Entry", command=self.searchCommand)
        self.b2.grid(row=3, column=5)

        self.b3 = Button(self.root, text="Add Entry", command=self.AddEntryCommand)
        self.b3.grid(row=4, column=5)

        self.b4 = Button(self.root, text="Update Entry", command=self.UpdateEntryCommand)
        self.b4.grid(row=5, column=5)

        self.b5 = Button(self.root, text="Delete Entry", command=self.DeleteEntryCommand)
        self.b5.grid(row=6, column=5)

        self.b6 = Button(self.root, text="Exit", command=self.ReturnInven)
        self.b6.grid(row=7, column=5)

    #functions for each button with backend functions called
    def viewCommand(self):
        self.listDisplay.delete(0, END)
        list = ViewAll()
        for x in range(0, len(list)):
            self.listDisplay.insert(x + 1, list[x])

    def searchCommand(self):
        self.listDisplay.delete(0, END)
        try:
            lis = Search_entry(self.e1.get(), self.e2.get())
            self.code_text.set("")
            self.name_text.set("")
            self.name_text.set("")
            self.cat_text.set("")
            self.qty_text.set("")
            self.price_text.set("")
        except:
            messagebox.showerror('SQL Error', 'Please enter valid inputs')

        if len(lis) == 0:
            messagebox.showinfo("Message", "Your search values didn't match any values")
            return

        for x in range(0, len(lis)):
            self.listDisplay.insert(x + 1, lis[x])

    def AddEntryCommand(self):
        AddEntry(self.e1.get(), self.e2.get(), self.cat_text.get(), self.e4.get(), self.e5.get())
        self.code_text.set("")
        self.name_text.set("")
        self.cat_text.set("")
        self.qty_text.set("")
        self.price_text.set("")
        self.viewCommand()

    def UpdateEntryCommand(self):
        try:
            index = self.listDisplay.curselection()[0]
            row = self.listDisplay.get(index)
            UpdateEntry(row[0], self.e2.get(), self.cat_text.get(), self.e4.get(), self.e5.get())
            self.listDisplay.delete(0, END)
            self.code_text.set("")
            self.name_text.set("")
            self.cat_text.set("")
            self.qty_text.set("")
            self.price_text.set("")
            self.viewCommand()
        except:
            messagebox.showerror('Error', 'Please select an item')

    def DeleteEntryCommand(self):
        try:
            index = self.listDisplay.curselection()[0]
            row = self.listDisplay.get(index)
            DeleteEntry(row[0])
            self.listDisplay.delete(0, END)
            self.code_text.set("")
            self.name_text.set("")
            self.cat_text.set("")
            self.qty_text.set("")
            self.price_text.set("")
            self.viewCommand()
        except:
            messagebox.showerror('Error', 'Please select an item')

    #List box selected function
    def getSelected(self, event):
        try:
            index = self.listDisplay.curselection()[0]
            row = self.listDisplay.get(index)
            self.code_text.set(row[0])
            self.name_text.set(row[1])
            self.cat_text.set(row[2])
            self.qty_text.set(row[3])
            self.price_text.set(row[4])
        except:
            pass

    def ReturnInven(self):
        op = messagebox.askyesno('Exit', "Are you sure you want to exit?")
        if op > 0:
            self.root.destroy()



if __name__ == "__main__":
    root = Tk()
    obj = frontInventory(root)
    root.mainloop()
