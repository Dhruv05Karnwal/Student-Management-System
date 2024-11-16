from tkinter import *
from tkinter import ttk, messagebox
import time
import ttkthemes


def date():
    todaysdate = time.strftime('%d/%m/%Y')
    datelabel.config(text=f"Date: {todaysdate}")

def AddStudent():
    def add_data():
        if sapentry.get() == '' or nameentry.get() == '' or addressentry.get() == '' or mobileentry.get() == '' or schoolentry.get() == '' or courseentry.get() == '':
            messagebox.showerror('Error', 'All Fields are Required', parent=addwin)
        else:
            studenttable.insert("", "end", values=(
                sapentry.get(),
                nameentry.get(),
                addressentry.get(),
                mobileentry.get(),
                schoolentry.get(),
                courseentry.get()
            ))

            with open("Details.txt", "a") as f:
                details = [
                    sapentry.get(),
                    nameentry.get(),
                    addressentry.get(),
                    mobileentry.get(),
                    schoolentry.get(),
                    courseentry.get(),
                ]
                print(details)
                f.write('\t'.join(details) + "\n")

            messagebox.showinfo("Success", "Student details added successfully", parent=addwin)
            addwin.destroy()
        
    addwin = Toplevel()
    addwin.resizable(0, 0)
    addwin.grab_set()
    addwin.geometry('500x500+500+150')
    addwin.title("Add Student Details")
    saplabel = Label(addwin, text='Sap Id:', font=('calbiri', 12, 'bold'))
    saplabel.grid(row=0, column=0, pady=20, padx=(60, 5), sticky=W)
    sapentry = Entry(addwin, bd=2, font=('calbiri', 12), width=25)
    sapentry.grid(row=0, column=1)
    namelabel = Label(addwin, text='Full Name:', font=('calbiri', 12, 'bold'))
    namelabel.grid(row=1, column=0, pady=20, padx=(60, 5), sticky=W)
    nameentry = Entry(addwin, bd=2, font=('calbiri', 12), width=25)
    nameentry.grid(row=1, column=1)
    addresslabel = Label(addwin, text='Address:', font=('calbiri', 12, 'bold'))
    addresslabel.grid(row=2, column=0, pady=20, padx=(60, 5), sticky=W)
    addressentry = Entry(addwin, bd=2, font=('calbiri', 12), width=25)
    addressentry.grid(row=2, column=1)
    mobilelabel = Label(addwin, text='Mobile No.:', font=('calbiri', 12, 'bold'))
    mobilelabel.grid(row=3, column=0, pady=20, padx=(60, 5), sticky=W)
    mobileentry = Entry(addwin, bd=2, font=('calbiri', 12), width=25)
    mobileentry.grid(row=3, column=1)
    schoollabel = Label(addwin, text='School:', font=('calbiri', 12, 'bold'))
    schoollabel.grid(row=4, column=0, pady=20, padx=(60, 5), sticky=W)
    schoolentry = Entry(addwin, bd=2, font=('calbiri', 12), width=25)
    schoolentry.grid(row=4, column=1)
    courselabel = Label(addwin, text='Course:', font=('calbiri', 12, 'bold'))
    courselabel.grid(row=5, column=0, pady=20, padx=(60, 5), sticky=W)
    courseentry = Entry(addwin, bd=2, font=('calbiri', 12), width=25)
    courseentry.grid(row=5, column=1)
    addstudent_button = ttk.Button(addwin, text='ADD STUDENT', command=add_data, width=20)
    addstudent_button.place(x=160, y=430)

def open_search_window():
    def search():
        query = search_entry.get()
        found = False
        studenttable.delete(*studenttable.get_children())
        with open("Details.txt", "r") as f:
            for line in f:
                data = line.strip().split('\t')
                if len(data) >= 2 and (data[0] == query or data[1] == query):
                    found = True
                    studenttable.insert("", "end", values=data)
        search_win.destroy()
        if not found:
            messagebox.showerror("Error", "Student with the given SAP ID or Name not found.")

    search_win = Toplevel()
    search_win.title("Search Student")
    search_win.geometry('450x250+500+200')
    search_win.resizable(0,0)
    search_win.grab_set()

    searchlabel = Label(search_win, text='Enter SAP ID or Name:', font=('calbiri', 12, 'bold'))
    searchlabel.grid(row=0, column=0, padx=10, pady=10)
    search_entry = Entry(search_win, bd=2, font=('calbiri', 12), width=25)
    search_entry.grid(row=0, column=1, padx=10, pady=10)

    search_button = ttk.Button(search_win, text='SEARCH', command=search, width=10)
    search_button.place(x=160, y=180)




