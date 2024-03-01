import os
import tkinter
import tkinter.messagebox
from tkinter import *
from PIL import Image, ImageTk
from time import strftime
from student import Student
from train import Train
from face_recgnition import Face_Recgnition
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x790+0+0")
        self.root.title("Face Recognition System")

        #
        img = Image.open(r"college_images\MIT-logo-blue-background-1.png")
        img = img.resize((1280, 170), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1280, height=170)

        # bg image
        img3 = Image.open(r"college_images\bg1.jpg")
        img3 = img3.resize((1280, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=170, width=1280, height=710)

        title_lb1 = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
                          font=("times new roman", 30, "bold"), bg="white", fg="red")
        title_lb1.place(x=0, y=0, width=1280, height=45)

        # ==============Time===============
        def time():
            string = strftime('%H:%M:%S %p')
            lb1.config(text=string)
            lb1.after(1000, time)

        lb1 = Label(title_lb1, font=("times new roman", 10), bg="white", fg="blue")
        lb1.place(x=0, y=0, width=80, height=45)
        time()

        # student button
        img4 = Image.open(r"college_images\student_info.png")
        img4 = img4.resize((150, 150), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, cursor="hand2", command=self.student_details)
        b1.place(x=100, y=90, width=150, height=150)

        b1 = Button(bg_img, text="Student Details", cursor="hand2", font=("times new roman", 10, "bold"), bg="darkblue",
                    fg="white", command=self.student_details)
        b1.place(x=100, y=240, width=150, height=30)

        # Detect Face button
        img5 = Image.open(r"college_images\face_detection.png")
        img5 = img5.resize((150, 150), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.face_data)
        b1.place(x=400, y=90, width=150, height=150)

        b1 = Button(bg_img, text="Face Detector", cursor="hand2", font=("times new roman", 10, "bold"), bg="darkblue",
                    fg="white", command=self.face_data)
        b1.place(x=400, y=240, width=150, height=30)

        # Attendance face button
        img6 = Image.open(r"college_images\attendance_logo.png")
        img6 = img6.resize((150, 150), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.stud_attendance)
        b1.place(x=700, y=90, width=150, height=150)

        b1 = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 10, "bold"), bg="darkblue",
                    fg="white", command=self.stud_attendance)
        b1.place(x=700, y=240, width=150, height=30)

        # Help button
        img7 = Image.open(r"C:college_images\help.png")
        img7 = img7.resize((150, 150), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.std_help)
        b1.place(x=1000, y=90, width=150, height=150)

        b1 = Button(bg_img, text="Help Desk", cursor="hand2", font=("times new roman", 10, "bold"), bg="darkblue",
                    fg="white", command=self.std_help)
        b1.place(x=1000, y=240, width=150, height=30)

        # Train face button
        img8 = Image.open(r"college_images\traindata.png")
        img8 = img8.resize((150, 150), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.train_data)
        b1.place(x=100, y=290, width=150, height=150)

        b1 = Button(bg_img, text="Train Data", cursor="hand2", font=("times new roman", 10, "bold"), bg="darkblue",
                    fg="white", command=self.train_data)
        b1.place(x=100, y=440, width=150, height=30)

        # Photo Face Button
        img9 = Image.open(r"college_images\photo.jpg")
        img9 = img9.resize((150, 150), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.open_img)
        b1.place(x=400, y=290, width=150, height=150)

        b1 = Button(bg_img, text="Photo", cursor="hand2", font=("times new roman", 10, "bold"), bg="darkblue",
                    fg="white", command=self.open_img)
        b1.place(x=400, y=440, width=150, height=30)

        # Developer Button
        img10 = Image.open(r"college_images\developer.jpg")
        img10 = img10.resize((150, 150), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.std_dev)
        b1.place(x=700, y=290, width=150, height=150)

        b1 = Button(bg_img, text="Developer", cursor="hand2", font=("times new roman", 10, "bold"), bg="darkblue",
                    fg="white", command=self.std_dev)
        b1.place(x=700, y=440, width=150, height=30)

        # Exit Button
        img11 = Image.open(r"college_images\exit1.jpg")
        img11 = img11.resize((150, 150), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.iExit)
        b1.place(x=1000, y=290, width=150, height=150)

        b1 = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 10, "bold"), bg="darkblue",
                    fg="white", command=self.iExit)
        b1.place(x=1000, y=440, width=150, height=30)

    def open_img(self):
        os.startfile("data")

    # =====================================Functions buttos====================+

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recgnition(self.new_window)

    def stud_attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def std_dev(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def std_help(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    def iExit(self):
        self.exit = tkinter.messagebox.askyesno("Face Recognition", "Sure do you want to exit", parent=self.root)
        if self.exit == True:
            self.root.destroy()
        else:
            return False


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
