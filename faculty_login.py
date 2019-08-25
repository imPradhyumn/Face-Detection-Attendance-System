from tkinter import *
from tkinter import messagebox
import time
from pandas import read_csv
import face_detection as FD

localtime = time.asctime( time.localtime(time.time()) )
localtime=localtime.split()
x=localtime[1]+' '+localtime[2]+', '+localtime[-1]
localtime.pop(1)
localtime.pop(1)
localtime.pop(-1)
localtime.insert(1,x)
x=localtime[2][:5]
localtime.pop(-1)
localtime.insert(2,x)
localtime=', '.join(localtime)

def logout(root):
    root.destroy()
    get_login_info()

    
def take_attendance(subject):
    FD.start_detection(subject)
    
def logging_in(root,subject):
    root.destroy()
    root=Tk()
    root.title('Attendance Panel')
    root.geometry('460x500+400+100')
    frame1=Frame(root,height=100)
    label=Label(frame1,text=' Attendance Panel ',bg='orange',fg='white',relief=SUNKEN,\
                font=('comic sans ms',23,'bold')).pack()
    label=Label(frame1,text=' Subject : '+subject,relief=RIDGE,\
                bg='white',fg='red',font=('comic sans ms',15)).pack(pady=10)
    frame1.pack(fill=X,pady=50)

    frame1=Frame(root,height=100)
    bt1=Button(frame1,text='Take Attendance',font=('Verdana',15,'bold'),\
               command=lambda : take_attendance(subject)).pack()
    frame1.pack(fill=X,pady=10)

    frame1=Frame(root,height=100)
    bt1=Button(frame1,text='Show Attendance',font=('Verdana',15,'bold')).pack()
    frame1.pack(fill=X,pady=10)

    frame1=Frame(root,height=100)
    bt1=Button(frame1,text='Edit Attendance',font=('Verdana',15,'bold')).pack()
    frame1.pack(fill=X,pady=10)

    frame1=Frame(root,bg='red',height=50)
    bt1=Button(frame1,text='Log Out',font=('Verdana',12,'bold'),\
               command=lambda:logout(root))
    bt1.pack()
    frame1.pack(side=RIGHT,fill=X,padx=75,pady=15)
    root.mainloop()

    
def login_check(entry1,entry2,root):
    username=entry1.get()
    passw=entry2.get()
    df=read_csv('login_credentials.csv',index_col='Username')
    pass_chk=df.loc[username]['Password']
    if passw==pass_chk:
        subject=df.loc[username]['Subject']
        logging_in(root,subject)
    else:
        messagebox.showinfo('Alert','Login credentials not matched !!')
        
      

def close_win(root):
    root.destroy()

def get_login_info():
    root=Tk()
    root.geometry('700x500')
    root.title('Login Window')
    root1=Frame(root,width=100,height=100)
    label1=Label(root1,text=' Faculty Login ',\
                 bg='purple',fg='white',font=('Comic sans',18,'bold'),\
                 relief=SUNKEN,\
                 height=2,width=18)
    label1.pack()
    label1=Label(root1,text='\n'+localtime,\
                 font=('Comic sans',15))
    label1.pack()
    root1.pack(fill=X,pady=50)

    root2=Frame(root,width=100,height=50)
    label2=Label(root2,text='Username : ',font=('Verdana',11,'bold'))
    label2.pack(side=LEFT)

    entry1=Entry(root2,font=('Verdana',11))
    entry1.pack(side=LEFT)
    root2.pack(fill=X,padx=190)

    root3=Frame(root,width=100,height=100)
    label3=Label(root3,text='Password : ',font=('Verdana',11,'bold'))
    label3.pack(side=LEFT)

    entry2=Entry(root3,font=('Verdana',11))
    entry2.pack(side=LEFT)
    root3.pack(fill=X,pady=15,padx=194)

    root4=Frame(root,width=100,height=100,bd=4)
    submit=Button(root4,text='Login',font=('Verdana',11,'bold'),\
                  command=lambda:login_check(entry1,entry2,root),\
                  bg='yellow',fg='black',width=5)
    submit.grid(row=0,column=0)
    submit=Button(root4,text='Exit',font=('Verdana',11,'bold'),\
                  bg='blue',fg='white',width=5,command=lambda:close_win(root))
    submit.grid(row=0,column=3,padx=50)
    root4.pack(fill=X,pady=20,padx=250)

    root.mainloop()

if __name__=='__main__':
    get_login_info()