def open_delete_window():
    def delete():
        query = delete_entry.get()
        found = False
        items_to_delete = []
        with open("Details.txt", "r") as f:
            lines = f.readlines()
        with open("Details.txt", "w") as f:
            for line in lines:
                data = line.strip().split('\t')
                if data[0] != query and data[1] != query:
                    f.write(line)
                else:
                    found = True
                    for item in studenttable.get_children():
                        if studenttable.item(item, "values")[:2] == (data[0], data[1]):
                            items_to_delete.append(item)
        for item in items_to_delete:
            studenttable.delete(item)

        if found:
            messagebox.showinfo("Success", "Student deleted successfully.",parent=delete_win)
        else:
            messagebox.showerror("Error", "Student with the given SAP ID or Name not found.",parent=delete_win)
        delete_win.destroy()

    def clear():
        open("Details.txt", "w").close()
        studenttable.delete(*studenttable.get_children())
        messagebox.showinfo("Success", "File content cleared successfully.")

    delete_win = Toplevel()
    delete_win.title("Delete Student")
    delete_win.geometry('450x300+500+200')
    delete_win.resizable(0,0)
    delete_win.grab_set()

    deletelabel = Label(delete_win, text='Enter SAP ID or Name:', font=('calbiri', 12, 'bold'))
    deletelabel.grid(row=0, column=0, padx=10, pady=10)
    delete_entry = Entry(delete_win, bd=2, font=('calbiri', 12), width=20)
    delete_entry.grid(row=0, column=1, padx=10, pady=10)

    delete_button = ttk.Button(delete_win, text='DELETE', command=delete, width=10)
    delete_button.place(x=160,y=180)

    clear_button = ttk.Button(delete_win, text='CLEAR FILE', command=clear, width=10)
    clear_button.place(x=160,y=220)


def open_update_window():
    update_win = Toplevel()
    update_win.title("Update Student")
    update_win.geometry('500x400+500+200')
    update_win.resizable(0,0)
    update_win.grab_set()

    sap_label = Label(update_win, text='SAP ID:', font=('calibri', 12, 'bold'))
    sap_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
    sap_entry = Entry(update_win, bd=2, font=('calibri', 12), width=25)
    sap_entry.grid(row=0, column=1, padx=10, pady=10)

    def check_sap_id():
        nonlocal name_entry, address_entry, mobile_entry, school_entry, course_entry
        sap_id = sap_entry.get()
        found = False
        with open("Details.txt", "r") as f:
            for line in f:
                data = line.strip().split('\t')
                if data[0] == sap_id:
                    found = True
                    name_entry.config(state='normal')
                    address_entry.config(state='normal')
                    mobile_entry.config(state='normal')
                    school_entry.config(state='normal')
                    course_entry.config(state='normal')
                    break
        if not found:
            messagebox.showerror("Error", "Student with the given SAP ID not found.")

    def update_student():
        sap_id = sap_entry.get()
        name = name_entry.get()
        address = address_entry.get()
        mobile = mobile_entry.get()
        school = school_entry.get()
        course = course_entry.get()

        with open("Details.txt", "r") as f:
            lines = f.readlines()
        with open("Details.txt", "w") as f:
            for line in lines:
                data = line.strip().split('\t')
                if data[0] == sap_id:
                    f.write(f"{sap_id}\t{name}\t{address}\t{mobile}\t{school}\t{course}\n")
                else:
                    f.write(line)

        for item in studenttable.get_children():
            if studenttable.item(item, "values")[0] == sap_id:
                studenttable.item(item, values=(sap_id, name, address, mobile, school, course))
        messagebox.showinfo("Success", "Student details updated successfully.")
        update_win.destroy()

    name_entry = Entry(update_win, bd=2, font=('calibri', 12), width=25, state='disabled')
    address_entry = Entry(update_win, bd=2, font=('calibri', 12), width=25, state='disabled')
    mobile_entry = Entry(update_win, bd=2, font=('calibri', 12), width=25, state='disabled')
    school_entry = Entry(update_win, bd=2, font=('calibri', 12), width=25, state='disabled')
    course_entry = Entry(update_win, bd=2, font=('calibri', 12), width=25, state='disabled')

    name_label = Label(update_win, text='Full Name:', font=('calibri', 12, 'bold'))
    name_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')
    name_entry.grid(row=1, column=1, padx=10, pady=10)

    address_label = Label(update_win, text='Address:', font=('calibri', 12, 'bold'))
    address_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')
    address_entry.grid(row=2, column=1, padx=10, pady=10)

    mobile_label = Label(update_win, text='Mobile No.:', font=('calibri', 12, 'bold'))
    mobile_label.grid(row=3, column=0, padx=10, pady=10, sticky='e')
    mobile_entry.grid(row=3, column=1, padx=10, pady=10)

    school_label = Label(update_win, text='School:', font=('calibri', 12, 'bold'))
    school_label.grid(row=4, column=0, padx=10, pady=10, sticky='e')
    school_entry.grid(row=4, column=1, padx=10, pady=10)

    course_label = Label(update_win, text='Course:', font=('calibri', 12, 'bold'))
    course_label.grid(row=5, column=0, padx=10, pady=10, sticky='e')
    course_entry.grid(row=5, column=1, padx=10, pady=10)

    check_button = ttk.Button(update_win, text='Check SAP ID', command=check_sap_id)
    check_button.grid(row=0, column=2, padx=10, pady=10)

    update_button = ttk.Button(update_win, text='Update', command=update_student)
    update_button.grid(row=6, column=1, padx=10, pady=10)


