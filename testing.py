import cv2
import os


def capture():
    label=[]
    dir1='C:/Users/shree/Desktop/Python/Projects/Face Detection/training_data'
    for x,y,z in os.walk(dir1):
        for a in y:
            label.append(int(a))

    i=max(label)
    i=i+1
    os.chdir('training_data')
    os.mkdir(str(i))
    print(os.getcwd())
               
if __name__=='__main__':
    capture()

    
