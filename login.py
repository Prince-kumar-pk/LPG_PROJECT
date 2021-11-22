from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from operator import itemgetter
import mysql.connector


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("LPG Login")
        self.root.geometry("800x400+0+0")
        self.root.maxsize(800,400)

        # variable

        self.var_username = StringVar()
        self.var_pasword = StringVar()

        img1 = Image.open(r"1.jpg")
        img1 = img1.resize((800,400), Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(img1)


        lbl_bg = Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame = Frame(self.root,bg="white")
        frame.place(x=400,y=50,width=250,height=300)

        get_str=Label(frame,text="Login",font=("times new roman",20,"bold"),fg="red", bg="white")
        get_str.grid(row=0, column=1,padx=10)

        lblfrstrow = Label(frame,bg="white", text="Username: ",font=("times new roman",12) )
        lblfrstrow.place(x=20, y=70)

        Username = ttk.Entry(frame,textvariable=self.var_username, width=35)
        Username.place(x=100, y=70, width=100)

        lblsecrow = Label(frame,bg="white", text="Password: ",font=("times new roman",12))
        lblsecrow.place(x=20, y=100)

        password = ttk.Entry(frame,textvariable=self.var_pasword, width=35,show="*")
        password.place(x=100, y=100, width=100)

        submitbtn = Button(frame,command=self.conform, text="Login",
                              bg='blue')
        submitbtn.place(x=22, y=135, width=55)
        registerbtn = Button(frame, command=self.register, text="Resister", bg='Green')
        registerbtn.place(x=90, y=135,  width=120)



    def conform(self):
        if self.var_username.get()=="" or self.var_pasword.get()=="":
            messagebox.showerror("Error","All fields are required!")
        else:

            cn1 = mysql.connector.connect(host="localhost", username="root", password="P123456k@", database="lpg")
            cn2 = mysql.connector.connect(host="localhost", username="root", password="P123456k@", database="lpg")


            self.sqlc1="select email from register"
            self.sqlc2="select password from register"

            cu=cn1.cursor()
            cu.execute(self.sqlc1)
            cu1 = cn2.cursor()
            cu1.execute(self.sqlc2)

            email=self.var_username.get()
            password=self.var_pasword.get()

            em=[]
            ps=[]

            for i in cu:
                em.append(i)
            for j in cu1:
                ps.append(j)

            r1=list(map(itemgetter(0),em))
            r2=list(map(itemgetter(0),ps))
            k=len(r1)
            i=1
            while i<k:
                if r1[i]==email and r2[i]==password:
                    messagebox.showinfo("Success","Login done")
                    self.redirect_window()
                    break
                i+=1
            else:messagebox.showerror("Error","UserId or password not found")


    def redirect_window(self):
        self.root.destroy()

        from New_Connection import Lpg
        root = Tk()
        obj = Lpg(root)
        root.mainloop()

    def register(self):
        self.root.destroy()

        from register import Register
        root = Tk()
        obj = Register(root)
        root.mainloop()


if __name__ == '__main__':
    root =Tk()
    app=Login(root)
    root.mainloop()

