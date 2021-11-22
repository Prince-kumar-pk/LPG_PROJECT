from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import random


class Lpg:
    def __init__(self, root):
        self.root = root
        self.root.title("LPG")
        self.root.geometry("1000x520+0+0")

        ###################variable#################

        self.var_state = StringVar()
        self.var_District = StringVar()
        self.var_Distributer = StringVar()
        self.var_ID = StringVar()
        self.var_name = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()

        self.var_ID=random.randrange(0,200)

        # ##############1stimg##########

        frane1=Frame(self.root, bd=2, relief = RIDGE,bg="orange", padx = 2)
        frane1.place(x=5,y=10,width=300,height=500)

        img1 = Image.open(r"images.jpg")
        img1=img1.resize((80,50),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(frane1,image=self.photoimg1,bd=1,relief=RIDGE)
        lblimg.place(x=100,y=5,width=80,height=50)

        submit = Button(frane1, text="Booking LPG", bg='orange', command=self.booking)
        submit.place(x=20, y=150, height=40, width=200)





  # 2nd frame

        frame2=LabelFrame(self.root, bd=2, relief = RIDGE, text = "Resister for new LPG connection", font = ("arial",15), padx = 2)
        frame2.place(x=310, y=10, width=680, height=500)
# ***************
        label_state = Label(frame2, font=("arial", 12, "bold"), text="State:", padx=2, pady=6)
        label_state.grid(row=0, column=0, sticky=W)

        combo_state = ttk.Combobox(frame2,textvariable=self.var_state, font=("arial", 12, "bold"), width=27,state="readonly")
        combo_state["value"] = ("select", "Bihar")
        combo_state.current(0)
        combo_state.grid(row=0, column=1,padx=40)
        # ***************
        label_District = Label(frame2, font=("arial", 12, "bold"), text="District:", padx=2, pady=6)
        label_District.grid(row=2, column=0, sticky=W)

        combo_District = ttk.Combobox(frame2,textvariable=self.var_District, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_District["value"] = ("select", "Rohtas", "ARA", "Buxer","Patna","kaimur","other")
        combo_District.current(0)
        combo_District.grid(row=2, column=1, padx=40)

        # ***************
        label_distributor = Label(frame2, font=("arial", 12, "bold"), text="Distributor:", padx=2, pady=6)
        label_distributor.grid(row=3, column=0, sticky=W)

        combo_distributor = ttk.Combobox(frame2,textvariable=self.var_Distributer, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_distributor["value"] = ("select", "Indane Gas Agency", "pk Gas Agency", "Nikhil Gas Agency")
        combo_distributor.current(0)
        combo_distributor.grid(row=3, column=1, padx=40)

        # ***************
        label_ID = Label(frame2, font=("arial", 12, "bold"), text="Connection Id:", padx=2, pady=6)
        label_ID.grid(row=4, column=0, sticky=W)
        ID=ttk.Entry(frame2,textvariable=self.var_ID, width=27)
        ID.grid(row=4, column=1, padx=40)

        # ***************
        label_name = Label(frame2, font=("arial", 12, "bold"), text="Full Name:", padx=2, pady=6)
        label_name.grid(row=5, column=0, sticky=W)


        txtfname = ttk.Entry(frame2,textvariable=self.var_name,  font=("arial", 13, "bold"), width=27)
        txtfname.grid(row=5, column=1)


        label_number = Label(frame2, font=("arial", 12, "bold"), text="Mobile Number:", padx=2, pady=6)
        label_number.grid(row=7, column=0, sticky=W)
        txtfnumber = ttk.Entry(frame2,textvariable=self.var_mobile, font=("arial", 13, "bold"), width=27)
        txtfnumber.grid(row=7, column=1)

        #
        label_number = Label(frame2, font=("arial", 12, "bold"), text="Email ID:", padx=2, pady=6)
        label_number.grid(row=8, column=0, sticky=W)
        txtfnumber = ttk.Entry(frame2,textvariable=self.var_email, font=("arial", 13, "bold"), width=27)
        txtfnumber.grid(row=8, column=1)

        submit = Button(frame2, text="Submit", bg='Green',command=self.register_data)
        submit.place(x=40, y=300, height=40, width=100)


    def register_data(self):
        if self.var_name.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error","All fields are required")

        else:

            try:


                cn=mysql.connector.connect(host="localhost",username="root",password="P123456k@",database="lpg")
                cur=cn.cursor()
                cur.execute("insert into connection values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                   self.var_state.get(),
                                                                                   self.var_District.get(),
                                                                                   self.var_Distributer.get(),
                                                                                   self.var_ID,
                                                                                   self.var_name.get(),
                                                                                   self.var_mobile.get(),
                                                                                   self.var_email.get()


                ))
                cn.commit()
                cn.close()
                messagebox.showinfo("Succes","Register Successfuly")

            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}")



    def booking(self):
        self.root.destroy()
        from BOOK import Book
        root = Tk()
        ob = Book(root)
        root.mainloop()

if __name__ == '__main__':
    root =Tk()
    app=Lpg(root)
    root.mainloop()