from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Generate UserName window")
root.geometry('700x300')
Label(root,text="User Id Creation Page").grid(row=0,column=1)
#====================================================>
#====================================================>
def confirm_check():
    checkbox_value=var.get()
    if(checkbox_value==1):
        password_check_1=e2.get()
        password_check_2=e3.get()
        if ((password_check_1==password_check_2)and (len(password_check_1))>0):
            messagebox.showinfo("success","All Done..Now Login")
            root.destroy()
        else:
            messagebox.showinfo("Try Again","passwords not matched")
    else:
        messagebox.askretrycancel("Failed","All feilds required")
#====================================================>
var = IntVar()
username=Label(root,text="Username",font="calibri",justify=LEFT).grid(row=1,column=0)
password=Label(root,text="Password",font="calibri",justify=LEFT).grid(row=2,column=0)
confirm=Label(root,text="Confirm Password",font="calibri",justify=LEFT).grid(row=3,column=0)
agreement=Checkbutton(root,text="Do you agree to terms and conditions of our policy*",variable=var,onvalue = 1,offvalue = 0)
agreement.grid(row=4,column=0)
#Label(root,text=var.get()).grid(row=4,column=2)
#====================================================>
b1=Button(root,text="Submit",bg='Light pink',font="sans-serif",width=10,command=confirm_check).grid(row=5,column=1)
#====================================================>
e1=Entry(root,width=40)
e1.grid(row=1,column=3)
e2=Entry(root,width=40)
e2.grid(row=2,column=3)
e3=Entry(root,width=40)
e3.grid(row=3,column=3)
#====================================================>
root.mainloop()


