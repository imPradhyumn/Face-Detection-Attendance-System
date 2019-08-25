import cv2
from numpy import array
import os,time
from mark_attendance import save_attendance

def facedetect(image):
    img_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cascade=cv2.CascadeClassifier('xml\haarcascade_frontalface_default.xml')
    faces=cascade.detectMultiScale(img_gray,scaleFactor=1.1,minNeighbors=5)

    return faces,img_gray

def create_labels():
    dir1='C:/Users/shree/AppData/Local/Programs/Python/Python36/Face Detection/training_data'
    faces_list=[]
    fid=[]
    temp=''
    names=[]

    for path,subdir,files in os.walk(dir1):
        name=''
        for f in files:
            if f.startswith('.'):
                continue
            image_path=os.path.join(path,f)
            img_id=os.path.basename(path)
            
            img=cv2.imread(image_path)
            img_re=cv2.resize(img,(1000,600))
            faces,img_gray=facedetect(img_re)

            if (len(faces)!=1):
                continue
            
            x,y,w,h=faces[0]
            req_region=img_gray[y:y+w,x:x+h]
            faces_list.append(req_region)
            fid.append(int(img_id))
            temp=f
            
        for char in temp:
            if char.isdigit():
                break
            else:
                name=name+char
        names.append(name)
    names.remove('')
    
    names_dic=dict(zip(set(fid),names))
    
    return faces_list,fid,names_dic

            
def trainer(faces_list,fid):
    trainer=cv2.face.LBPHFaceRecognizer_create()
    trainer.train(faces_list,array(fid))
    return trainer

def rectangle(face,image):
    x,y,w,h=face
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)

def text(image,text,x,y):
    font=cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(image,text,(x-15,y-40),font,1,(255,0,0),2)
    

#dic={0:'Pradhyumn',1:'B'}

faces_list,fid,names_dic=create_labels()
classifier=trainer(faces_list,fid)

all_labels=[]

#test_prediction
'''img_test=cv2.imread('test.jpg')
faces,img_gray_test=facedetect(img_test)

for f in faces:
    (x,y,w,h)=f
    req_region=img_gray_test[y:y+w,x:x+h]
    label,confi=classifier.predict(req_region)
    all_labels.append(names_dic[label].capitalize())
    rectangle(f,img_gray_test)
    text(img_gray_test,names_dic[label].capitalize(),x,y)


cv2.imshow('Gray',img_gray_test)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

def start_detection(subject='Testing'):
    #live_prediction
    cam=cv2.VideoCapture(0)
    ch=1
    while True:
        ret,frame=cam.read()
        faces,img_gray_test=facedetect(frame)

        for f in faces:
            (x,y,w,h)=f
            req_region=img_gray_test[y:y+w,x:x+h]
            label,confi=classifier.predict(req_region)
            all_labels.append(names_dic[label].capitalize())
            rectangle(f,img_gray_test)
            text(img_gray_test,names_dic[label].capitalize(),x,y)
            
        cv2.imshow('Gray',img_gray_test)
        
        if cv2.waitKey(10)==ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()

    mark_attendance(all_labels,subject)

if __name__=='__main__':
    start_detection(subject)
