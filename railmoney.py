#fetch details only
import mysql.connector
from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("PNR ENQUIRY")
root.geometry('700x400')
my_connect = mysql.connector.connect(
    host="localhost",user="root",password="Ekansh@123",database="test2")
my_conn=my_connect.cursor()
#==============================================================================================>>>
my_img = ImageTk.PhotoImage(ImageTk.Image.open("images\\rail-money.png"))
img=Label(image=my_img)
img.place(x= 150,y= 0)

##########################################33333
def fetch_detail():
    root.destroy()
def back():
    root.destroy()
    from ekanshDBMS.venv import AfterLoginSuccess
#==============================================================================================>>>
back=Button(root,text="Back",command=back,bg='yellow').grid(row=11,column=1)

#==============================================================================================>>>
#==============================================================================================>>>

#vertical spacing trick
dateLabel=Label(root,text="   ",font=('courier')).grid(row=0,column=0)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=13,column=1)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=13,column=2)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=13,column=3)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=13,column=4)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=13,column=5)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=13,column=6)

dateLabel=Label(root,text="   ",font=('courier')).grid(row=8,column=0)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=9,column=0)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=11,column=0)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=12,column=0)
dateLabel=Label(root,text="   ",font=('courier')).grid(row=13,column=0)

#==============================================================================================>>>
root.mainloop()
