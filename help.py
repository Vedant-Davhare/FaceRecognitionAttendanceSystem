from tkinter import *
from PIL import Image, ImageTk


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x790+0+0")
        self.root.title("face Recognition System")

        title_lb1 = Label(self.root, text="Help",
                          font=("times new roman", 25, "bold"), bg="Black", fg="red")
        title_lb1.place(x=0, y=0, width=1280, height=35)

        img_top = Image.open(r"college_images\help (2).png")
        img_top = img_top.resize((1280, 625), Image.LANCZOS)
        self.photoimg_top \
            = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=35, width=1280, height=625)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
