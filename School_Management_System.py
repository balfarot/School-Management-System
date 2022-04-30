# CSUMB School Management System #

# I was inspired by the user forms we were taught how to build on Excel in BUS 308
# Here are the list of websites I used to help me build this management system:
    # https://github.com/shivambangwal/Student-Management-System-PYTHON-GUI-tkinter.- MY MAIN REFERENCE IN WHICH I ADDED TOO
    # https://techvidvan.com/tutorials/shop-management-system-in-python/
    # https://towardsdatascience.com/develop-your-own-calendar-to-track-important-dates-with-python-c1af9e98ffc3#
    # https://www.geeksforgeeks.org/tkinter-optionmenu-widget/
# I also watched many YouTube videos like the ones I will be listing down below:
    # https://www.youtube.com/watch?v=YR3h2CY21-U
    # https://www.youtube.com/watch?v=AK1J8xF4fuk
    # https://www.youtube.com/watch?v=c9_gcIeAru0


# Lines 16-20 are the libraries I use
from tkinter import *
import tkinter.messagebox as mb
from tkinter import ttk
from tkcalendar import DateEntry
import sqlite3


# Lines 25-30 connects the Database where all information will be stored
# Reference https://www.youtube.com/watch?v=YR3h2CY21-U&t=3s
connector = sqlite3.connect('SchoolManagement.db')
cursor = connector.cursor()

connector.execute(
    "CREATE TABLE IF NOT EXISTS SCHOOL_MANAGEMENT (STUDENT_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NAME TEXT, EMAIL TEXT, PHONE_NO TEXT, GENDER TEXT, DOB TEXT, STREAM TEXT)"
)


# Lines 38-45 creates a display function by deleting everything from the table where all information
# is displayed by using the tree.delete(*tree.get_children()) statement
# The connector runs the select all statement and get all the data.
# Then, using the.insert() function, I took every piece of that data and continuing entering it into the table.
# Reference https://www.youtube.com/watch?v=c9_gcIeAru0
def display_records():
    tree.delete(*tree.get_children())

    curr = connector.execute('SELECT * FROM SCHOOL_MANAGEMENT')
    data = curr.fetchall()

    for records in data:
        tree.insert('', END, values=records)

# Lines 56-79 I got the data from all the StringVar and IntVar instances using .set() methods, and from the DateEntry
# instance using .get_date() method in the add_record() function.
# I then implemented an if not function to add an "error" message when there's a missing filled
# The else and try functions are there to add the variables' intro the database and give a message when the user did it
# correctly.
# The except function is added to for the contact entry when the user does not fill it in correctly.
# Reference https://www.youtube.com/watch?v=c9_gcIeAru0
# Reference https://towardsdatascience.com/develop-your-own-calendar-to-track-important-dates-with-python-c1af9e98ffc3#
# Reference https://techvidvan.com/tutorials/shop-management-system-in-python/
def add_record():
    global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, stream_strvar

    name = name_strvar.get()
    email = email_strvar.get()
    contact = contact_strvar.get()
    gender = gender_strvar.get()
    DOB = dob.get_date()
    stream = stream_strvar.get()

    if not name or not email or not contact or not gender or not DOB or not stream:
        mb.showerror('Error!', "Please fill all the missing fields!!")
    else:
        try:
            connector.execute(
                'INSERT INTO SCHOOL_MANAGEMENT (NAME, EMAIL, PHONE_NO, GENDER, DOB, STREAM) VALUES (?,?,?,?,?,?)',
                (name, email, contact, gender, DOB, stream)
            )
            connector.commit()
            mb.showinfo('Record added', f"Record of {name} was successfully added")
            display_records()
        except:
            mb.showerror('Wrong type',
                         'The type of the values entered is not accurate. Pls note that the contact field can only contain numbers')


# Lines 85-100 is added to be able to remove row from the database and give the user an error when a row is not selected
# after the row is selected the selection will be removed from the gui and database.
# Reference https://www.youtube.com/watch?v=c9_gcIeAru0
def remove_record():
    if not tree.selection():
        mb.showerror('Error!', 'Please select an item from the database')
    else:
        current_item = tree.focus()
        values = tree.item(current_item)
        selection = values["values"]

        tree.delete(current_item)

        connector.execute('DELETE FROM SCHOOL_MANAGEMENT WHERE STUDENT_ID=%d' % selection[0])
        connector.commit()

        mb.showinfo('Done', 'The record you wanted deleted was successfully deleted.')

        display_records()

# I CREATED LINES 104-193. THESE LINES WERE PERSONAL KNOWLEDGE THAT I LEARNED IN THIS CLASS!
# Lines 104-107 creates the gui window, gives the gui a title, creates the size, and makes sure that it does not expand
main = Tk()
main.title('CSUMB Management System')
main.geometry('1050x600')
main.resizable(0, 0)

# Lines 110-112 creates a universal font variables for my GUI
headlabelfont = ("Times", 16, 'bold')
labelfont = ('Garamond', 14)
entryfont = ('Garamond', 12)

# Lines 115-116 creates the background and foreground color variables for the frames
lf_bg = '#E4F0F7'  # bg color for the left_frame
cf_bg = '#E4F0F7'  # bg color for the center_frame

# Lines 119-123 creates the StringVar variables
name_strvar = StringVar()
email_strvar = StringVar()
contact_strvar = StringVar()
gender_strvar = StringVar()
stream_strvar = StringVar()

# Line 126 places the title of the gui the main window
Label(main, text="CSUMB Management System", font=headlabelfont, bg='#E4F0F7').pack(side=TOP, fill=X)

