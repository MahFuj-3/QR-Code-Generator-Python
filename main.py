from tkinter import*
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage


class QR_Generator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x650+200+50")
        self.root.title("QR Code Generator | Developed by MahFuj")

        title = Label(self.root, text="    Qr Code Generator", font=(
            "times new roman", 40), bg="#197fd3", fg="white", anchor="w").place(x=0, y=0, relwidth=1)

        # Student Details
        # Variables
        self.var_std_name = StringVar()
        self.var_std_id = StringVar()
        self.var_std_department = StringVar()
        self.var_std_batch = StringVar()

        std_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        std_Frame.place(x=50, y=110, width=600, height=500)

        std_title = Label(std_Frame, text="Student Info", font=(
            "goudy old style", 20), bg="#5a19d3", fg="white").place(x=0, y=0, relwidth=1)

        lbl_std_name = Label(std_Frame, text="Student Name", font=(
            "times new roman", 15, "bold"), bg="white").place(x=20, y=80)
        lbl_std_id = Label(std_Frame, text="Student ID", font=(
            "times new roman", 15, "bold"), bg="white").place(x=20, y=140)
        lbl_std_department = Label(std_Frame, text="Department", font=(
            "times new roman", 15, "bold"), bg="white").place(x=20, y=200)
        lbl_std_batch = Label(std_Frame, text="Batch", font=(
            "times new roman", 15, "bold"), bg="white").place(x=20, y=260)

        txt_std_name = Entry(std_Frame, font=(
            "times new roman", 15), textvariable=self.var_std_name, bg="#cecece").place(x=200, y=80, width=350, height=40)
        txt_std_id = Entry(std_Frame, font=(
            "times new roman", 15), textvariable=self.var_std_id, bg="#cecece").place(x=200, y=140, width=350, height=40)
        txt_std_department = Entry(std_Frame, font=(
            "times new roman", 15), textvariable=self.var_std_department, bg="#cecece").place(x=200, y=200, width=350, height=40)
        txt_std_batch = Entry(std_Frame, font=(
            "times new roman", 15), textvariable=self.var_std_batch, bg="#cecece").place(x=200, y=260, width=350, height=40)

        btn_generate = Button(std_Frame, text="Generate QR", command=self.generate, font=(
            "times new roman", 18, "bold"), bg="#5ed121", fg="white").place(x=90, y=360, width=220, height=40)

        btn_clear = Button(std_Frame, text="Clear", command=self.clear, font=(
            "times new roman", 18, "bold"), bg="#ea2923", fg="white").place(x=340, y=360, width=160, height=40)

        self.msg = "Enter Student Informations!!"
        self.lbl_msg = Label(std_Frame, text=self.msg, font=(
            "times new roman", 20), bg="white", fg="#0866d8")
        self.lbl_msg.place(x=0, y=430, relwidth=1)

        # Qr Code
        qr_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        qr_Frame.place(x=700, y=110, width=450, height=500)

        std_title = Label(qr_Frame, text="Student QR Code", font=(
            "goudy old style", 20), bg="#5a19d3", fg="white").place(x=0, y=0, relwidth=1)

        self.qr_code = Label(qr_Frame, text="No QR\nAvailable", font=(
            "times new roman", 15), bg="#a0a0a0", fg="white", bd=1, relief=RIDGE)
        self.qr_code.place(x=50, y=78, width=350, height=380)

    def generate(self):
        if self.var_std_name.get() == "" or self.var_std_id.get() == "" or self.var_std_department.get() == "" or self.var_std_batch.get() == "":
            self.msg = "All Fields are Required!!"
            self.lbl_msg.config(text=self.msg, fg="red")
        else:
            qr_data = (
                f"Student Name: {self.var_std_name.get()}\nStudent ID: {self.var_std_id.get()}\nDepartment: {self.var_std_department.get()}\nBatch: {self.var_std_batch.get()}")
            qr_code = qrcode.make(qr_data)

            qr_code = resizeimage.resize_cover(qr_code, [350, 380])
            qr_code.save("Student_QR/Std_"+str(self.var_std_id.get())+".png")
            # QR Code Image Update
            self.im = ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)
            self.msg = "QR Generated Successfully!!"
            self.lbl_msg.config(text=self.msg, fg="green")

    def clear(self):
        self.var_std_name.set("")
        self.var_std_id.set("")
        self.var_std_department.set("")
        self.var_std_batch.set("")
        self.msg = "Enter Student Informations!!"
        self.lbl_msg.config(text=self.msg, fg="#0866d8")
        self.qr_code.config(image="")


root = Tk()
obj = QR_Generator(root)
root.mainloop()
