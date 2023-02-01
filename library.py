from tkinter import *
from tkinter import ttk


class LibraryManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1365x767+0+0")

        labeltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", fg="green", bd=10,
                           relief=RIDGE, font=("times new roman", 30, "bold"), padx=2, pady=6)
        labeltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=78, width=1365, height=400)

        # ======================= DataFrame Right Left =======================
        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg="green", bd=5,
                                   relief=RIDGE, font=("times new roman", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=750, height=340)
        # ======================= DataFrame Right Right =======================
        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue", fg="green", bd=5,
                                    relief=RIDGE, font=("times new roman", 12, "bold"))
        DataFrameRight.place(x=810, y=5, width=490, height=340)
        # ============================= Membership option =============================
        labelMember = Label(DataFrameLeft, text="Member Type", bg="powder blue", font=("times new roman", 12, "bold"),
                            padx=2, pady=6)
        labelMember.grid(row=0, column=0, sticky=W)

        ComMember = ttk.Combobox(DataFrameLeft, font=("times new roman", 12, "bold"), width=22, state="readonly")
        ComMember["value"] = ("Admin Staff", "Student", "Lecturer", "Professor", "Guest")
        ComMember.grid(row=0, column=1)

        # ======================== Label ========================
        labelPRN_No = Label(DataFrameLeft, text="PRN No", bg="powder blue", font=("times new roman", 12, "bold"),
                            padx=2, pady=0)
        labelPRN_No.grid(row=1, column=0, sticky=W)

        txtPRN_No = Entry(DataFrameLeft, font=("times new roman", 12), width=25)
        txtPRN_No.grid(row=1, column=1)

        labeltitle = Label(DataFrameLeft, text="Identity No", bg="powder blue", font=("times new roman", 12, "bold"),
                           padx=2, pady=4)
        labeltitle.grid(row=2, column=0, sticky=W)
        txttitle = Entry(DataFrameLeft, font=("times new roman", 12), width=25)
        txttitle.grid(row=2, column=1)

        labelfname = Label(DataFrameLeft, text="First Name", bg="powder blue", font=("times new roman", 12, "bold"),
                           padx=2, pady=4)
        labelfname.grid(row=3, column=0, sticky=W)
        txtfname = Entry(DataFrameLeft, font=("times new roman", 12), width=25)
        txtfname.grid(row=3, column=1)
        labellname = Label(DataFrameLeft, text="Last Name", bg="powder blue", font=("times new roman", 12, "bold"),
                           padx=2, pady=4)
        labellname.grid(row=4, column=0, sticky=W)
        txtlname = Entry(DataFrameLeft, font=("times new roman", 12), width=25)
        txtlname.grid(row=4, column=1)

        labeladdress1 = Label(DataFrameLeft, text="Address 1", bg="powder blue", font=("times new roman", 12, "bold"),
                              padx=2, pady=4)
        labeladdress1.grid(row=5, column=0, sticky=W)
        txtaddress1 = Entry(DataFrameLeft, font=("times new roman", 12), width=25)
        txtaddress1.grid(row=5, column=1)

        labeladdress2 = Label(DataFrameLeft, text="Address 2", bg="powder blue", font=("times new roman", 12, "bold"),
                              padx=2, pady=4)
        labeladdress2.grid(row=6, column=0, sticky=W)
        txtaddress2 = Entry(DataFrameLeft, font=("times new roman", 12), width=25)
        txtaddress2.grid(row=6, column=1)

        labelpostalcode = Label(DataFrameLeft, text="Postal Code", bg="powder blue",
                                font=("times new roman", 12, "bold"),
                                padx=2, pady=4)
        labelpostalcode.grid(row=7, column=0, sticky=W)
        txtpostalcode = Entry(DataFrameLeft, font=("times new roman", 12), width=25)
        txtpostalcode.grid(row=7, column=1)

        labelmobile = Label(DataFrameLeft, text="Mobile", bg="powder blue", font=("times new roman", 12, "bold"),
                            padx=2, pady=4)
        labelmobile.grid(row=8, column=0, sticky=W)
        txtmobile = Entry(DataFrameLeft, font=("times new roman", 12), width=25)
        txtmobile.grid(row=8, column=1)

        # ================New Column================

        labelbookid = Label(DataFrameLeft, text="Book Id", bg="powder blue", font=("times new roman", 12, "bold"),
                            padx=2, pady=4)
        labelbookid.grid(row=0, column=4, sticky=W)
        txtbookid = Entry(DataFrameLeft, font=("times new roman", 12), width=25)
        txtbookid.grid(row=0, column=5)

        labelbookname = Label(DataFrameLeft, text="Book Name", bg="powder blue", font=("times new roman", 12, "bold"),
                              padx=2, pady=4)
        labelbookname.grid(row=1, column=4, sticky=W)
        txtname = Entry(DataFrameLeft, font=("times new roman", 12), width=25)
        txtname.grid(row=1, column=5)

        labelauthorname = Label(DataFrameLeft, text="Author Name", bg="powder blue",
                                font=("times new roman", 12, "bold"),
                                padx=2, pady=4)
        labelauthorname.grid(row=2, column=4, sticky=W)
        txtauthor = Entry(DataFrameLeft, font=("times new roman", 12), width=25)
        txtauthor.grid(row=2, column=5)

        labeldateborrowed = Label(DataFrameLeft, text="Date Borrowed", bg="powder blue",
                                  font=("times new roman", 12, "bold"),
                                  padx=2, pady=4)
        labeldateborrowed.grid(row=3, column=4, sticky=W)
        txtdateborrowed = Entry(DataFrameLeft, font=("times new roman", 12), width=25)
        txtdateborrowed.grid(row=3, column=5)

        labeldatedue = Label(DataFrameLeft, text="Date Due", bg="powder blue",
                             font=("times new roman", 12, "bold"),
                             padx=2, pady=4)
        labeldatedue.grid(row=4, column=4, sticky=W)
        txtdatedue = Entry(DataFrameLeft, font=("times new roman", 12), width=25)
        txtdatedue.grid(row=4, column=5)

        labeldaysonbook = Label(DataFrameLeft, text="Days on Book", bg="powder blue",
                                font=("times new roman", 12, "bold"),
                                padx=2, pady=4)
        labeldaysonbook.grid(row=5, column=4, sticky=W)
        txtdaysonbook = Entry(DataFrameLeft, font=("times new roman", 12), width=25)
        txtdaysonbook.grid(row=5, column=5)

        labellatereturnfine = Label(DataFrameLeft, text="Late Return Fine", bg="powder blue",
                                    font=("times new roman", 12, "bold"),
                                    padx=2, pady=4)
        labellatereturnfine.grid(row=6, column=4, sticky=W)
        txtlatereturnfine = Entry(DataFrameLeft, font=("times new roman", 12), width=25)
        txtlatereturnfine.grid(row=6, column=5)

        labeldateoverdue = Label(DataFrameLeft, text="Date Over Due", bg="powder blue",
                                 font=("times new roman", 12, "bold"),
                                 padx=2, pady=4)
        labeldateoverdue.grid(row=7, column=4, sticky=W)
        txtdateoverdue = Entry(DataFrameLeft, font=("times new roman", 12), width=25)
        txtdateoverdue.grid(row=7, column=5)

        labelprice = Label(DataFrameLeft, text="Actual Price", bg="powder blue",
                           font=("times new roman", 12, "bold"),
                           padx=2, pady=4)
        labelprice.grid(row=8, column=4, sticky=W)
        txtprice = Entry(DataFrameLeft, font=("times new roman", 12), width=25)
        txtprice.grid(row=8, column=5)

        # ============================DataFrame Right Inside============================
        self.txtBox = Text(DataFrameRight, font=("time new roman", 12, "bold"),
                           width=25, height=16)
        self.txtBox.grid(row=0, column=4, padx=6, pady=2)

        # ====================Scroll bar Right Frame list====================
        listscrollbar = Scrollbar(DataFrameRight)
        listscrollbar.grid(row=0, column=1, sticky="ns")  # ns for north-south, direction of scrollbar

        listbooks = ["Python Crash Course", "Programming with Jabed", "CS50 Python", "Steve Jobs",
                     "Love for imperfect things", "Machine Learning", "Jupyter Notebook", "Numpy Tutorial",
                     "Opencv Python", "Compiler Design", "Computer Networks", "Automation", "Anaconda3",
                     "Object Oriented Program", "Structure Programming", "Software Engineering"]
        listBox = Listbox(DataFrameRight, font=("times new roman", 12, "bold"), width=25, height=15)
        listBox.grid(row=0, column=0, padx=4)

        # configuration of the scrollbar
        listscrollbar.config(command=listBox.yview)

        for item in listbooks:
            listBox.insert(END, item)


        # ======================Information Desk======================

        # =======================Buttons Frame=======================
        FrameButton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameButton.place(x=0, y=450, width=1365, height=70)

        # =======================Database Info Frame=======================
        FrameData = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameData.place(x=0, y=500, width=1365, height=230)


if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagement(root)
    root.mainloop()
