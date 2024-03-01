from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from main import Face_Recognition_System
from regester import Register



def main():
    win = Tk()
    app = LoginWindow(win)
    win.mainloop()


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.root.title("Creative Login Page")

        # ================Variables============
        self.var_email = StringVar()
        self.var_password = StringVar()

        # Background Image (Subtle Gradient)
        gradient_img = Image.new("RGB", (600, 400), "#009688")  # Green color
        self.gradient_photo = ImageTk.PhotoImage(gradient_img)
        gradient_label = Label(self.root, image=self.gradient_photo)
        gradient_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Title
        title_label = Label(self.root, text="Welcome to Our System", font=("Helvetica", 20, "bold"), fg="white",
                            bg="#009688")
        title_label.pack(pady=20)

        # Frame
        frame = Frame(self.root, bg="white", bd=10)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Username Label and Entry
        username_lbl = Label(frame, text="Username", font=("Arial", 12), fg="#333", bg="white")
        username_lbl.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.txtuser = ttk.Entry(frame, font=("Arial", 12))
        self.txtuser.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Password Label and Entry
        password_lbl = Label(frame, text="Password", font=("Arial", 12), fg="#333", bg="white")
        password_lbl.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.txtpass = ttk.Entry(frame, show="*", font=("Arial", 12))
        self.txtpass.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # Login Button
        loginbtn = Button(frame, text="Login", font=("Arial", 12, "bold"),
                          bd=3, relief=RIDGE, fg="white", bg="#009688",
                          activeforeground="white", activebackground="#004D40", command=self.login)
        loginbtn.grid(row=2, column=0, columnspan=2, pady=20)

        # Register Button
        registerbtn = Button(frame, text="New User Register", font=("Arial", 10, "bold"),
                             bd=3, relief=RIDGE, fg="white", bg="#004D40",
                             activeforeground="white", activebackground="#009688", command=self.rigister_window)
        registerbtn.grid(row=3, column=0, columnspan=2, pady=10)

        # Forget Password Button
        forget_pass_btn = Button(frame, text="Forget Password", font=("Arial", 10, "bold"),
                                 bd=3, relief=RIDGE, borderwidth=0, fg="white", bg="#004D40",
                                 activeforeground="white", activebackground="#009688", command=self.forget_password)
        forget_pass_btn.grid(row=4, column=0, columnspan=2, pady=10)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "user" and self.txtpass.get() == "password":
            messagebox.showinfo("Success", "Welcome to Our System")
        else:
            con = mysql.connector.connect(host="localhost", username="root", password="vedant@9765",
                                          database="face_recognizer")
            cur = con.cursor()
            cur.execute("select * from register where email=%s and password=%s",
                        (
                            self.txtuser.get(),
                            self.txtpass.get()
                        ))
            row = cur.fetchone()

            if row == None:
                messagebox.showerror("Error", "Invalid username and password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access only admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            con.commit()
            con.close()

    # ============Reset password==============
    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select the security Question", parent=self.root2)
        elif self.txt_security_A.get() == "":
            messagebox.showerror("Error", "Please Enter Answer", parent=self.root2)
        elif self.txt_new_pass.get() == "":
            messagebox.showerror("Error", "Please Enter new password", parent=self.root2)
        else:
            con = mysql.connector.connect(host="localhost", username="root", password="vedant@9765",
                                          database="face_recognizer")
            cur = con.cursor()
            query = ("select * from register where email=%s and securityQ=%s and securityA=%s ")
            value = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security_A.get())
            cur.execute(query, value)
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please enter correct Answer", parent=self.root2)

            else:
                query = ("update register set password=%s where email=%s")
                value = (self.txt_new_pass.get(), self.txtuser.get())
                cur.execute(query, value)
                con.commit()
                con.close()
                messagebox.showinfo("Info", "Your password has been reset ,please login new password",
                                    parent=self.root2)
                self.root2.destroy()

    # ============Forget password==============
    def forget_password(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please Enter the Email address to reset password")
        else:
            con = mysql.connector.connect(host="localhost", username="root", password="vedant@9765",
                                          database="face_recognizer")
            cur = con.cursor()
            query = ("select * from register where email=%s")
            value = (self.txtuser.get())
            print(value)
            cur.execute(query, (value,))
            row = cur.fetchone()
            con.commit()
            con.close()
            # print(row)

            if row == None:
                messagebox.showerror("Error", "Please enter valid user name")
            else:
                con.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                l = Label(self.root2, text="Forget Password", font=("Helvetica", 20, "bold"), fg="white",
                          bg="#009688")
                l.place(x=0, y=0, relwidth=1)

                security_Q = Label(self.root2, text="Select Security Questions", font=("times new roman", 15, "bold"),
                                   bg="white",
                                   fg="black")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2,
                                                     font=("times new roman", 15),
                                                     state="read only")
                self.combo_security_Q["values"] = ("Select", "Birth Place", "Dob", "Pet Name", "friend Name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Select Security Answer", font=("times new roman", 15, "bold"),
                                   bg="white",
                                   fg="black")
                security_A.place(x=50, y=150)
                self.txt_security_A = ttk.Entry(self.root2,
                                                font=("times new roman", 15, "bold"))
                self.txt_security_A.place(x=50, y=180, width=250)

                # =======New Pass=====

                new_pass = Label(self.root2, text="Enter New Password", font=("times new roman", 15, "bold"),
                                 bg="white",
                                 fg="black")
                new_pass.place(x=50, y=220)
                self.txt_new_pass = ttk.Entry(self.root2,
                                              font=("times new roman", 15, "bold"))
                self.txt_new_pass.place(x=50, y=250, width=250)

                # ========confirm pass========
                # con_pass = Label(self.root2, text="confirm New Password", font=("times new roman", 15, "bold"),
                #                  bg="white",
                #                  fg="black")
                # con_pass.place(x=50, y=220)
                # self.txt_con_pass = ttk.Entry(self.root2,
                #                               font=("times new roman", 15, "bold"))
                # self.txt_con_pass.place(x=50, y=250, width=250)
                #
                #
                btn = Button(self.root2, text="Reset", font=("times new roman", 15, "bold"), fg="red", bg="white",
                             command=self.reset_pass)
                btn.place(x=150, y=290)

    def rigister_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)


if __name__ == "__main__":
    main()
