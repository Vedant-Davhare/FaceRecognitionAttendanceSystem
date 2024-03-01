import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recgnition import Face_Recgnition
from attendance import Attendance

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x790+0+0")
        self.root.title("face Recognition System")

        title_lb1 = Label(self.root, text="Help",
                          font=("times new roman", 25, "bold"), bg="green", fg="white")
        title_lb1.place(x=0, y=0, width=1280, height=35)

        img_top = Image.open(r"college_images\download.jpg")
        img_top = img_top.resize((1280, 290), Image.LANCZOS)
        self.photoimg_top \
            = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=35, width=1280, height=290)

        #frame
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=10, y=35, width=1250, height=525)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
