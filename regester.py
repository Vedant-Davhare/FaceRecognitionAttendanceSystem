from tkinter import *
from tkinter import ttk
from PIL import  ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1300x700+0+0")
        # ================Variables============
        self.var_faname = StringVar()
        self.var_iname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_password = StringVar()
        self.var_pcf = StringVar()
        self.var_check = IntVar()

        self.bg = ImageTk.PhotoImage(file=r"college_images/bg-reg.jpg")
        bg_lb1 = Label(self.root, image=self.bg)
        bg_lb1.place(x=0, y=0, relwidth=1, relheight=1)

        ##############################################################
        frame = Frame(self.root, bg="white")
        frame.place(x=300, y=100, width=800, height=501)

        register_lb1 = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="green", bg="white")
        register_lb1.place(x=20, y=20)
        ########################################
        fname = Label(frame, text="Frist Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=70)

        fname_entry = ttk.Entry(frame, textvariable=self.var_faname, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=100, width=250)

        lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        lname.place(x=400, y=70)

        self.lname_entry = ttk.Entry(frame, textvariable=self.var_iname, font=("times new roman", 15, "bold"))
        self.lname_entry.place(x=400, y=100, width=250)
        # -------------------------------------------------------

        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=145)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=175, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=400, y=145, width=250)
        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.txt_email.place(x=400, y=175, width=250)
        # ---------------------------------------------------

        security_Q = Label(frame, text="Select Security Questions", font=("times new roman", 15, "bold"), bg="white",
                           fg="black")
        security_Q.place(x=50, y=220)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15),
                                             state="read only")
        self.combo_security_Q["values"] = ("Select", "Birth Place", "Dob", "Pet Name", "friend Name")
        self.combo_security_Q.place(x=50, y=260, width="250")
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Select Security Answer", font=("times new roman", 15, "bold"), bg="white",
                           fg="black")
        security_A.place(x=400, y=220)
        self.txt_security_A = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15, "bold"))
        self.txt_security_A.place(x=400, y=260, width=250)

        # ---------------------------------------------------------

        passw = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        passw.place(x=50, y=300)
        self.txt_passw = ttk.Entry(frame, textvariable=self.var_password, font=("times new roman", 15, "bold"))
        self.txt_passw.place(x=50, y=340, width=250)

        pcf = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pcf.place(x=400, y=300)
        self.txt_pcf = ttk.Entry(frame, textvariable=self.var_pcf, font=("times new roman", 15, "bold"))
        self.txt_pcf.place(x=400, y=340, width=250)

        # ----------------------

        chebtn = Checkbutton(frame, variable=self.var_check, text="I Agree Terms & Condition", font=("times new roman", 12, "bold"),
                             onvalue=1, offvalue=0)
        chebtn.place(x=50, y=390)
        # ----------------------------------------------#
        btn1 = Button(frame, text="Register Now", font=20, bg="cyan", command=self.data)
        btn1.place(x=400, y=390)

        btn2 = Button(frame, text="Login", font=20, bg="cyan", command=self.return_login)
        btn2.place(x=600, y=390)


    # -------------------------------------------------

    def data(self):
        if self.var_faname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "select":
            messagebox.showerror("Error", "All field are required")
        elif self.var_password.get() != self.var_pcf.get():
            messagebox.showerror("Error", "Password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree our term and condition")
        else:
            con = mysql.connector.connect(host="localhost", username="root", password="vedant@9765",
                                                   database="face_recognizer")
            cur = con.cursor()
            query = ("select * from register where email = %s")
            value = (self.var_email.get())
            cur.execute(query, (value,))
            data = cur.fetchone()
            if data != None:
                messagebox.showerror("Error", "user already exist, please try another email")
            else:
                cur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (self.var_faname.get(),
                                                                                                 self.var_iname.get(),
                                                                                                 self.var_contact.get(),
                                                                                                 self.var_email.get(),
                                                                                                 self.var_securityQ.get(),
                                                                                                 self.var_securityA.get(),
                                                                                                 self.var_password.get()
                                                                                  ))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Registration Successful")

    def return_login(self):
        self.root.destroy()




if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()