import mysql.connector
from tkinter import messagebox

#Function to retrieve all available items in regards to a category

def listItems(categ):
    db = mysql.connector.connect(host="localhost", user="root", password="abcd1234", database="Pythonproj")
    curs = db.cursor()
    # code = 1022
    curs.execute("SELECT product_name FROM groceryInventory"
                 " WHERE category='{0}' ;".format(categ))
    result = curs.fetchall()
    db.commit()
    db.close()
    lst = []
    for x in result:
        lst.append(x[0])
    return (lst)

#Fucntion to check valididty of item added to cart and reduce quantity in databse by 1
def AddCartFun(name, quant):
    if name == 'Select' or quant == '0':
        messagebox.showerror(message="Please enter valid item details")
        return
    try:
        quant = int(quant)
    except:
        messagebox.showerror(message="Please enter valid quantity")
        return

    db = mysql.connector.connect(host="localhost", user="root", password="abcd1234", database="Pythonproj")
    curs = db.cursor()
    curs.execute("SELECT * FROM groceryInventory WHERE product_name='{0}' ;".format(name))
    result = curs.fetchall()
    db.commit()
    db.close()

    #print(result)

    qtavail = result[0][3]
    if qtavail < quant:
        messagebox.showerror(message="We do not have the required stock. Available stock is %s" % (qtavail,))
        return
    newqnt = qtavail - quant
    totalAmt = quant * result[0][4]

    db = mysql.connector.connect(host="localhost", user="root", password="abcd1234", database="Pythonproj")
    curs = db.cursor()
    curs.execute("UPDATE groceryInventory  SET qty_available = %s WHERE product_name='%s' ;"%(newqnt,name))
    mess="Your item {0} with product code {1} of quantity {2} costing a total of Rs.{3} has been added".format(name, result[0][0]
                                                                                                              ,quant,totalAmt)
    messagebox.showinfo(message=mess)
    db.commit()
    db.close()
    return [result[0][0],name,quant,totalAmt]
