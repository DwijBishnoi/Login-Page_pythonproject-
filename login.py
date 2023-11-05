from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql


# FUNCTIONALITY PART

def forget_pass():
    def change_password():
        if user_entry.get() == '' or newpass_entry.get() == '' or confirmpass_entry.get() == '':
            messagebox.showerror('ERROR', 'All Fields are Required', parent=window)
        elif newpass_entry.get() != confirmpass_entry.get():
            messagebox.showerror('ERROR', 'Password and Confirm Password are ot matching', parent=window)
        else:
            con = pymysql.connect(host='localhost', user='root', password='1234', database='userdata')
            mycursor = con.cursor()
            query = 'select * from data where username=%s'
            mycursor.execute(query, (user_entry.get()))
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('ERROR', 'Incorrect Username', parent=window)
            else:
                query = 'update data set password=%s where username=%s'
                mycursor.execute(query, (newpass_entry.get(), user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Password is reset,Please login with New Password', parent=window)
                window.destroy()

    window = Toplevel()
    window.title('Change Password')

    bgPic = ImageTk.PhotoImage(file='background.jpg')
    bgLabel = Label(window, image=bgPic)
    bgLabel.grid()

    heading_label = Label(window, text='RESET PASSWORD', font=('MV Boli', 18, 'bold'), bg='white', fg='magenta2')
    heading_label.place(x=480, y=60)

    userlabel = Label(window, text='Username', font=('Open Sans', 12, 'bold'), bg='white', fg='orchid1')
    userlabel.place(x=470, y=130)

    user_entry = Entry(window, width=25, fg='magenta2', font=('Open Sans', 10, 'bold'), bg='white', bd=0)
    user_entry.place(x=470, y=160)

    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=180)

    newpasslabel = Label(window, text='New Password', font=('Open Sans', 12, 'bold'), bg='white', fg='orchid1')
    newpasslabel.place(x=470, y=210)

    newpass_entry = Entry(window, width=25, fg='magenta2', font=('Open Sans', 10, 'bold'), bg='white', bd=0)
    newpass_entry.place(x=470, y=240)

    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=260)

    confirmpasslabel = Label(window, text='Confirm Password', font=('Open Sans', 12, 'bold'), bg='white', fg='orchid1')
    confirmpasslabel.place(x=470, y=290)

    confirmpass_entry = Entry(window, width=25, fg='magenta2', font=('Open Sans', 12, 'bold'), bg='white', bd=0)
    confirmpass_entry.place(x=470, y=320)

    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=340)

    submitButton = Button(window, text='Submit', font=('Open Sans', 15, 'bold'), fg='white', bg='VioletRed4',
                          activeforeground='white', activebackground='VioletRed4', cursor='hand2', bd=0, width=19,
                          command=change_password)

    submitButton.place(x=470, y=390)

    window.mainloop()


def login_user():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('ERROR', 'All Fields are Required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='1234')
            mycursor = con.cursor()
        except:
            messagebox.showerror('ERROR', 'Connection is not established yet,Try Again')
            return

        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from data where username=%s and password=%s'
        mycursor.execute(query, (usernameEntry.get(), passwordEntry.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('ERROR', 'Invalid Userame or Password')
        else:
            messagebox.showinfo('WELCOME', 'Login is Successful')


def signup_page():
    login_window.destroy()
    import signup


def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


def user_enter(event):
    if usernameEntry.get() == "Username":
        usernameEntry.delete(0, END)


def password_enter(event):
    if passwordEntry.get() == "Password":
        passwordEntry.delete(0, END)


# GUI PART
login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0, 0)
login_window.title('Login Page')
bgImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(login_window, text='Student Assitant', font=('MV Boli', 23, 'bold'), bg='white')
heading.place(x=570, y=120)

usernameEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0)
usernameEntry.place(x=567, y=200)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_enter)
frame1 = Frame(login_window, width=250, height=2, bg='firebrick1').place(x=567, y=222)

passwordEntry = Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0)
passwordEntry.place(x=567, y=260)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_enter)
frame2 = Frame(login_window, width=250, height=2, bg='firebrick1').place(x=567, y=282)

openeye = PhotoImage(file='openeye.png')
eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2',
                   command=hide)
eyeButton.place(x=800, y=255)
forgetButton = Button(login_window, text='Forgot Password?', bd=0, bg='white', activebackground='white', cursor='hand2',
                      font=('Microsoft Yahei UI Light', 9, 'bold'), command=forget_pass)
forgetButton.place(x=700, y=295)

loginButton = Button(login_window, text='Login', font=('Open Sans', 15, 'bold'), fg='white', bg='VioletRed4',
                     activeforeground='white', activebackground='VioletRed4', cursor='hand2', bd=0, width=19,
                     command=login_user)
loginButton.place(x=578, y=350)

orLabel = Label(login_window, text='---------- OR ----------', font=('Open Sans', 15), bg='white')

orLabel.place(x=598, y=400)

google_logo = PhotoImage(file='google.png')

googleLabel = Label(login_window, image=google_logo, bg='white').place(x=670, y=440)
twitter_logo = PhotoImage(file='twitter.png')

twitterLabel = Label(login_window, image=twitter_logo, bg='white').place(x=720, y=440)

facebook_logo = PhotoImage(file='facebook.png')

fbLabel = Label(login_window, image=facebook_logo, bg='white').place(x=620, y=440)

signupLabel = Label(login_window, text='Dont have an account? ', font=('Open Sans', 9, 'bold'), fg='white',
                    bg='VioletRed4', activeforeground='white', activebackground='white', cursor='hand2', bd=0, )

signupLabel.place(x=588, y=500)

newaccountButton = Button(login_window, text='Create New Account', font=('Open Sans', 8, 'bold underline'), fg='blue',
                          activeforeground='white', activebackground='white', cursor='hand2', bd=0, command=signup_page)

newaccountButton.place(x=727, y=498)

login_window.mainloop()
