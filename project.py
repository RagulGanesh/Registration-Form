from tkinter import*
import re
from tkinter import messagebox
import sqlite3
def add_new():
    fname_entry.delete(0,END)
    email_entry.delete(0,END)
    age_entry.delete(0,END)
    get_gender.set(False)
    get_chkbtn.set(False)
    number_entry.delete(0,END)

def msg_num():
    messagebox.showinfo("Error","Enter 10 digit phone number")  
def msg_email():
    messagebox.showinfo("Error","Enter correct email address") 
def msg_chkbtn():
    messagebox.showinfo("Error","Check the terms and conditions")
#def msg_caps():
    #messagebox.showinfo("Error","Only Uppercase applicable")
def msg_exists():
    messagebox.showinfo("Error","User already exists")  
def msg_registered():
    messagebox.showinfo("Info","Registered Successfully!!!")      
def submit():
    global flag
    name=fname_entry.get()
    email=email_entry.get()
    age=age_entry.get()    
    number=number_entry.get()
    b=get_gender.get()
    pattern1=r"\d{10}\b" 
    pattern2=r"[\w.-]+@[\w.-]+"
    #if get_fn.islower():
        #msg_caps()     
    if re.match(pattern1,number)==None:
        msg_num()
    if re.match(pattern2,email)==None:
        msg_email()
    if get_chkbtn.get()==0:
        msg_chkbtn()     
    if b==1:
        put="Male"
    else:
        put="Female" 
    #with open("StudentRegistrationForm.txt","a") as f:
        #f.write("{},{},{},{},{}".format(get_fn,get_em,get_age,put,get_number)) 
        #f.write("\n")              
    #if re.match(pattern1,get_number) and re.match(pattern2,get_em) and get_chkbtn.get()==1:
        #print(get_fn,get_em,get_age,put,get_number)
        # with open("StudentRegistrationForm.txt","a") as f:
        #     f.write("{},{},{},{},{}".format(get_fn,get_em,get_age,put,get_number)) 
        #     f.write("\n")  
        #file=open("StudentRegistrationForm.csv","a")
        #file.write("{},{},{},{},{}".format(get_fn,get_em,get_age,put,get_number))
        #file.write("\n")
        #file.close()
    '''flag=0    
    if re.match(pattern1,get_number) and re.match(pattern2,get_em) and get_chkbtn.get()==1:
        with open("StudentRegistrationForm.csv","r") as file:
            for line in file:
                k=line.strip(",")
                print(k)
                if get_fn in k and get_em in k and get_age in k and get_number in k:
                    msg_exists()
                    flag=1

        if flag==0:
           with open("StudentRegistrationForm.csv","a+") as f:
                    f.write("{},{},{},{},{}".format(get_fn,get_em,get_age,put,get_number))
                    f.write("\n")
                    print(get_fn,get_em,get_age,put,get_number)'''
    if re.match(pattern1,number) and re.match(pattern2,email) and get_chkbtn.get()==1:                
        conn=sqlite3.connect('Registration Form.sqlite')
        cur=conn.cursor()
        flag=0
        cur.execute('CREATE TABLE IF NOT EXISTS Admission (name TEXT(128),email TEXT(128),age INT,mnum BIGINT,gender TEXT(128))')
        cur.execute('SELECT email,mnum FROM Admission')  
        row=cur.fetchall()
        for i in row:
            if i[0]==email:
                flag=1
                break
            if i[1]==int(number):
                flag=1
                break
        if flag==1:
            msg_exists()        
        else:
            cur.execute('''INSERT OR IGNORE INTO Admission (name,email,age,mnum,gender) VALUES (?,?,?,?,?)''',(name,email,age,number,put))
            msg_registered()

        conn.commit()         
           
    #if row==None:
        #cur.execute('''INSERT OR IGNORE INTO Admission (name,email,age,mnum,gender) VALUES (?,?,?,?,?)''',(name,email,age,number,put))
        #msg_registered()
    '''flag_test1=flag_test2=0    
    for i in row:
       # print(i[0],i[1])
        if  i[1]==number or i[0]==email: 
            flag=1
            if i[1]==number_entry.get():
                flag_test1+=1
                print('number',flag_test1,i[1])
            else: 
                print('number',flag_test1,i[1]) 
            if i[0]==email:
                flag_test2+=1
                print('email',flag_test2,i[0])
            else: 
                print('email',flag_test2,i[0])    
                   
            break

        if  i[1]==number:
            flag=1
            break'''

            #cur.execute('''INSERT OR IGNORE INTO Admission (name,email,age,mnum,gender) VALUES (?,?,?,?,?)''',(name,email,age,number,put))
            #msg_registered()
                     

         
     
root = Tk()
get_fn=StringVar
get_em=StringVar
get_gender=IntVar()
get_age=StringVar
get_number=StringVar
get_chkbtn=IntVar()
root.geometry('500x550')
root.resizable(0,0)
root.title("Registration Form")

title = Label(root, text="Registration form",width=20,font=("Comic Sans MS",20,"underline"),fg="red",)
title.place(x=90,y=53)

fullname = Label(root, text="FullName",width=20,font=("Comic Sans MS",15))
fullname.place(x=35,y=130)

fname_entry = Entry(root)
fname_entry.place(x=240,y=135)

email = Label(root, text="Email",width=20,font=("Comic Sans MS",15))
email.place(x=18,y=180)

email_entry = Entry(root)
email_entry.place(x=240,y=190)

gender = Label(root, text="Gender",width=20,font=("Comic Sans MS",15))
gender.place(x=28,y=230)

# var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=get_gender, value=1,font=("Comic Sans MS",15)).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=get_gender, value=2,font=("Comic Sans MS",15)).place(x=320,y=230)

age= Label(root, text="Age",width=20,font=("Comic Sans MS",15))
age.place(x=10,y=280)

age_entry= Entry(root)
age_entry.place(x=240,y=290)


number = Label(root, text="Mobile No.",width=20,font=("Comic Sans MS",15))
number.place(x=40,y=320)

number_entry= Entry(root)
number_entry.place(x=240,y=330)

sub1=Button(root, text='Submit',width=20,bg='brown',fg='white',command=submit,font=("Comic Sans MS",10)).place(x=80,y=440)
sub2=Button(root, text='Close',width=20,bg='brown',fg='white',command=root.destroy,font=("Comic Sans MS",10)).place(x=260,y=440)
sub3=Button(root, text='Add New Entry',width=20,bg='brown',fg='white',command=add_new,font=("Comic Sans MS",10)).place(x=80,y=480)
sub4=Button(root, text='Clear',width=20,bg='brown',fg='white',command=add_new,font=("Comic Sans MS",10)).place(x=260,y=480)
get_chkbtn=IntVar()
Checkbutton(root, text="Terms and Condition", variable=get_chkbtn,font=("Comic Sans MS",15)).place(x=150,y=375)
root.mainloop()
