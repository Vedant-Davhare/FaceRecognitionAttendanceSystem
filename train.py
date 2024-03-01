from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import numpy as np
import mysql.connector
import cv2
import os



class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x790+0+0")
        self.root.title("face Recognition System")

        title_lb1 = Label(self.root, text="TRAIN DATA SET",
                          font=("times new roman", 30, "bold"), bg="coral", fg="mediumpurple")
        title_lb1.place(x=0, y=0, width=1280, height=60)

        img_top = Image.open(r"college_images\tu.jpg")
        img_top = img_top.resize((1280, 310), Image.LANCZOS)
        self.photoimg_top \
            = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=60, width=1280, height=310)

        b1 = Button(self.root, text="TRAIN DATA SET", cursor="hand2", font=("times new roman", 20, "bold"),
                    bg="yellowgreen",
                    fg="midnightblue", command=self.train_classifier)
        b1.place(x=0, y=320, width=1280, height=50)

        img_bottom = Image.open(r"college_images\td.jpg")
        img_bottom = img_bottom.resize((1280, 290), Image.LANCZOS)
        self.photoimg_bottom \
            = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=370, width=1280, height=290)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # Gray scale image
            imageNp = np.array(img, "uint8")
            id = int(os.path.split(image)[1].split(".")[1])

            faces.append((imageNp))
            ids.append(id)
            cv2.imshow("Training", imageNp)
            if  cv2.waitKey(1) == 13:
                break

        ids = np.array(ids)

        # ===================Train the classifier and save====================
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed...")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
