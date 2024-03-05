from tkinter import *
from PIL import Image, ImageTk
import webbrowser


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x790+0+0")
        self.root.title("face Recognition System")

        title_lb1 = Label(self.root, text="Developer",
                          font=("times new roman", 25, "bold"), bg="Black", fg="white")
        title_lb1.place(x=0, y=0, width=1280, height=35)

        img_bg = Image.open(r"college_images\About.png")
        img_bg = img_bg.resize((1280, 625), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_bg)
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=35, width=1280, height=625)

        # Twitter

        imgtwitter = Image.open(r"college_images\twitter.png")
        imgtwitter = imgtwitter.resize((50, 45), Image.LANCZOS)
        self.photoimgtwitter = ImageTk.PhotoImage(imgtwitter)

        b1 = Button(bg_img, image=self.photoimgtwitter, cursor="hand2", command=self.twitter)
        b1.place(x=1030, y=23, width=50, height=45)

        # Github

        imggithub = Image.open(r"college_images\github.jpg")
        imggithub = imggithub.resize((50, 45), Image.LANCZOS)
        self.photoimggithub = ImageTk.PhotoImage(imggithub)

        b1 = Button(bg_img, image=self.photoimggithub, cursor="hand2", command=self.github)
        b1.place(x=1103, y=23, width=50, height=45)

        # Linkedin

        imglinkedin = Image.open(r"college_images\linkedin.png")
        imglinkedin = imglinkedin.resize((50, 45), Image.LANCZOS)
        self.photoimglinkedin = ImageTk.PhotoImage(imglinkedin)

        b1 = Button(bg_img, image=self.photoimglinkedin, cursor="hand2", command=self.linkedin)
        b1.place(x=1168, y=23, width=50, height=45)

        # ==================Buttons=================

    def twitter(self):
        url = "https://x.com/DavhareVedant?t=opx8gQ8K_4YdtXYvN2H_5Q&s=08"
        webbrowser.open(url)

    def github(self):
        url = "https://github.com/Vedant-Davhare"
        webbrowser.open(url)

    def linkedin(self):
        url = "https://www.linkedin.com/in/vedant-davhare-b61b64227?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"
        webbrowser.open(url)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
