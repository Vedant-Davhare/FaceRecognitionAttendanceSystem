from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x790+0+0")
        self.root.title("Face Recognition System")

        # ==========================varaibles===============
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        #
        img = Image.open(r"college_images\sa.jpg")
        img = img.resize((1280, 150), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1280, height=150)


        title_lb1 = Label(self.root, text="Student Attendance Details",
                          font=("times new roman", 30, "bold"), bg="lightcyan", fg="saddlebrown")
        title_lb1.place(x=0, y=150, width=1280, height=40)

        img3 = Image.open(r"college_images\bg.jpg")
        img3 = img3.resize((1280, 710), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=190, width=1280, height=710)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=15, width=1250, height=500)

        # Left Side Frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Studet Information",
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=625, height=500)

        img_left = Image.open(r"college_images\ati.jpg")
        img_left = img_left.resize((600, 150), Image.LANCZOS)
        self.photoimg_left \
            = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=600, height=150)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=5, y=160, width=600, height=300)

        # Lable entry
        # attendance_id
        attendance_label = Label(left_inside_frame, text="AttendanceId:", font=("times new roman", 10, "bold"),
                                 bg="white")
        attendance_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendance_entry = ttk.Entry(left_inside_frame, width=20,
                                     font=("times new roman", 10, "bold"), textvariable=self.var_atten_id)
        attendance_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Roll No
        roll_label = Label(left_inside_frame, text="Roll No:", font=("times new roman", 10, "bold"),
                           bg="white", )
        roll_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        roll_entry = ttk.Entry(left_inside_frame, width=20,
                               font=("times new roman", 10, "bold"), textvariable=self.var_atten_roll)
        roll_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Name
        name_label = Label(left_inside_frame, text="Name:", font=("times new roman", 10, "bold"),
                           bg="white")
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        name_entry = ttk.Entry(left_inside_frame, width=20,
                               font=("times new roman", 10, "bold"), textvariable=self.var_atten_name)
        name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Department
        dep_label = Label(left_inside_frame, text="Department:",
                          font=("times new roman", 10, "bold"), bg="white")
        dep_label.grid(row=1, column=2, padx=10,pady=5, sticky=W)

        dep_entry = ttk.Entry(left_inside_frame, width=20,
                              font=("times new roman", 10, "bold"), textvariable=self.var_atten_dep)
        dep_entry.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Time
        time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 10, "bold"),
                           bg="white")
        time_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        time_entry = ttk.Entry(left_inside_frame, width=20,
                               font=("times new roman", 10, "bold"), textvariable=self.var_atten_time)
        time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Date
        date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 10, "bold"),
                           bg="white")
        date_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        date_entry = ttk.Entry(left_inside_frame, width=20,
                               font=("times new roman", 10, "bold"), textvariable=self.var_atten_date)
        date_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Attendance Status
        atten_label = Label(left_inside_frame, text="Attendance Status:",
                            font=("times new roman", 11, "bold"), bg="white")
        atten_label.grid(row=3, column=0, padx=10, sticky=W)

        atten_entry = ttk.Entry(left_inside_frame, width=20,
                                font=("times new roman", 10, "bold"), textvariable=self.var_atten_attendance)
        atten_entry.grid(row=3, column=1, padx=2, pady=10, sticky=W)

        # buttons frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=170, width=595, height=30)

        # save
        import_btn = Button(btn_frame, text="Import csv", width=20, font=("times new roman", 10, "bold"), bg="blue",
                            fg="white", command=self.importCsv
                            )
        import_btn.grid(row=0, column=0)

        # update
        export_btn = Button(btn_frame, text="Export csv", width=20, font=("times new roman", 10, "bold"), bg="blue",
                            fg="white", command=self.exportCsv)
        export_btn.grid(row=0, column=1)

        # delete
        update_btn = Button(btn_frame, text="Update csv", width=20, font=("times new roman", 10, "bold"), bg="blue",
                            fg="white")
        update_btn.grid(row=0, column=2)

        # reset
        reset_btn = Button(btn_frame, text="Reset", width=20, font=("times new roman", 10, "bold"), bg="blue",
                           fg="white", command=self.reset_data)
        reset_btn.grid(row=0, column=3)

        # Right Side Frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=630, y=10, width=620, height=500)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=5, width=595, height=400)

        # ===================Scroll table====================
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=(
        "id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set,
                                                  yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

    # =====================fetch data======================

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

            self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open csv",
                                         filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # export CSV

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "NO DATA FOUND TO EXPORT", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open csv",
                                               filetypes=(("Open CSV", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data exported to" + os.path.basename(fln) + "Successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