# Lines 129-130 creates the left_frame by adding the color (the variable I created earlier lf_bg), placement, and command
left_frame = Frame(main, bg=lf_bg)
left_frame.place(x=0, y=30, relheight=1, relwidth=0.2)

# Lines 133-134 creates the center_frame by adding the color (the variable I created earlier cf_bg), placement, and command
center_frame = Frame(main, bg=cf_bg)
center_frame.place(relx=0.2, y=30, relheight=1, relwidth=0.2)

# Lines 138-139 creates the right_frame by adding the color (I did not create a variable for this frame because more
# than half of it was going to be covered by the database), placement, and command.
right_frame = Frame(main, bg="Gray35")
right_frame.place(relx=0.4, y=30, relheight=1, relwidth=0.6)

# Lines 144-149 places the variable components in the left frame by using a label function.
# After we will add a command, label fonts (variable that I created in the begging of the code), background color
# (variable that I created earlier), and placement.
Label(left_frame, text="Name", font=labelfont, bg=lf_bg).place(relx=0.375, rely=0.10)
Label(left_frame, text="Contact Number", font=labelfont, bg=lf_bg).place(relx=0.175, rely=0.23)
Label(left_frame, text="Email Address", font=labelfont, bg=lf_bg).place(relx=0.2, rely=0.36)
Label(left_frame, text="Gender", font=labelfont, bg=lf_bg).place(relx=0.3, rely=0.50)
Label(left_frame, text="Date of Birth", font=labelfont, bg=lf_bg).place(relx=0.2, rely=0.62)
Label(left_frame, text="Stream", font=labelfont, bg=lf_bg).place(relx=0.3, rely=0.75)

# Lines 155-158 creates an entry function for the 'name', 'contact', 'email', and 'stream' variable.
# The user will be able to interact and add there information. In the entry function.
# I added a command, size, variable, font (I created in the beginning of the code), and placement into the entry
# function.
Entry(center_frame, width=19, textvariable=name_strvar, font=entryfont).place(x=20, rely=0.1)
Entry(center_frame, width=19, textvariable=contact_strvar, font=entryfont).place(x=20, rely=0.23)
Entry(center_frame, width=19, textvariable=email_strvar, font=entryfont).place(x=20, rely=0.36)
Entry(center_frame, width=19, textvariable=stream_strvar, font=entryfont).place(x=20, rely=0.75)

# Line 160 is an option menu were the user can select an entry by using a scroll bar.
# The option menu has a frame, command, description of inputs, and place function.
# Reference https://www.geeksforgeeks.org/tkinter-optionmenu-widget/
OptionMenu(center_frame, gender_strvar, 'Male', "Female").place(x=45, rely=0.49, relwidth=0.5)

# Lines 167-168 adds a date entry for the date of birth.
# This function has a frame function, font description, size, and place.
dob = DateEntry(center_frame, font=("Arial", 12), width=15)
dob.place(x=20, rely=0.62)

# Lines 172-173 creates a button for to submit and delete function.
# The button function has a frame placement, variable, font description, command, size, and placement.
Button(left_frame, text='Submit', font=labelfont, command=add_record, width=18).place(relx=0.025, rely=0.85)
Button(center_frame, text='Delete', font=labelfont, command=remove_record, width=15).place(relx=0.1, rely=0.85)

# Line 177 is a label function that put the label on the right frame of the gui.
# I added text, font description, background color, and placement into the label function.
Label(right_frame, text='Students Records', font=headlabelfont, bg='Gray90').pack(side=TOP, fill=X)

# Lines 182-184 has a treeview function which is a tabular representation of the data as it has all the properties
# of the table.Treeview has rows, columns, and heading similar to an Excel spreadsheet.
# This function is placed in the right frame, with a height, mode, and implementation of the columns for our varibles.
tree = ttk.Treeview(right_frame, height=100, selectmode=BROWSE,
                    columns=(
                        'Student ID', "Name", "Email Address", "Contact Number", "Gender", "Date of Birth", "Stream"))

# Lines 187-193 creates a scroll bar on the right side of the gui frame making it easier for users to view the data.
X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)

X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller.pack(side=RIGHT, fill=Y)

tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)


# Lines 200-217 showcase where each heading and column will be placed in the right frame for the database.
# This function carries a command, text, and anchor function as well as the number the data will start off with for the
# students ID,sizing, and stretch (to be able to expand the data table) and placement.
# Reference https://www.youtube.com/watch?v=AK1J8xF4fuk
tree.heading('Student ID', text='ID', anchor=CENTER)
tree.heading('Name', text='Name', anchor=CENTER)
tree.heading('Email Address', text='Email ID', anchor=CENTER)
tree.heading('Contact Number', text='Phone No', anchor=CENTER)
tree.heading('Gender', text='Gender', anchor=CENTER)
tree.heading('Date of Birth', text='DOB', anchor=CENTER)
tree.heading('Stream', text='Stream', anchor=CENTER)

tree.column('#0', width=0, stretch=NO)
tree.column('#1', width=40, stretch=NO)
tree.column('#2', width=140, stretch=NO)
tree.column('#3', width=200, stretch=NO)
tree.column('#4', width=80, stretch=NO)
tree.column('#5', width=80, stretch=NO)
tree.column('#6', width=80, stretch=NO)
tree.column('#7', width=150, stretch=NO)

tree.place(y=30, relwidth=1, relheight=0.9, relx=0)

# Line 220 displays the records function
display_records()

# Lines 223-224 finalizing, displays, and updates the GUI window
main.update()
main.mainloop()