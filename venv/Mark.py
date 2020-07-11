from datetime import date
import csv
import os

today=date.today()

roll={'DIBYENDU':48,'SANGRAMJIT':17, 'SUBHRA':9,'SUBRATA':21}
dept={'DIBYENDU':"CSE",'SANGRAMJIT':"IT", 'SUBHRA':"IT",'SUBRATA':'CSE'}

path = 'Face Recog Pro//ImageAttendance'
images=[]
classNames=[]
myList=os.listdir(path)
present={}
#print(myList)
for cl in myList:
    present[os.path.splitext(cl)[0].upper()]=0


try:
    f=open('Face Recog Pro//Attendance.csv','r')
    raw_data=f.readlines()
    for lines in range(1,len(raw_data)):
        present[raw_data[lines].split(',')[2].upper()]=1
except:
    f=open('Face Recog Pro//Attendance.csv','w')
    f.write('Date, Roll, Name, Dept \n')
f.close()


def attended(name):
    f=open('Face Recog Pro//Attendance.csv','a+')
    if (present[name.upper()]==0):
            
        f.write(today.strftime("%d/%m/%Y")+","+str(roll[name])+","+name+","+dept[name]+'\n')
        present[name.upper()]=1
        print("Present:",sum(present.values()))
        f.close()
    #df=pd.read_csv('Attendance.csv')
    #df.to_csv("Attendance.csv",header=["Date","Roll","Name","Dept"])
#open("Attendance.csv",'a+')
