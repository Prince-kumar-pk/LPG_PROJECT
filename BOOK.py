from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from operator import itemgetter

class Book:
    def __init__(self,root):
        self.root=root
        self.root.title("LPG gas Booking")
        self.root.geometry("1295x550+78+180")




        # variables


        self.var_ref=StringVar()
        self.var_name = StringVar()
        self.var_Mname = StringVar()
        self.var_Fname = StringVar()
        self.var_Gender = StringVar()
        self.var_Pincode = StringVar()
        self.var_Mobile = StringVar()
        self.var_email = StringVar()
        self.var_IDP = StringVar()
        self.var_IDN = StringVar()
        self.var_address = StringVar()


        lbl_title = Label(self.root, text="LPG BOOKING SYSTEM", font=("times new roman", 30), bg="blue", fg="white",
                          bd=1)
        lbl_title.place(x=0, y=2, width=1295, height=50)


        lableframe=LabelFrame(self.root,bd=2,text="BOOKING",font=("times neew roman",12,"bold"),padx=2)
        lableframe.place(x=5,y=50,width=425,height=490)


#         --------------------

        labelframeleft = LabelFrame(self.root, bd=2, relief = RIDGE, text = "Customer Details", font = ("arial", 12, "bold"), padx = 2)
        labelframeleft.place(x =5, y=50, width=425, height=490)

        # ===================labels and entrys======================



        cust_ref = Label(labelframeleft, text="Type", font=("arial", 12, "bold"), padx=2, pady=6)
        cust_ref.grid(row=0, column=0, sticky=W)

        combo_ref = ttk.Combobox(labelframeleft,textvariable=self.var_ref, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_ref["value"] = ("select","12.5KG 1 cylender", "12.5KG -2 cylender")
        combo_ref.current(0)

        combo_ref.grid(row = 0, column=1)

        # cust name

        cname = Label(labelframeleft, font =("arial", 12, "bold"), text = "Customer Name : ", padx = 2, pady = 6)
        cname.grid(row =1,column = 0,sticky= W)

        txtcname = ttk.Entry(labelframeleft,textvariable=self.var_name, font =("arial", 13, "bold"), width=29)

        txtcname.grid(row = 1, column=1)

        # mother name


        lblmname = Label(labelframeleft, font=("arial", 12, "bold"), text="Mother Name: ", padx=2, pady=6)

        lblmname.grid(row =2, column=0, sticky= W)

        txtmname = ttk.Entry(labelframeleft,textvariable=self.var_Mname, font =("arial", 13, "bold"), width=29)

        txtmname.grid(row =2, column=1)

        lblmname = Label(labelframeleft, font=("arial", 12, "bold"), text="Father Name: ", padx=2, pady=6)

        lblmname.grid(row=3, column=0, sticky=W)

        txtmname = ttk.Entry(labelframeleft,textvariable=self.var_Fname, font=("arial", 13, "bold"), width=29)

        txtmname.grid(row=3, column=1)


        label_gender = Label(labelframeleft, font=("arial", 12, "bold"), text="Gender:", padx=2, pady=6)
        label_gender.grid(row = 4, column=0, sticky=W)

        combo_gender = ttk.Combobox(labelframeleft,textvariable=self.var_Gender, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_gender["value"] = ("select","Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=4, column=1)

        # postcode


        lblPostCode = Label(labelframeleft, font = ("arial", 12, "bold"), text="PostCode: ", padx=2, pady=6)

        lblPostCode.grid(row = 5, column=0, sticky=W)

        txtPostCode = ttk.Entry(labelframeleft,textvariable=self.var_Pincode, font = ("arial", 13, "bold"), width=29)

        txtPostCode.grid(row = 5, column=1)

        # mobilenumber


        lblMobile = Label(labelframeleft, font = ("arial", 12, "bold"), text="Mobile: ", padx=2, pady=6)

        lblMobile.grid(row=6, column=0, sticky=W)

        txtMobile = ttk.Entry(labelframeleft,textvariable=self.var_Mobile, font = ("arial", 13, "bold"), width=29)
        txtMobile.grid(row = 6, column=1)

        # email


        lblEmail = Label(labelframeleft, font=("arial", 12, "bold"), text="Email: ", padx=2, pady=6)

        lblEmail.grid(row=7, column=0, sticky=W)

        txtEmail = ttk.Entry(labelframeleft,textvariable=self.var_email, font = ("arial", 13, "bold"), width=29)
        txtEmail.grid(row =7,column = 1)

        label_gender = Label(labelframeleft, font=("arial", 12, "bold"), text="ID Proof:", padx=2, pady=6)
        label_gender.grid(row=8, column=0, sticky=W)

        combo_ID = ttk.Combobox(labelframeleft,textvariable=self.var_IDP, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_ID["value"] = ("select", "Addhar card", "Pasport","Voter ID","Student ID", "Other")
        combo_ID.current(0)
        combo_ID.grid(row=8, column=1)


        lblIDNo = Label(labelframeleft, font=("arial", 12, "bold"), text="ID Number: ", padx=2, pady=6)

        lblIDNo.grid(row=9, column=0, sticky=W)

        txtIDno = ttk.Entry(labelframeleft,textvariable=self.var_IDN, font=("arial", 13, "bold"), width=29)
        txtIDno.grid(row=9, column=1)

        lbladr = Label(labelframeleft, font=("arial", 12, "bold"), text="Address: ", padx=2, pady=6)
        lbladr.grid(row=10, column=0, sticky=W)

        txtaddress = ttk.Entry(labelframeleft,textvariable=self.var_address, font=("arial", 13, "bold"), width=29)
        txtaddress.grid(row=10, column=1)

        registerbtn = Button(labelframeleft,command=self.book_data, text="Book Now", bg='Green')
        registerbtn.place(x=40, y=400, height=40, width=100)

        details_table = LabelFrame(self.root,text=("View Booking Details"),font=("arial", 14, "bold"), bd=2, relief=RIDGE)
        details_table.place(x=430, y=50, width=860, height=490)
        cdetails_table = Frame(details_table, bd=2,relief=RIDGE)
        cdetails_table.place(x=0, y=10, width=860, height=490)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Booking_detail = ttk.Treeview(details_table, column=(
        "ref", "name", "mother","father", "gender", "post", "mobile", "email", "idproof", "idnumber", "address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)



        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side = RIGHT, fill=Y)

        scroll_x.config(command =self.Booking_detail.xview)
        scroll_y.config(command =self.Booking_detail.yview)

        self.Booking_detail.heading("ref",text="Type")
        self.Booking_detail.heading("name", text="Coustomar Name")
        self.Booking_detail.heading("mother", text="Mother Name")
        self.Booking_detail.heading("father", text="Father Name")
        self.Booking_detail.heading("gender", text="Gender")
        self.Booking_detail.heading("post", text="PinCode")
        self.Booking_detail.heading("mobile", text="Mobile")
        self.Booking_detail.heading("email", text="Email")
        self.Booking_detail.heading("idproof", text="ID proof")
        self.Booking_detail.heading("idnumber", text="ID No.")
        self.Booking_detail.heading("address", text="Address")

        self.Booking_detail["show"] = "headings"

        self.Booking_detail.column("ref",width=100)
        self.Booking_detail.column("name", width=100)
        self.Booking_detail.column("mother", width=100)
        self.Booking_detail.column("father", width=100)
        self.Booking_detail.column("gender", width=100)
        self.Booking_detail.column("post", width=100)
        self.Booking_detail.column("mobile", width=100)
        self.Booking_detail.column("email", width=100)
        self.Booking_detail.column("idproof", width=100)
        self.Booking_detail.column("idnumber", width=100)
        self.Booking_detail.column("address", width=100)

        self.Booking_detail.pack(fill=BOTH,expand=1)
        self.fetch()


    def book_data(self):
        if self.var_name.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error", "All Fields are requred")



        else:

            try:

                cn=mysql.connector.connect(host="localhost",username="root",password="P123456k@",database="lpg")
                cur=cn.cursor()


                cur.execute("insert into booking values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                   self.var_ref.get(),
                                                                                   self.var_name.get(),
                                                                                   self.var_Mname.get(),
                                                                                   self.var_Fname.get(),
                                                                                   self.var_Gender.get(),
                                                                                   self.var_Pincode.get(),
                                                                                   self.var_Mobile.get(),
                                                                                   self.var_email.get(),
                                                                                   self.var_IDP.get(),
                                                                                   self.var_IDN.get(),
                                                                                   self.var_address.get()
                ))
                cn.commit()
                cn.close()
                messagebox.showinfo("Success","Booked")
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}")

    def fetch(self):
        cn = mysql.connector.connect(host="localhost", username="root", password="P123456k@", database="lpg")
        cur = cn.cursor()

        cur.execute(f"select * from booking")
        rows=cur.fetchall()
        if len(rows) != 0:
            self.Booking_detail.delete(*self.Booking_detail.get_children())
            for i in rows:
                self.Booking_detail.insert("",END,values=i)
            cn.commit()
        cn.close()

if __name__ == '__main__':
    root=Tk()
    obj=Book(root)
    root.mainloop()