def show_students():
    for row in studenttable.get_children():
        studenttable.delete(row)

    with open("Details.txt", "r") as f:
        for line in f:
            data = line.strip().split('\t')
            studenttable.insert("", "end", values=data)

def end_program():
    win.destroy()

win = ttkthemes.ThemedTk()
win.get_themes()
win.set_theme('radiance')

win.geometry('1530x800+0+0')

win.title('Student Management System')

datelabel = Label(win, font=('sans serif', 18, 'bold'))
datelabel.place(x=50, y=10)
date()

heading = Label(win, text='STUDENT MANAGEMENT SYSTEM', font=('Times New Roman', 25, 'bold', 'underline', 'italic'))
heading.place(x=490, y=10)

exitbutton = ttk.Button(win, text='END PROGRAM',command=end_program, width=25,)
exitbutton.place(x=1200, y=20)

header = Frame(win)
header.place(x=0, y=60, width=1530, height=150)

addstudent = ttk.Button(header, text='Add Student', command=AddStudent, width=25)
addstudent.grid(row=0, column=2, pady=70, padx=(150, 0))

searchstudent = ttk.Button(header, text='Search Student',command=open_search_window, width=25)
searchstudent.grid(row=0, column=3)

deletestudent = ttk.Button(header, text='Delete Student',command=open_delete_window, width=25)
deletestudent.grid(row=0, column=4)

updatestudent = ttk.Button(header, text='Update Student',command=open_update_window, width=25)
updatestudent.grid(row=0, column=5)

showstudent = ttk.Button(header, text='Show Student',command=show_students, width=25)
showstudent.grid(row=0, column=6)

footer = Frame(win)
footer.place(x=0, y=210, width=1530, height=590)

studenttable = ttk.Treeview(footer, columns=('Sap Id', 'Name', 'Address', 'Mobile No.', 'School', 'Course'))
studenttable.pack(fill=BOTH, expand=1)

studenttable.heading('Sap Id', text='SAP ID')
studenttable.heading('Name', text='FULL NAME')
studenttable.heading('Address', text='ADDRESS')
studenttable.heading('Mobile No.', text='MOBILE NO.')
studenttable.heading('School', text='SCHOOL')
studenttable.heading('Course', text='COURSE')

studenttable.config(show='headings')

win.mainloop()
