from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime

class LibraryManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1365x767+0+0")

        # ======================= Variable ======================
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.actualprice_var = StringVar()

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

        ComMember = ttk.Combobox(DataFrameLeft, textvariable=self.member_var, font=("times new roman", 12, "bold"),
                                 width=22, state="readonly")
        ComMember["value"] = ("Admin Staff", "Student", "Lecturer", "Professor", "Guest")
        ComMember.grid(row=0, column=1)

        # ======================== Label ========================
        labelPRN_No = Label(DataFrameLeft, text="PRN No", bg="powder blue", font=("times new roman", 12, "bold"),
                            padx=2, pady=0)
        labelPRN_No.grid(row=1, column=0, sticky=W)

        txtPRN_No = Entry(DataFrameLeft, font=("times new roman", 12), textvariable=self.prn_var, width=25)
        txtPRN_No.grid(row=1, column=1)

        labeltitle = Label(DataFrameLeft, text="Identity No", bg="powder blue", font=("times new roman", 12, "bold"),
                           padx=2, pady=4)
        labeltitle.grid(row=2, column=0, sticky=W)
        txttitle = Entry(DataFrameLeft, font=("times new roman", 12), textvariable=self.id_var, width=25)
        txttitle.grid(row=2, column=1)

        labelfname = Label(DataFrameLeft, text="First Name", bg="powder blue", font=("times new roman", 12, "bold"),
                           padx=2, pady=4)
        labelfname.grid(row=3, column=0, sticky=W)
        txtfname = Entry(DataFrameLeft, font=("times new roman", 12), textvariable=self.firstname_var, width=25)
        txtfname.grid(row=3, column=1)
        labellname = Label(DataFrameLeft, text="Last Name", bg="powder blue", font=("times new roman", 12, "bold"),
                           padx=2, pady=4)
        labellname.grid(row=4, column=0, sticky=W)
        txtlname = Entry(DataFrameLeft, font=("times new roman", 12), textvariable=self.lastname_var, width=25)
        txtlname.grid(row=4, column=1)

        labeladdress1 = Label(DataFrameLeft, text="Address 1", bg="powder blue", font=("times new roman", 12, "bold"),
                              padx=2, pady=4)
        labeladdress1.grid(row=5, column=0, sticky=W)
        txtaddress1 = Entry(DataFrameLeft, font=("times new roman", 12), textvariable=self.address1_var, width=25)
        txtaddress1.grid(row=5, column=1)

        labeladdress2 = Label(DataFrameLeft, text="Address 2", bg="powder blue", font=("times new roman", 12, "bold"),
                              padx=2, pady=4)
        labeladdress2.grid(row=6, column=0, sticky=W)
        txtaddress2 = Entry(DataFrameLeft, font=("times new roman", 12), textvariable=self.address2_var, width=25)
        txtaddress2.grid(row=6, column=1)

        labelpostalcode = Label(DataFrameLeft, text="Postal Code", bg="powder blue",
                                font=("times new roman", 12, "bold"),
                                padx=2, pady=4)
        labelpostalcode.grid(row=7, column=0, sticky=W)
        txtpostalcode = Entry(DataFrameLeft, font=("times new roman", 12), textvariable=self.postcode_var, width=25)
        txtpostalcode.grid(row=7, column=1)

        labelmobile = Label(DataFrameLeft, text="Mobile", bg="powder blue", font=("times new roman", 12, "bold"),
                            padx=2, pady=4)
        labelmobile.grid(row=8, column=0, sticky=W)
        txtmobile = Entry(DataFrameLeft, font=("times new roman", 12), textvariable=self.mobile_var, width=25)
        txtmobile.grid(row=8, column=1)

        # ================New Column================

        labelbookid = Label(DataFrameLeft, text="Book Id", bg="powder blue", font=("times new roman", 12, "bold"),
                            padx=2, pady=4)
        labelbookid.grid(row=0, column=4, sticky=W)
        txtbookid = Entry(DataFrameLeft, font=("times new roman", 12), textvariable=self.bookid_var, width=25)
        txtbookid.grid(row=0, column=5)

        labelbookname = Label(DataFrameLeft, text="Book Name", bg="powder blue", font=("times new roman", 12, "bold"),
                              padx=2, pady=4)
        labelbookname.grid(row=1, column=4, sticky=W)
        txtname = Entry(DataFrameLeft, font=("times new roman", 12), textvariable=self.booktitle_var, width=25)
        txtname.grid(row=1, column=5)

        labelauthorname = Label(DataFrameLeft, text="Author Name", bg="powder blue",
                                font=("times new roman", 12, "bold"),
                                padx=2, pady=4)
        labelauthorname.grid(row=2, column=4, sticky=W)
        txtauthor = Entry(DataFrameLeft, font=("times new roman", 12), textvariable=self.author_var, width=25)
        txtauthor.grid(row=2, column=5)

        labeldateborrowed = Label(DataFrameLeft, text="Date Borrowed", bg="powder blue",
                                  font=("times new roman", 12, "bold"),
                                  padx=2, pady=4)
        labeldateborrowed.grid(row=3, column=4, sticky=W)
        txtdateborrowed = Entry(DataFrameLeft, font=("times new roman", 12), textvariable=self.dateborrowed_var,
                                width=25)
        txtdateborrowed.grid(row=3, column=5)

        labeldatedue = Label(DataFrameLeft, text="Date Due", bg="powder blue",
                             font=("times new roman", 12, "bold"),
                             padx=2, pady=4)
        labeldatedue.grid(row=4, column=4, sticky=W)
        txtdatedue = Entry(DataFrameLeft, font=("times new roman", 12), textvariable=self.datedue_var, width=25)
        txtdatedue.grid(row=4, column=5)

        labeldaysonbook = Label(DataFrameLeft, text="Days on Book", bg="powder blue",
                                font=("times new roman", 12, "bold"),
                                padx=2, pady=4)
        labeldaysonbook.grid(row=5, column=4, sticky=W)
        txtdaysonbook = Entry(DataFrameLeft, font=("times new roman", 12), textvariable=self.daysonbook_var, width=25)
        txtdaysonbook.grid(row=5, column=5)

        labellatereturnfine = Label(DataFrameLeft, text="Late Return Fine", bg="powder blue",
                                    font=("times new roman", 12, "bold"),
                                    padx=2, pady=4)
        labellatereturnfine.grid(row=6, column=4, sticky=W)
        txtlatereturnfine = Entry(DataFrameLeft, font=("times new roman", 12), textvariable=self.latereturnfine_var,
                                  width=25)
        txtlatereturnfine.grid(row=6, column=5)

        labeldateoverdue = Label(DataFrameLeft, text="Date Over Due", bg="powder blue",
                                 font=("times new roman", 12, "bold"),
                                 padx=2, pady=4)
        labeldateoverdue.grid(row=7, column=4, sticky=W)
        txtdateoverdue = Entry(DataFrameLeft, font=("times new roman", 12), textvariable=self.dateoverdue_var, width=25)
        txtdateoverdue.grid(row=7, column=5)

        labelprice = Label(DataFrameLeft, text="Actual Price", bg="powder blue",
                           font=("times new roman", 12, "bold"),
                           padx=2, pady=4)
        labelprice.grid(row=8, column=4, sticky=W)
        txtprice = Entry(DataFrameLeft, font=("times new roman", 12), textvariable=self.actualprice_var, width=25)
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
                     "Object Oriented Program", "Structure Programming", "Software Engineering",
                     "Theory of Computation",
                     "Data Structure", "Electronics-1", "Multimedia", "Operation System", "Peripheral",
                     "Visual Programming", "Algorithm Design", "Assembly Language", "Microprocessor"]
        def SelectBook(event=""):
            value = str(listBox.get(listBox.curselection()))
            x = value
            if x == "Python Crash Course":
                self.bookid_var.set("PCC22")
                self.booktitle_var.set("Python Crash Course")
                self.author_var.set("Eric Matthes")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("100 TK")
                self.dateoverdue_var.set("NO")
                self.actualprice_var.set("1200 TK")



        listBox = Listbox(DataFrameRight, font=("times new roman", 12, "bold"), width=25, height=15)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0, column=0, padx=4)

        # configuration of the scrollbar
        listscrollbar.config(command=listBox.yview)

        for item in listbooks:
            listBox.insert(END, item)

        # =======================Buttons Frame=======================
        FrameButton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameButton.place(x=0, y=450, width=1365, height=70)

        btnaddData = Button(FrameButton, command=self.ADD_DATA, text="Add Data", font=("times new roman", 12, "bold"),
                            width=20, bg="#cdcdcd", fg="#2e325c")
        btnaddData.grid(row=0, column=0, padx=15, pady=2)
        btnaddData = Button(FrameButton, text="Show Data", font=("times new roman", 12, "bold"),
                            width=20, bg="#cdcdcd", fg="#2e325c")
        btnaddData.grid(row=0, column=1, padx=15, pady=2)
        btnaddData = Button(FrameButton, text="Update", font=("times new roman", 12, "bold"),
                            width=20, bg="#cdcdcd", fg="#2e325c")
        btnaddData.grid(row=0, column=2, padx=15, pady=2)
        btnaddData = Button(FrameButton, text="Delete", font=("times new roman", 12, "bold"),
                            width=20, bg="#cdcdcd", fg="#2e325c")
        btnaddData.grid(row=0, column=3, padx=15, pady=2)
        btnaddData = Button(FrameButton, text="Reset", font=("times new roman", 12, "bold"),
                            width=20, bg="#cdcdcd", fg="#2e325c")
        btnaddData.grid(row=0, column=4, padx=15, pady=2)
        btnaddData = Button(FrameButton, text="Exit", font=("times new roman", 12, "bold"),
                            width=20, bg="#cdcdcd", fg="#2e325c")
        btnaddData.grid(row=0, column=5, padx=15, pady=2)

        # =======================Database Info Frame=======================
        FrameData = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameData.place(x=0, y=500, width=1365, height=230)

        tableframe = Frame(FrameData, bd=4, relief=RIDGE, bg="powder blue")
        tableframe.place(x=0, y=6, width=1300, height=190)

        xscroll = ttk.Scrollbar(tableframe, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(tableframe, orient=VERTICAL)

        self.library_table = ttk.Treeview(tableframe, column=("membertype", "prnno", "title", "firstname",
                                                              "lastname", "address1", "address2", "postid",
                                                              "booktitle", "author", "dateborrowed", "datedue",
                                                              "days", "latereturnfine", "dateoverdue", "finalprice"),
                                          xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        # ----- Config Scroll to make it visible-----
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("prnno", text="PRN No")
        self.library_table.heading("title", text="Title")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address1", text="Address 1")
        self.library_table.heading("address2", text="Address 2")
        self.library_table.heading("postid", text="Post ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("dateborrowed", text="Date Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="Days")
        self.library_table.heading("latereturnfine", text="Late Return Fine")
        self.library_table.heading("dateoverdue", text="Date Over Due")
        self.library_table.heading("finalprice", text="Final Price")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        # ==============Database frame table width setting===============
        self.library_table.column("membertype", width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("title", width=100)
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("postid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("author", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)

    # =================== add data function===============
    def ADD_DATA(self):
        connect = mysql.connector.connect(host="127.0.0.1",
                                          username="root",
                                          password="jabedkhanjb",
                                          database="library_management_system")
        my_cursor = connect.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                          (self.member_var.get(),
                           self.prn_var.get(), # verify input using regular expression
                           self.id_var.get(),
                           self.firstname_var.get(),
                           self.lastname_var.get(),
                           self.address1_var.get(),
                           self.address2_var.get(),
                           self.postcode_var.get(),
                           self.mobile_var.get(),
                           self.bookid_var.get(),
                           self.booktitle_var.get(),
                           self.author_var.get(),
                           self.dateborrowed_var.get(),
                           self.datedue_var.get(),
                           self.daysonbook_var.get(),
                           self.latereturnfine_var.get(),
                           self.dateoverdue_var.get(),
                           self.actualprice_var.get(),
                           ))
        connect.commit()
        connect.close()
        messagebox.showinfo("Success", "Member has been inserted successfully")


if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagement(root)
    root.mainloop()
















