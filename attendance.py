from pandas import read_csv
import datetime as dt

def mark_attendance(names):
    names=set(names)
    print(names)
    df=read_csv('attendance_data/attendance.csv',index_col='Name')
    
    today=dt.datetime.now()
    today=today.strftime('%d/%m/%y')
    
    student_status=['Nil' for i in range(len(df))]
    
    df[today]=student_status
    
    for i in names:
        df.loc[i]['25/08/19']='Yes'
    df.to_csv('attendance_data/attendance.csv')
    df.to_excel(r'attendance_data/attendance.xlsx',header=True)




