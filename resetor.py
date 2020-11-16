from tkinter import *
from tkinter import messagebox
import mysql.connector as sq
#============================================================>>
root=Tk()
root.title("change your password")
root.geometry('700x400')
global emailID
print("emailid"+str(len(emailId))+emailId)
#===========================================================>>
conn = sq.connect(host="localhost",user="root",password="Ekansh@123",database="test2",auth_plugin='mysql_native_password')
cursor = conn.cursor()
#============================================================>>
def executor():
    #emailId = emailId_input.get()
    pass
    # cursor.execute("select email from username where email='{}'".format(emailId))
    # items = cursor.fetchall()
    # if(items):
    #     pass
#=============================================================>>
#enter pass

#=============================================================>>
root.mainloop()