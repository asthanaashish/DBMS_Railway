#this page will book tickets for you and return pnr
import mysql.connector
from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("MY BOOKING INFO PAGE")
root.geometry('1000x570')
my_connect = mysql.connector.connect(
    host="localhost",user="root",password="Ekansh@123",database="test2")
my_conn=my_connect.cursor()

my_img = ImageTk.PhotoImage(ImageTk.Image.open("images\\MY-BOOKING-INFO.png"))
img=Label(image=my_img)
img.place(x= 130,y= 0)







root.mainloop()