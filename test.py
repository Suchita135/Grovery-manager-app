import mysql.connector


def Add():
    vals = input("Enter values seperated by comma: ")
    try:
        a, b, c, d, e, f = vals.split(",")
        db = mysql.connector.connect(host="localhost", user="root", password="abcd1234", database="Pythonproj")
        curs = db.cursor()

        curs.execute("INSERT INTO PLAYERS VALUES (%s,%s,'%s','%s','%s',%s);" % (a, b, c, d, e, f))
        db.commit()
        db.close()


    except:
        print('Error')
        return


def Delete():
    ID = input("Enter player ID: ")
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="abcd1234", database="Pythonproj")
        curs = db.cursor()
        curs.execute("DELETE FROM PLAYERS WHERE PLAYER_ID=%s;"%(ID))
        db.commit()
        db.close()
    except:
        print('Error')
        return


def Display():
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="abcd1234", database="Pythonproj")
        curs = db.cursor()
        curs.execute("SELECT * FROM PLAYERS;")
        result = curs.fetchall()
        for x in result:
            print(x)
        db.commit()
        db.close()
    except:
        print('Error')
        return



def Search():
    n = input("Enter player name: ")
    try:
        db = mysql.connector.connect(host="localhost", user="root", password="abcd1234", database="Pythonproj")
        curs = db.cursor()
        curs.execute("SELECT * FROM PLAYERS WHERE PLAYER_N= '%s';"%(n))
        result = curs.fetchall()
        db.commit()
        db.close()
    except:
        print('Error')
        return
    for x in result:
        print(x)


def modify():
    ID = input("Enter player ID: ")
    try:
        team = input("Enter player team to change to: ")
        db = mysql.connector.connect(host="localhost", user="root", password="abcd1234", database="Pythonproj")
        curs = db.cursor()
        curs.execute("UPDATE PLAYERS SET TEAM='%s' WHERE PLAYER_ID=%s;"% (team, ID))
        db.commit()
        db.close()
    except:
        print('Error')
        return


while True:
    inp = input("Enter space to break or anything else to cont: ")
    if inp == " ":
        break
    else:
        print(" 1.Add entry \n 2.Delete entry \n 3.Display All \n 4.Search \n 5.Modify ")
        answ = input("Enter: ")
        if answ == '1':
            Add()
        elif answ == '2':
            Delete()
        elif answ == '3':
            Display()
        elif answ == '4':
            Search()
        elif answ == '5':
            modify()
        else:
            print('Invalid')
            continue
