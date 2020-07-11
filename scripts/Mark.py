from datetime import date
import csv
import os
import random

today=date.today()

roll={}
dept={}

path = 'Face Recog Pro//Students'
images=[]
classNames=[]
myList=os.listdir(path)
present={}
#print(myList)
for cl in myList:
    roll[os.path.splitext(cl)[0].upper()]=random.randint(1,100)
    dept[os.path.splitext(cl)[0].upper()]=random.choice(['Dark Arts','Herbology','Transfiguration','Potions','Charms'])
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
