from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

import os

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("LPG New Connection")
        self.root.geometry("1000x600+0+0")
        # self.root.configure(bg="#93a49a")
        self.root.maxsize(1000, 600)

        img1 = Image.open(r"landing-bg.jpg")
        img1 = img1.resize((1000, 600), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(img1)

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # veriables

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pasword = StringVar()
        self.var_cnformpasw = StringVar()
        self.var_check = IntVar()



        frame = Frame(self.root, bg="gray").place(x=400, y=50, width=550, height=50)
        get_str = Label(frame, text="Register ", font=("times new roman", 30), fg="white", bg="gray")
        get_str.place(x=400, y=50)

        # -----------2nd frame----------

        frame1=Frame(self.root,bg="white").place(x=400,y=100,width=550,height=440)

        lblfname = Label(frame,bg="white",font=("times new roman",15), text="First Name:", )
        lblfname.place(x=410, y=130)

        self.fname = ttk.Entry(frame,textvariable=self.var_fname)
        self.fname.place(x=510, y=130, width=150)

        lblname = Label(frame, bg="white", font=("times new roman", 15), text="Last Name:", )
        lblname.place(x=680, y=130)

        self.lname = ttk.Entry(frame,textvariable=self.var_lname)
        self.lname.place(x=780, y=130, width=150)

        # ----------

        lblcon = Label(frame, bg="white", font=("times new roman", 12), text="Contact Number:", )
        lblcon.place(x=410, y=180)

        self.Contact_no = ttk.Entry(frame,textvariable=self.var_contact)
        self.Contact_no.place(x=520, y=180, width=150)

        lblem = Label(frame, bg="white", font=("times new roman", 15), text="Email:", )
        lblem.place(x=680, y=180)

        self.email = ttk.Entry(frame,textvariable=self.var_email)
        self.email.place(x=780, y=180, width=150)

        lblcombo = Label(frame, bg="white", font=("times new roman", 15), text="Security Qn:", )
        lblcombo.place(x=410, y=230)

        self.combo = ttk.Combobox(frame,textvariable=self.var_securityQ, state="readonly")
        self.combo["values"]=("select","Your Birth Place","Your Pet Name")
        self.combo.place(x=520,y=230)
        self.combo.current(0)

        lblcom = Label(frame, bg="white", font=("times new roman", 14), text="Security Ans:", )
        lblcom.place(x=680, y=230)

        self.comboAns = ttk.Entry(frame,textvariable=self.var_securityA, show="*")
        self.comboAns.place(x=790, y=230, width=150)

        lblpas = Label(frame, bg="white", font=("times new roman", 9), text="Password:" )
        lblpas.place(x=410, y=280)

        self.pasw = ttk.Entry(frame,textvariable=self.var_pasword, show="*")
        self.pasw.place(x=510, y=280, width=150)

        lblcpas = Label(frame, bg="white", font=("times new roman", 9), text="Confirm Password:" )
        lblcpas.place(x=680, y=280)

        self.cpasw = ttk.Entry(frame,textvariable=self.var_cnformpasw, show="*")
        self.cpasw.place(x=780, y=280, width=150)

        checkbtn=Checkbutton(frame,variable=self.var_check, text="I Agree to the prescribed Terms and Conditions*",font=("times new roman", 11),onvalue=1,offvalue=0)
        checkbtn.place(x=420,y=320)

        registerbtn = Button(frame,command=self.register_data, text="Register",bg='Green')
        registerbtn.place(x=600, y=380, height=40,width=120)
        registerbtn = Button(frame, command=self.redirect_window, text="Login", bg='red')
        registerbtn.place(x=750, y=380, height=40, width=120)



#         -------------------Functions------------

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pasword.get() != self.var_cnformpasw.get():
            messagebox.showerror("Error","Password & Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please click the agree button")
        else:

            try:


                cn=mysql.connector.connect(host="localhost",username="root",password="P123456k@",database="lpg")
                cur=cn.cursor()
                cur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                   self.var_fname.get(),
                                                                                   self.var_lname.get(),
                                                                                   self.var_contact.get(),
                                                                                   self.var_email.get(),
                                                                                   self.var_securityQ.get(),
                                                                                   self.var_securityA.get(),
                                                                                   self.var_pasword.get(),
                                                                                   self.var_cnformpasw.get(),

                ))
                cn.commit()
                cn.close()
                messagebox.showinfo("Succes","Register Successfuly")
                self.reset_fields()  # for stay window
                self.redirect_window()


            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}")



    def redirect_window(self):
        self.root.destroy()

        from login import Login
        root = Tk()
        obj = Login(root)
        root.mainloop()

    def reset_fields(self):
        self.email.delete(0,END)
        self.fname.delete(0, END)
        self.lname.delete(0, END)
        self.Contact_no.delete(0, END)
        self.combo.delete(0, END)
        self.comboAns.delete(0, END)
        self.cpasw.delete(0, END)
        self.pasw.delete(0, END)














if __name__ == '__main__':
    root=Tk()
    app=Register(root)
    root.mainloop()