from tkinter import *
from tkinter import ttk
from BillingBackend import *
from PIL import Image, ImageTk
import random
import os


class Bill_App:

    # Initialization function
    def __init__(self, root):
        super().__init__()
        self.root = root

        # image1
        img = Image.open('images/image3.png')
        img = img.resize((500, 130))
        self.photoimg = ImageTk.PhotoImage(img)

        lb_img = Label(self.root, image=self.photoimg)
        lb_img.place(x=0, y=0, width=500, height=130)

        # image2
        img1 = Image.open('images/image1.png')
        img1 = img1.resize((500, 130))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lb_img1 = Label(self.root, image=self.photoimg1)
        lb_img1.place(x=500, y=0, width=500, height=130)

        # image3
        img2 = Image.open('images/image2.png')
        img2 = img2.resize((500, 130))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lb_img2 = Label(self.root, image=self.photoimg2)
        lb_img2.place(x=1000, y=0, width=500, height=130)

        # all curr items
        self.ItemsInCart = []

        # variables (mobile no, customer, email id, )
        self.nameTextVar = StringVar()
        self.phoneNoTextVar = StringVar()
        self.email = StringVar()
        self.product = StringVar()

        self.search = StringVar()

        self.subTotTextVar = StringVar()
        self.taxTextVar = StringVar()
        self.totTextVar = StringVar()

        self.price = IntVar()
        self.quantity = IntVar()

        self.bill_noTextVar = IntVar()

        # background
        self.root.geometry('1300x800')
        self.root.title('Billing software - Sanya and Suchita')

        # title
        lbl_title = Label(self.root, text='BILLING SOFTWARE', font=('times new roman', 35, 'bold'), bg='white',
                          fg='red')
        lbl_title.place(x=0, y=130, width=1200, height=45)

        # frame under title
        self.Main_Frame = Frame(self.root, bd=5, relief=GROOVE, bg='white')
        self.Main_Frame.place(x=0, y=175, width=1530, height=620)

        # customer frame
        self.Cust_Frame = LabelFrame(self.Main_Frame, text='Customer', font=('times new roman', 12, 'bold'), bg='white',
                                     fg='red')
        self.Cust_Frame.place(x=0, y=5, width=350, height=140)

        # mobile no
        self.lbl_mob = Label(self.Cust_Frame, text='Mobile No', font=('times new roman', 12, 'bold'), bg='white',
                             fg='red')
        self.lbl_mob.grid(row=0, column=0, stick=W, padx=5, pady=2)

        # box to enter the mobile no
        self.entry_mob = ttk.Entry(self.Cust_Frame, font=('times new roman', 12, 'bold'), width=24,
                                   textvariable=self.phoneNoTextVar)
        self.entry_mob.grid(row=0, column=1)

        # customer name
        self.lbl_cus = Label(self.Cust_Frame, text='Customer Name', font=('times new roman', 12, 'bold'), bg='white',
                             fg='red')
        self.lbl_cus.grid(row=1, column=0, stick=W, padx=5, pady=2)

        # box to enter the customer name
        self.entry_cus = ttk.Entry(self.Cust_Frame, font=('times new roman', 12, 'bold'), width=24,
                                   textvariable=self.nameTextVar)
        self.entry_cus.grid(row=1, column=1)

        # email id
        self.lbl_em = Label(self.Cust_Frame, text='Email id', font=('times new roman', 12, 'bold'), bg='white',
                            fg='red')
        self.lbl_em.grid(row=2, column=0, stick=W, padx=5, pady=2)

        # box to enter the email id
        self.entry_em = ttk.Entry(self.Cust_Frame, font=('times new roman', 12, 'bold'), width=24,
                                  textvariable=self.email)
        self.entry_em.grid(row=2, column=1)

        # product frame- inside the main frame
        self.Prod_Frame = LabelFrame(self.Main_Frame, text='Product', font=('times new roman', 12, 'bold'), bg='white',
                                     fg='red')
        self.Prod_Frame.place(x=370, y=5, width=500, height=140)

        # category
        self.lbl_cat = Label(self.Prod_Frame, text='Select Categories', font=('times new roman', 10, 'bold'),
                             bg='white', fg='red')
        self.lbl_cat.grid(row=0, column=0, stick=W, padx=5, pady=2)

        OPTIONS = ['Select', 'Fruit and Veg', 'Dairy', 'Bakery', 'Packaged foods']
        self.clicked = StringVar()
        #self.clicked = StringVar(master=self.Prod_Frame)
        self.clicked.set(OPTIONS[0])  # default value
        self.clicked.trace("w", self.changed)
        self.drop = ttk.OptionMenu(self.Prod_Frame, self.clicked, *OPTIONS)
        self.drop.grid(row=0, column=1, stick=W, padx=5, pady=2)

        # product name
        self.lbl_product = Label(self.Prod_Frame, text='Product Name', font=('times new roman', 10, 'bold'), bg='white',
                                 fg='red')
        self.lbl_product.grid(row=1, column=0, stick=W, padx=5, pady=2)

        # quantity label
        self.lbl_q = Label(self.Prod_Frame, text='Quantity', font=('times new roman', 10, 'bold'), bg='white', fg='red')
        self.lbl_q.grid(row=2, column=0, stick=W, padx=5, pady=2)

        # quantity entry
        self.Qty_entry = ttk.Entry(self.Prod_Frame, font=('times new roman', 10, 'bold'), width=24, state='normal',
                                   textvariable=self.quantity)
        self.Qty_entry.grid(row=2, column=1, stick=W, padx=5, pady=2)

        # Bill
        self.Bill_Frame = LabelFrame(self.Main_Frame, text='Bill', font=('times new roman', 12, 'bold'), bg='white',
                                     fg='red')
        self.Bill_Frame.place(x=900, y=45, width=370, height=300)

        # scroll bar
        scroll_y = Scrollbar(self.Bill_Frame, orient=VERTICAL)
        self.textarea = Text(self.Bill_Frame, yscrollcommand=scroll_y.set, font=('times new roman', 12, 'bold'),
                             bg='white', fg='blue')
        scroll_y.pack(side=RIGHT, fill=Y)

        # join scroll bar and text
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # Bill counter
        self.Bottom_Frame = LabelFrame(self.Main_Frame, text='Bill Counter', font=('times new roman', 12, 'bold'),
                                       bg='white', fg='red')
        self.Bottom_Frame.place(x=0, y=370, width=1400, height=125)

        # sub total
        self.lbl_sub = Label(self.Bottom_Frame, text='Sub Total', font=('times new roman', 12, 'bold'), bg='white',
                             fg='red')
        self.lbl_sub.grid(row=0, column=0, stick=W, padx=5, pady=2)

        # box to enter the sub total
        self.entry_sub = ttk.Entry(self.Bottom_Frame, font=('times new roman', 12, 'bold'), width=24,
                                   textvariable=self.subTotTextVar)
        self.entry_sub.grid(row=0, column=1)

        # govt tax
        self.lbl_gov = Label(self.Bottom_Frame, text='Govt Tax', font=('times new roman', 12, 'bold'), bg='white',
                             fg='red')
        self.lbl_gov.grid(row=1, column=0, stick=W, padx=5, pady=2)

        # box to enter the govt tax
        self.entry_gov = ttk.Entry(self.Bottom_Frame, font=('times new roman', 12, 'bold'), width=24,
                                   textvariable=self.taxTextVar)
        self.entry_gov.grid(row=1, column=1)

        # total
        self.lbl_tot = Label(self.Bottom_Frame, text='Total', font=('times new roman', 12, 'bold'), bg='white',
                             fg='red')
        self.lbl_tot.grid(row=2, column=0, stick=W, padx=5, pady=2)

        # box to enter the total
        self.entry_tot = ttk.Entry(self.Bottom_Frame, font=('times new roman', 12, 'bold'), width=24,
                                   textvariable=self.totTextVar)
        self.entry_tot.grid(row=2, column=1)

        # Button Frame
        self.Btn_Frame = Frame(self.Bottom_Frame, bd=5, bg='white')
        self.Btn_Frame.place(x=320, y=0)

        # Add Button
        self.AddToCartBtn = Button(self.Btn_Frame, text='Add To Cart', command=self.AddingtoCart,
                                   font=('times new roman', 15, 'bold'), fg='red', height=5, width=15)
        self.AddToCartBtn.grid(row=0, column=0)

        # Generate Button
        self.GenerateBtn = Button(self.Btn_Frame, text='Generate Bill', font=('times new roman', 15, 'bold'),
                                  command=self.GenerateBill, fg='red', height=5, width=15, state=DISABLED)
        self.GenerateBtn.grid(row=0, column=1)

        # Save Button
        self.SaveBillBtn = Button(self.Btn_Frame, text='Save Bill', font=('times new roman', 15, 'bold'),
                                  command=self.SaveBill, fg='red', height=5, width=15, state=DISABLED)
        self.SaveBillBtn.grid(row=0, column=2)

        # Clear Button
        self.ClearBtn = Button(self.Btn_Frame, text='Clear', font=('times new roman', 15, 'bold'), command=self.Clear,
                               fg='red', height=5,
                               width=15)
        self.ClearBtn.grid(row=0, column=3)

        # Exit Button
        self.ExitBtn = Button(self.Btn_Frame, text='Exit', command=self.ReturnBill,
                              font=('times new roman', 15, 'bold'),
                              fg='red', height=5, width=15)
        self.ExitBtn.grid(row=0, column=4)

        # search bill
        Search_Frame = LabelFrame(self.Main_Frame, text='Customer', font=('times new roman', 12, 'bold'), bg='white',
                                  bd=2)
        Search_Frame.place(x=900, y=8, width=1400, height=40)

        # bill no
        self.lbl_bil = Label(Search_Frame, text='Bill no', font=('times new roman', 12, 'bold'), bg='red', fg='white')
        self.lbl_bil.grid(row=0, column=0, stick=W, )

        # enter bill no
        self.Search = ttk.Entry(Search_Frame, font=('times new roman', 10, 'bold'), width=24,
                                textvariable=self.bill_noTextVar)
        self.Search.grid(row=0, column=1, stick=W, padx=2, pady=2)

        # search button
        self.SBtn = Button(Search_Frame, text='Search', font=('times new roman', 15, 'bold'), command=self.Find_bill,
                           fg='red')
        self.SBtn.grid(row=0, column=20)

    # Function to restrict item dropdown on selecting category
    def changed(self, *args):
        if self.clicked.get() == 'Select':
            pass
        try:
            category = self.clicked.get()
            options = listItems(category)
            options.insert(0, "Select")
            self.categ_text = StringVar()
            self.categ_text.set(options[0])
            self.e3 = ttk.OptionMenu(self.Prod_Frame, self.categ_text, *options)
            self.e3.grid(row=1, column=1, stick=W, padx=5, pady=2)
            # print("You changed the selection. The new selection is " + self.clicked.get())
        except:
            pass

    # Adding items to internal list
    def AddingtoCart(self):
        self.textarea.delete(1.0, END)
        self.bill_noTextVar.set(0)
        prodName = self.categ_text.get()
        qtyAmt = self.Qty_entry.get()
        self.ItemsInCart.append(AddCartFun(prodName, qtyAmt))
        #print(self.ItemsInCart)
        self.categ_text.set('Select')
        self.clicked.set('Select')
        self.quantity.set(0)
        self.GenerateBtn['state'] = NORMAL

    # Generic function to get cust details
    def getCustomerDetails(self):
        if not (self.nameTextVar.get() and self.phoneNoTextVar.get() and self.email.get()):
            messagebox.showerror(message="Please enter customer details")
            return

        return self.nameTextVar.get(), self.phoneNoTextVar.get(), self.email.get()

    # Using added to cart items to generate bill with unique number and all customer details
    def GenerateBill(self):
        self.SaveBillBtn['state'] = NORMAL
        self.GenerateBtn['state'] = DISABLED
        self.AddToCartBtn['state'] = DISABLED

        z = random.randint(1000, 9999)

        file = open('UsedBillNos.txt', 'r')
        lstNos = file.read().split(",")

        while z in lstNos:
            z = random.randint(1000, 9999)

        file = open('UsedBillNos.txt', 'a+')
        file.write(str(z))
        file.write(",")
        file.close()

        cust_name, cust_phone, cust_mail = self.getCustomerDetails()
        self.bill_noTextVar.set(z)
        self.textarea.delete(1.0, END)
        self.textarea.insert(END, "\t\t Welcome to mart")
        self.textarea.insert(END, "\n Bill Number: {0} ".format(z))

        self.textarea.insert(END, "\n Customer Name: {0}".format(cust_name))
        self.textarea.insert(END, "\n Phone Number: {0}".format(cust_phone))
        self.textarea.insert(END, "\n Customer Email: {0}".format(cust_mail))

        self.textarea.insert(END, "\n===========================================")
        self.textarea.insert(END, "\n Products \t\t\t\tQTY\tPrice")
        self.textarea.insert(END, "\n===========================================")
        total = 0
        for x in self.ItemsInCart:
            self.textarea.insert(END, "\n{0}\t\t\t\t{1}\t{2}".format(x[1], x[2], x[3]))
            total += x[3]
        self.textarea.insert(END, "\n===========================================")
        tax = round(0.18 * total, 2)
        totalAfterTax = round(tax + total, 2)
        self.textarea.insert(END, "\nTotal:\t\t\t\tRs.{0}".format(total))
        self.textarea.insert(END, "\nTax(18%)\t\t\t\tRs.{0}".format(tax))
        self.textarea.insert(END, "\nPayable\t\t\t\tRs.{0}".format(totalAfterTax))
        self.textarea.insert(END, "\n===========================================")
        self.textarea.insert(END, "\nTHANK YOU FOR SHOPPING WITH US")
        self.subTotTextVar.set(total)
        self.taxTextVar.set(tax)
        self.totTextVar.set(totalAfterTax)

    # Function to save bill locally in txt file
    def SaveBill(self):
        self.SaveBillBtn['state'] = DISABLED
        op = messagebox.askyesno('Save Bill', "Are you sure you want to save?")
        if op > 0:
            bill_data = self.textarea.get(1.0, END)
            f = open('bill/' + str(self.bill_noTextVar.get()) + '.txt', 'w')
            f.write(bill_data)
            messagebox.showinfo('Saved', 'Bill No: {0} saved successfully'.format(self.bill_noTextVar.get()))
            f.close()
        self.Clear()

    # Function to retieve locally saved bills
    def Find_bill(self):
        try:
            int(self.bill_noTextVar.get())
        except:
            messagebox.showerror("Error", "Invalid Bill No")

        found = 'no'
        for i in os.listdir('bill/'):
            if int(i[0:4]) == int(self.bill_noTextVar.get()):
                f = open('bill/{0}'.format(i), 'r')
                self.textarea.delete(1.0, END)
                for d in f:
                    self.textarea.insert(END, d)
                f.close()
                found = 'yes'
        if found == 'no':
            messagebox.showerror("Error", "Invalid Bill No")

    # Clearing everything
    def Clear(self):
        op = messagebox.askyesno('Clear', "Are you sure you want to clear")
        if op > 0:
            self.nameTextVar.set("")
            self.phoneNoTextVar.set("")
            self.email.set("")
            self.subTotTextVar.set("")
            self.taxTextVar.set("")
            self.totTextVar.set("")
            self.textarea.delete(1.0, END)
            self.bill_noTextVar.set(0)
            self.ItemsInCart.clear()
            self.AddToCartBtn['state'] = NORMAL

    #
    def ReturnBill(self):
        op = messagebox.askyesno('Exit', "Are you sure you want to exit?")
        if op > 0:
            self.root.destroy()


if __name__ == '__main__':
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()
