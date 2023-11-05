from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmpasswordEntry.delete(0,END)
    check.set(0)
def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('ERROR','All Fields are Required')
    elif passwordEntry.get() != confirmpasswordEntry.get():
        messagebox.showerror('ERROR', 'Password Mismatched')
    elif check.get()==0:
        messagebox.showerror('ERROR', 'Please Accept Terms & Conditions')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='1234')
            mycursor=con.cursor()
        except:
            messagebox.showerror('ERROR', 'Database Connectivity Issue,Try Again')
            return

        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table data(id int auto_increment primary key not null, email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')

        query='select * from data where username=%s'
        mycursor.execute(query,(usernameEntry.get()))

        row=mycursor.fetchone()
        if row!=None:
            messagebox.showerror('ERROR', 'Userame already exists')


        else:
            query = 'insert into data(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is Successful')
            clear()
            signup_window.destroy()
            import login

def login_page():
    signup_window.destroy()
    import login


signup_window=Tk()
signup_window.title('Signup Page')
signup_window.resizable(False,False)

background=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(signup_window,image=background)
bgLabel.grid()

frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)

heading=Label(frame,text='Create An Account',font=('MV Boli',22,'bold'),bg='white',fg='gray1')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel=Label(frame,text='Email',font=('Open Sans',10,'bold'),bg='white',fg='VioletRed4')
emailLabel.grid(row=1,column=0,sticky='w',padx=25)
emailEntry=Entry(frame,width=30,font=('Open Sans',10,'bold'),bg='white',fg='RoyalBlue3')
emailEntry.grid(row=2,column=0,sticky='w',padx=25,pady=(10,0))


usernameLabel=Label(frame,text='Username',font=('Open Sans',10,'bold'),bg='white',fg='VioletRed4')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
usernameEntry=Entry(frame,width=30,font=('Open Sans',10,'bold'),bg='white',fg='RoyalBlue3')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)


passwordLabel=Label(frame,text='Password',font=('Open Sans',10,'bold'),bg='white',fg='VioletRed4')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))
passwordEntry=Entry(frame,width=30,font=('Open Sans',10,'bold'),bg='white',fg='RoyalBlue3')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)


confirmpasswordLabel=Label(frame,text='Confirm password',font=('Open Sans',10,'bold'),bg='white',fg='VioletRed4')
confirmpasswordLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))
confirmpasswordEntry=Entry(frame,width=30,font=('Open Sans',10,'bold'),bg='white',fg='RoyalBlue3')
confirmpasswordEntry.grid(row=8,column=0,sticky='w',padx=25)

check=IntVar()
termsandcondition=Checkbutton(frame,text='I agree to the Terms & Conditions',font=('Open Sans',8,'bold'),bg='white',fg='VioletRed4',activebackground='white',activeforeground='VioletRed4',cursor='hand2',variable=check)
termsandcondition.grid(row=9,column=0,pady=10,padx=15)


signupButton=Button(frame,text='Signup',font=('Open Sans',16,'bold'),bd=0,bg='cyan3',fg='black',activeforeground='black',activebackground='cyan3',width=17,command=connect_database)
signupButton.grid(row=10,column=0)


alreadyaccount=Label(frame,text='dont have an account?',font=('Open Sans',10,'bold'),bd=0,bg='white',fg='VioletRed4')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25)


loginButton=Button(frame,text='Log in',font=('Open Sans',10,'bold underline'),bd=0,bg='white',fg='blue',cursor='hand2',activeforeground='blue',activebackground='white',command=login_page)
loginButton.grid(row=12,column=0)



signup_window.mainloop()