from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
import mysql.connector
import cv2

class Face_Recgnition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x790+0+0")
        self.root.title("Face Recognition System")

        title_lb1 = Label(self.root, text="FACE RECOGNITION",
                          font=("times new roman", 25, "bold"), bg="green", fg="white")
        title_lb1.place(x=0, y=0, width=1280, height=35)

        # 1 image
        img_top = Image.open(r"college_images\fl.jpg")
        img_top = img_top.resize((640, 750), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=0, width=640, height=750)

        img_bottom = Image.open(r"college_images\fr.jpg")
        img_bottom = img_bottom.resize((640, 750), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=640, y=0, width=640, height=750)

        b1 = Button(self.root, text="Face Recognition", cursor="hand2", font=("times new roman", 10, "bold"),
                    bg="red", fg="white", command=self.face_recog)
        b1.place(x=300, y=450, width=150, height=40)

        exit_button = Button(self.root, text="Exit", cursor="hand2", font=("times new roman", 10, "bold"),
                             bg="red", fg="white", command=self.exit_program)
        exit_button.place(x=920, y=450, width=150, height=40)

    # ==============================Attendance=============================
    def mark_attendance(self, i, r, n, d):

        # now = datetime.now()
        # fd = now.strftime("%d/%m/%Y")
        # with open(fd+".csv", "a", newline="\n") as f:

        with open("ved.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = [entry.split(",")[0] for entry in myDataList]

            if (i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    # ===========Face Recognition=======================
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="vedant@9765",
                                               database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name, Roll, Dep FROM student WHERE Student_id=%s", (id,))

                result = my_cursor.fetchone()

                if result is not None:  # Check if result is not None before unpacking
                    name, roll, dep = result
                    cv2.putText(img, f"ID:{id}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{roll}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{dep}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(id, roll, name, dep)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, y]

            return coord

        # def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
        #     gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #     features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
        #
        #     coord = []
        #
        #     for (x, y, w, h) in features:
        #         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        #         id, predict = clf.predict(gray_image[y:y + h, x:x + w])
        #         confidence = int((100 * (1 - predict / 300)))
        #
        #         conn = mysql.connector.connect(host="localhost", username="root", password="vedant@9765",
        #                                        database="face_recognizer")
        #         my_cursor = conn.cursor()
        #
        #         my_cursor.execute("SELECT Name, Roll, Dep FROM student WHERE Student_id=%s", (id,))
        #
        #         result = my_cursor.fetchone()
        #
        #         if confidence > 80:
        #             name, roll, dep = result
        #             cv2.putText(img, f"ID:{id}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
        #             cv2.putText(img, f"Roll:{roll}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
        #             cv2.putText(img, f"Name:{name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
        #             cv2.putText(img, f"Department:{dep}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
        #             self.mark_attendance(id, roll, name, dep)
        #         else:
        #             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
        #             cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
        #
        #         coord = [x, y, w, y]
        #
        #     return coord

        def recognize(img, clf, face_cascade):

            cord = draw_boundary(img, face_cascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        address="http://100.74.87.230:8080//video"
        video_cap.open(address)
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, face_cascade)
            cv2.imshow("Welcome To Face Recognition", img)

            # Break the loop on 'Enter' key (key code 13)
            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

    def exit_program(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recgnition(root)
    root.mainloop()