import cv2
from tkinter import *
from tkinter import messagebox
import os
from time import sleep

def create_dir():
    label=[]
    dir1=os.getcwd()+'/training_data'
    for x,y,z in os.walk(dir1):
        for a in y:
            label.append(int(a))
    if label==[]:
        i='0'
    else:
        i=max(label)
        i=i+1
        
    os.chdir('training_data')
    os.mkdir(str(i))
    os.chdir(str(i))
        
    return os.getcwd()

def capture_pic(root,entry1):
    name=entry1.get()
    root.destroy()
    cwd=create_dir()
    cam=cv2.VideoCapture(0)
    ch=1
    while True:
        ret,frame=cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Capturing',gray)
        cv2.imwrite(name+str(ch)+'.jpg',cv2.flip(gray, 1 ))
        ch=ch+1
        if ch>10:
            break
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
    cam.release()
    root=Tk()
    root.geometry('0x0')
    root.title('Alert')
    messagebox.showinfo('Alert','Data Captured !!')
    root.destroy()
    cv2.destroyAllWindows()
    window()
    
def window():
    root=Tk()
    root.geometry('500x170+400+300')
    root.title('Face Capture')
    frame=Frame(root)
    label=Label(frame,text='Face Capture ',font=('Verdana',15,'bold'))
    label.pack(pady=30)
    label=Label(frame,text='Student Name : ',font=('Verdana',11,'bold'))
    label.pack(side=LEFT)
    entry1=Entry(frame,font=('Verdana',11))
    entry1.pack(side=LEFT)
    bt=Button(frame,text='Capture',font=('Verdana',9,'bold'),\
              bg='blue',fg='white',width=7,command=lambda:capture_pic(root,entry1))
    bt.pack(padx=20)
    frame.pack()
    root.mainloop()
    
    
if __name__=='__main__':
    window()

    
