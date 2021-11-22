from tkinter import *
from PIL import Image,ImageTk

class main:
    def __init__(self,root):
        self.root=root

        self.root.title("LPG ")
        self.root.geometry("550x300")
        self.root.maxsize(550,300)

        img1 = Image.open(r"landing-bg.jpg")
        img1 = img1.resize((550, 300), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(img1)

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        lbl_title = Label(self.root, text="New LPG connection and LPG booking system", font=("times new roman", 20), bg="gray", fg="white",
                          bd=1)
        lbl_title.place(x=10, y=2, width=520, height=50)

        registerbtn = Button(self.root,command=self.login,  text="Login", bg='Green')
        registerbtn.place(x=60, y=100, height=40, width=120)
        registerbtn = Button(self.root,command=self.register, text="Register", bg='Blue')
        registerbtn.place(x=300, y=100, height=40, width=120)
    def login(self):
        self.root.destroy()

        from login import Login
        root = Tk()
        obj = Login(root)
        root.mainloop()

    def register(self):
        self.root.destroy()

        from register import Register
        root = Tk()
        obj = Register(root)
        root.mainloop()




if __name__ == '__main__':
    root = Tk()
    app = main(root)
    root.mainloop()
