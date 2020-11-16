# this page will be added onreset button of trail page which was called from package(main) module
# it will check user's email-id if matched it will allow to reset password
# import sql module and then validate
from tkinter import *
from tkinter import messagebox
import mysql.connector as sq
#========================================================================================>
root = Tk()
root.geometry('400x300')
root.title('RESET PAGE FOR VALID USERS')
Label(root,text='                ').grid(row=0,column=0)
Label(root,text='WELCOME TO RESET PAGE',font='orbitron',fg='red').grid(row=0,column=1)
#=========================================================================================>
conn = sq.connect(host="localhost",user="root",password="Ekansh@123",database="test2",auth_plugin='mysql_native_password')
cursor = conn.cursor()
#===========================================================================================>
# global username1
# global email1
# username1=''
# email1=''
def executor():
    emailId = emailId_input.get()
    #print("emailid"+str(len(emailId))+emailId)
    cursor.execute("select email from username where email='{}'".format(emailId))
    items = cursor.fetchall()
    if(items):
        #print("nacho bc")
        root.destroy()
        from ekanshDBMS.venv import resetor
        resetor.emailID=emailId
    #print(items)
    # for nm,pasd,email in items:
    #     #emaildb=email
    #     #print("emaildb" + str(len(email))+email)
    #     if(email==emailId):
    #     elif(email!=emailId):
    #         messagebox.showerror("error 404","hockerman")
#=========================================================================================>
def resetFUnc():
    #username=username_input.get()
    emailId=emailId_input.get()
    if(emailId==''):
        messagebox.showerror("Error","Enter Valid Email")
    else:
        executor()
    #edit here by validatng users from sql
#==========================================================================================>
# Label(root,text=' ').grid(row=1,column=0)
# Label(root,text='OR',font='calibri').grid(row=5,column=1)
# Label(root,text=' ').grid(row=7,column=0)
#enter email id or username you last remember
# username=Label(root,text='Username',font=('arial',15),fg='blue').grid(row=4,column=0)
emailId=Label(root,text="EMAIL_ID",font=('arial',15),fg='blue').grid(row=6,column=0)
# username_input=Entry(root,width=30)
# username_input.grid(row=4,column=1)
emailId_input=Entry(root,width=40)
emailId_input.grid(row=6,column=1)
reset=Button(root,text="CHECK FOR VALIDATIDTY",fg='white',bg='pink',command=resetFUnc,borderwidth=10).grid(row=8,column=1)
#==========================================================================================>
root.mainloop()