from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x790+0+0")
        self.root.title("face Recognition System")

        title_lb1 = Label(self.root, text="Developer",
                          font=("times new roman", 25, "bold"), bg="green", fg="white")
        title_lb1.place(x=0, y=0, width=1280, height=35)

        img_bg = Image.open(r"college_images\developer_bg.jpg")
        img_bg = img_bg.resize((1280, 710), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_bg)
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=35, width=1280, height=710)


        # ------------------------------------------

        img = Image.open(r"college_images\developer_Per1.png")
        img = img.resize((150, 150), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=100, y=100, width=100, height=100)

        #frame
        title_lb1 = Label(text="Vedant Davhare\n",
                          font=("times new roman", 15),bg="white", fg="red")
        title_lb1.place(x=100, y=300, width=300, height=300)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
