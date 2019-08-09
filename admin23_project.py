from tkinter import messagebox as msg
from tkinter import *
from PIL import ImageTk,Image
import pyttsx3 as py
import sqlite3
import os
import getpass
import smtplib      #simple mail trasfer protocol
from email.mime.text import MIMEText   #multipurpose internet mail extension
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

root=Tk()
root.title('page 1')
frame=Frame(root,width=1366,height=768)
frame.place(x=0,y=0)
root.geometry('1366x768')

def xyz(event):
    tts=py.init()
    tts.say("fill your complete details")
    tts.runAndWait()
def main(root,frame):
    img=ImageTk.PhotoImage(Image.open('C:\\Users\\user\\Desktop\\typing_laptop_179161332-56b08e685f9b58b7d0240a17.jpg'))
    l=Label(frame,image=img)
    l.place(x=0,y=0)
    img2=ImageTk.PhotoImage(Image.open('C:\\Users\\user\\Desktop\\download (1).png'))
    l=Label(frame,image=img2)
    l.place(x=120,y=220)
    img3=ImageTk.PhotoImage(Image.open('C:\\Users\\user\\Desktop\\download (1).png'))
    l=Label(frame,image=img3)
    l.place(x=850,y=220)
    l=Label(frame,text="ADMIN",font=("algerian",40,'bold','underline'),fg='black',bg='gray84',bd=8,width=40,relief='raised')
    l.place(x=0,y=30)

    b1=Button(frame,text="REGISTER",font=("algerian",30,'bold','underline'),fg='black',bg='gray84',bd=6,width=11,command=lambda:register(root,frame))
    b1.place(x=120,y=380)
    b1.bind('<Button 1>',xyz)
    
    
    b2=Button(frame,text="LOGIN",font=("algerian",30,'bold','underline'),fg='black',bg='gray84',bd=6,width=11,command=lambda:login(root,frame))
    b2.place(x=850,y=380)
    
    frame.mainloop()

def register(root,frame):
    frame.destroy()
    frame=Frame(root,width=1366,height=768)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:\\Users\\user\\Desktop\\about-background.jpg'))
    l=Label(frame,image=img)
    l.place(x=0,y=0)
    l=Label(frame,text="TEACHER INFORMATION",font=("algerian",20,'bold','underline'),fg='black',bg='gray93',bd=8,width=80,relief='raised')
    l.place(x=0,y=20)
    l1=Label(frame,text="Enter Name",font=("algerian",25,'bold'),borderwidth=12,fg='black',bg='gray84',bd=14,width=20,relief='raised')
    l1.place(x=60,y=90)

    l2=Label(frame,text="Enter Email",font=("algerian",25,'bold'),borderwidth=12,fg='black',bg='gray84',bd=14,width=20,relief='raised')
    l2.place(x=60,y=180)

    l3=Label(frame,text="Enter Password",font=("algerian",25,'bold'),borderwidth=12,fg='black',bg='gray84',bd=14,width=20,relief='raised')
    l3.place(x=60,y=270)
    
    l4=Label(frame,text="Enter Phone_number",font=("algerian",25,'bold'),borderwidth=12,fg='black',bg='gray84',bd=14,width=20,relief='raised')
    l4.place(x=60,y=360)
    
    l5=Label(frame,text="Enter Address",font=("algerian",25,'bold'),borderwidth=12,fg='black',bg='gray84',bd=14,width=20,relief='raised')
    l5.place(x=60,y=450)
    
    l6=Label(frame,text="Enter qualification",font=("algerian",25,'bold'),borderwidth=12,fg='black',bg='gray84',bd=14,width=20,relief='raised')
    l6.place(x=60,y=540)


    e1=Entry(frame,bg='white',fg='black',width=50,bd=15,font=("Verdana 10 bold",12))
    e1.place(x=600,y=90)

    e2=Entry(frame,bg='white',fg='black',width=50,bd=15,font=("Verdana 10 bold",12))
    e2.place(x=600,y=180)

    e3=Entry(frame,show='*',bg='white',fg='black',width=50,bd=15,font=("Verdana 10 bold",12))
    e3.place(x=600,y=270)
    
    e4=Entry(frame,bg='white',fg='black',width=50,bd=15,font=("Verdana 10 bold",12))
    e4.place(x=600,y=360)
    
    e5=Entry(frame,bg='white',fg='black',width=50,bd=15,font=("Verdana 10 bold",12))
    e5.place(x=600,y=450)
    
    qualification=StringVar()
    qualification.set('select your qualification')
    e6=OptionMenu(frame,qualification,'B.tech','M.tech','B.Ed','PHD','BSC','MSC')
    e6.place(x=600,y=540)
    e6.config(width=73,height=2)
    
    b1=Button(frame,text="SUBMIT",command=lambda:submit1(root,frame,e1,e2,e3,e4,e5,qualification),font=("algerian",15,'bold','underline'),fg='black',bd=15,bg='gray76',padx=20,width=5)
    b1.place(x=1200,y=500)

    b2=Button(frame,text="BACK",command=lambda:back(root,frame),font=("algerian",15,'bold','underline'),fg='black',bd=15,bg='gray76',padx=20,width=5)
    b2.place(x=1200,y=600)

    frame.mainloop()

def submit1(root,frame,e1,e2,e3,e4,e5,qualification):
    t1=e1.get()
    t2=e2.get()
    t3=e3.get()
    t4=e4.get()
    t5=e5.get()
    t6=qualification.get()
    conn=sqlite3.connect("table.db")
    conn.execute('''create table if not exists tables1
    (Name TEXT,
    Email INTVAR,
    Password TEXT,
    Mobile_Number INT(10),
    Address INTVAR,
    Qualification TEXT);''')
    conn.execute('''Insert into tables1 VALUES(?,?,?,?,?,?)''',(t1,t2,t3,int(t4),t5,t6))
    conn.commit()

    ans=msg.askquestion('sucessfully registered','do you want to proceed')
    print(ans)
    if ans=='yes':
        next_page_register(root,frame)
    else:
        register(root,frame)
    frame.mainloop()

def next_page_register(root,frame):
    frame.destroy()
    frame=Frame(root,width=1366,height=768)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:\\Users\\user\\Desktop\\Clear_Best-Masters-in-Management-Information-Services.jpg'))
    l=Label(frame,image=img)
    l.place(x=0,y=0)
    l=Label(frame,text="UPDATE DATA",font=("algerian",20,'bold','underline'),fg='black',bg='honeydew2',bd=14,width=82,relief='raised')
    l.place(x=0,y=20)

    b3=Button(frame,text="Update Marks",font=("algerian",25,'bold'),bg='honeydew2',width=20,bd=15,command=lambda:update_marks(root,frame))
    b3.place(x=50,y=200)

    b4=Button(frame,text="Update Attendance",font=("algerian",25,'bold'),bg='honeydew2',width=20,bd=15,command=lambda:update_attendance(root,frame))
    b4.place(x=50,y=350)
    frame.mainloop()
    
def update_marks(root,frame):
    frame.destroy()
    frame=Frame(root,width=1366,height=768)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:\\Users\\user\\Desktop\\Clear_Best-Masters-in-Management-Information-Services.jpg'))
    l=Label(frame,image=img)
    l.place(x=0,y=0)
    l1=Label(frame,text="Enter Student name",font=("algerian",25,'bold'),borderwidth=3,fg='black',bg='honeydew2',width=20,relief='raised')
    l1.place(x=60,y=60)

    l2=Label(frame,text="Enter Rollnumber",font=("algerian",25,'bold'),borderwidth=3,fg='black',bg='honeydew2',width=20,relief='raised')
    l2.place(x=60,y=120)

    l3=Label(frame,text="Enter Year",font=("algerian",25,'bold'),borderwidth=3,fg='black',bg='honeydew2',width=20,relief='raised')
    l3.place(x=60,y=180)
                
    l4=Label(frame,text="Enter Semester",font=("algerian",25,'bold'),borderwidth=3,fg='black',bg='honeydew2',width=20,relief='raised')
    l4.place(x=60,y=240)
                
    l5=Label(frame,text="Enter Subject 1",font=("algerian",25,'bold'),borderwidth=3,fg='black',bg='honeydew2',width=20,relief='raised')
    l5.place(x=60,y=300)
    l6=Label(frame,text="Enter Subject 2",font=("algerian",25,'bold'),borderwidth=3,fg='black',bg='honeydew2',width=20,relief='raised')
    l6.place(x=60,y=360)
    l7=Label(frame,text="Enter Subject 3",font=("algerian",25,'bold'),borderwidth=3,fg='black',bg='honeydew2',width=20,relief='raised')
    l7.place(x=60,y=420)
    l8=Label(frame,text="Enter Subject 4",font=("algerian",25,'bold'),borderwidth=3,fg='black',bg='honeydew2',width=20,relief='raised')
    l8.place(x=60,y=480)
    l9=Label(frame,text="Enter Subject 5",font=("algerian",25,'bold'),borderwidth=3,fg='black',bg='honeydew2',width=20,relief='raised')
    l9.place(x=60,y=540)
    l10=Label(frame,text="Enter Subject 6",font=("algerian",25,'bold'),borderwidth=3,fg='black',bg='honeydew2',width=20,relief='raised')
    l10.place(x=60,y=600)

    l11=Label(frame,text="Total marks1",font=("times",8,'bold'),borderwidth=8,fg='black',bg='honeydew2',width=10,relief='raised')
    l11.place(x=750,y=300)
    l12=Label(frame,text="Total marks2",font=("times",8,'bold'),borderwidth=8,fg='black',bg='honeydew2',width=10,relief='raised')
    l12.place(x=750,y=360)
    l13=Label(frame,text="Total marks3",font=("times",8,'bold'),borderwidth=8,fg='black',bg='honeydew2',width=10,relief='raised')
    l13.place(x=750,y=420)
    l14=Label(frame,text="Total marks4",font=("times",8,'bold'),borderwidth=8,fg='black',bg='honeydew2',width=10,relief='raised')
    l14.place(x=750,y=480)
    l15=Label(frame,text="Total marks5",font=("times",8,'bold'),borderwidth=8,fg='black',bg='honeydew2',width=10,relief='raised')
    l15.place(x=750,y=540)
    l16=Label(frame,text="Total marks6",font=("times",8,'bold'),borderwidth=8,fg='black',bg='honeydew2',width=10,relief='raised')
    l16.place(x=750,y=600)

    l17=Label(frame,text="Obtained marks1",font=("times",8,'bold'),borderwidth=8,fg='black',bg='honeydew2',width=14,relief='raised')
    l17.place(x=905,y=300)
    l18=Label(frame,text="Obtained marks2",font=("times",8,'bold'),borderwidth=8,fg='black',bg='honeydew2',width=14,relief='raised')
    l18.place(x=905,y=360)
    l19=Label(frame,text="Obtained marks3",font=("times",8,'bold'),borderwidth=8,fg='black',bg='honeydew2',width=14,relief='raised')
    l19.place(x=905,y=420)
    l20=Label(frame,text="Obtained marks4",font=("times",8,'bold'),borderwidth=8,fg='black',bg='honeydew2',width=14,relief='raised')
    l20.place(x=905,y=480)
    l21=Label(frame,text="Obtained marks5",font=("times",8,'bold'),borderwidth=8,fg='black',bg='honeydew2',width=14,relief='raised')
    l21.place(x=905,y=540)
    l22=Label(frame,text="Obtained marks6",font=("times",8,'bold'),borderwidth=8,fg='black',bg='honeydew2',width=14,relief='raised')
    l22.place(x=905,y=600)

    e1=Entry(frame,bg='white',fg='black',width=64,bd=15,font=("Verdana 10 bold",10))
    e1.place(x=600,y=60)
                
    e2=Entry(frame,bg='white',fg='black',width=64,bd=15,font=("Verdana 10 bold",10))
    e2.place(x=600,y=120)
                          
    e3=Entry(frame,bg='white',fg='black',width=64,bd=15,font=("Verdana 10 bold",10))
    e3.place(x=600,y=180)

    e4=Entry(frame,bg='white',fg='black',width=64,bd=15,font=("Verdana 10 bold",10))
    e4.place(x=600,y=240)
                
    subject1=StringVar()
    subject1.set('select the subject')
    e5=OptionMenu(frame,subject1,'Cloud Computing','Information SYstem Securities','Data Mining And Ware Housing','CAD For VLSI','Computer Construction','Advance Database Management System')
    e5.place(x=600,y=300)
    e6=Entry(frame,bg='white',fg='black',width=4,bd=4,font=("Verdana",13,"bold"))
    e6.place(x=850,y=300)
    e7=Entry(frame,bg='white',fg='black',width=4,bd=4,font=("Verdana",13,"bold"))
    e7.place(x=1020,y=300)
    
    subject2=StringVar()
    subject2.set('select the subject')
    e8=OptionMenu(frame,subject2,'Cloud Computing','Information SYstem Securities','Data Mining And Ware Housing','CAD For VLSI','Computer Construction','Advance Database Management System')
    e8.place(x=600,y=360)
    e9=Entry(frame,bg='white',fg='black',width=4,bd=4,font=("Verdana",13,"bold"))
    e9.place(x=850,y=360)
    e10=Entry(frame,bg='white',fg='black',width=4,bd=4,font=("Verdana",13,"bold"))
    e10.place(x=1020,y=360)
    
    subject3=StringVar()
    subject3.set('select the subject')
    e11=OptionMenu(frame,subject3,'Cloud Computing','Information SYstem Securities','Data Mining And Ware Housing','CAD For VLSI','Computer Construction','Advance Database Management System')
    e11.place(x=600,y=420)
    e12=Entry(frame,bg='white',fg='black',width=4,bd=4,font=("Verdana",13," bold"))
    e12.place(x=850,y=420)
    e13=Entry(frame,bg='white',fg='black',width=4,bd=4,font=("Verdana",13,"bold"))
    e13.place(x=1020,y=420)
    
    subject4=StringVar()
    subject4.set('select the subject')
    e14=OptionMenu(frame,subject4,'Cloud Computing','Information SYstem Securities','Data Mining And Ware Housing','CAD For VLSI','Computer Construction','Advance Database Management System')
    e14.place(x=600,y=480)
    e15=Entry(frame,bg='white',fg='black',width=4,bd=4,font=("Verdana",13,"bold"))
    e15.place(x=850,y=480)
    e16=Entry(frame,bg='white',fg='black',width=4,bd=4,font=("Verdana",13,"bold"))
    e16.place(x=1020,y=480)
    
    subject5=StringVar()
    subject5.set('select the subject')
    e17=OptionMenu(frame,subject5,'Cloud Computing','Information SYstem Securities','Data Mining And Ware Housing','CAD For VLSI','Computer Construction','Advance Database Management System')
    e17.place(x=600,y=540)
    e18=Entry(frame,bg='white',fg='black',width=4,bd=4,font=("Verdana",13,"bold"))
    e18.place(x=850,y=540)
    e19=Entry(frame,bg='white',fg='black',width=4,bd=4,font=("Verdana",13,"bold"))
    e19.place(x=1020,y=540)
    
    
    subject6=StringVar()
    subject6.set('select the subject')
    e20=OptionMenu(frame,subject6,'Cloud Computing','Information SYstem Securities','Data Mining And Ware Housing','CAD For VLSI','Computer Construction','Advance Database Management System')
    e20.place(x=600,y=600)
    e21=Entry(frame,bg='white',fg='black',width=4,bd=4,font=("Verdana",13,"bold"))
    e21.place(x=850,y=600)
    e22=Entry(frame,bg='white',fg='black',width=4,bd=4,font=("Verdana",13,"bold"))
    e22.place(x=1020,y=600)

                
    b1=Button(frame,text="UPDATE",command=lambda:fun(root,frame,e1,e2,e3,e4,subject1,e6,e7,subject2,e9,e10,subject3,e12,e13,subject4,e15,e16,subject5,e18,e19,subject6,e21,e22),font=("algerian",15,'bold','underline'),fg='black',bd=15,bg='gray76',padx=20,width=5)
    b1.place(x=1200,y=50)
    b2=Button(frame,text="BACK",command=lambda:back(root,frame),font=("algerian",15,'bold','underline'),fg='black',bd=15,bg='gray76',padx=20,width=5)
    b2.place(x=1200,y= 140)

    #b3=Button(frame,text="Next",command=lambda:email(root,frame,e1,e2,e3,e4,subject1,e6,e7,subject2,e9,e10,subject3,e12,e13,subject4,e15,e16,subject5,e18,e19,subject6,e21,e22),font=("algerian",15,'bold','underline'),fg='black',bd=15,bg='gray76',padx=20,width=5)
    #b3.place(x=1200,y= 600)
    frame.mainloop()
def fun(root,frame,e1,e2,e3,e4,subject1,e6,e7,subject2,e9,e10,subject3,e12,e13,subject4,e15,e16,subject5,e18,e19,subject6,e21,e22):
    t1=e1.get()
    t2=e2.get()
    t3=e3.get()
    t4=e4.get()
    t5=subject1.get()
    t6=e6.get()
    t7=e7.get()
    t8=subject2.get()
    t9=e9.get()
    t10=e10.get()
    t11=subject3.get()
    t12=e12.get()
    t13=e13.get()
    t14=subject4.get()
    t15=e15.get()
    t16=e16.get()   
    t17=subject5.get()
    t18=e18.get()
    t19=e19.get()
    t20=subject6.get()
    t21=e21.get()
    t22=e22.get()
    conn=sqlite3.connect("table.db")
    cursor=conn.execute('''create table if not exists table3(Student_Name TEXT,Rollnumber INTVAR,Year int,Semester int,Sub_1 TEXT,Tot_Marks1 int,Ob_marks1 int,Sub_2 TEXT,Tot_Marks2 int,Ob_marks2 int,Sub_3 TEXT,Tot_Marks3 int,Ob_marks3 int,Sub_4 TEXT,Tot_Marks4 int,Ob_marks4 int,Sub_5 TEXT,Tot_Marks5 int,Ob_marks5 int,Sub_6 TEXT,Tot_Marks6 int,Ob_marks6 int);''')
    conn.execute('''Insert into table3 VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',[t1,t2,t3,t4,t5,int(t6),int(t7),t8,int(t9),int(t10),t11,int(t12),int(t13),t14,int(t15),int(t16),t17,int(t18),int(t19),t20,int(t21),int(t22)])
    conn.commit()
    email(root,frame,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22)
def email(root,frame,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21,t22):
    frame.destroy()
    frame1=Frame(root,width=1366,height=768)
    frame1.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:\\Users\\user\\Desktop\\about-background.jpg'))
    l=Label(frame1,image=img)
    l.place(x=0,y=0)
    conn=sqlite3.connect("major.db")
    n=conn.execute("select Parents_Email from major2 where Rollnumber='%s'"%t2)
    for i in n:
        print(i[0])
        c=i[0]
    #print(type(n))
    #print(n[0][0])
    
    
    content='Name: '+str(t1)+' \nRoll No.: '+str(t2)+' \nyear: '+str(t3)+' \nsemester: '+str(t4)+' \nsubject1: '+str(t5)+' \ntotalmarks1: '+str(t6)+' \nobtainedmarks1:  '+str(t7)+' \nsubject2: '+str(t8)+' \ntotalmarks2: '+str(t9)+' \nobtainedmarks2: '+str(t10)+' \nsubject3: '+str(t11)+' \ntotalmarks3: '+str(t12)+' \nobtainedmarks3: '+str(t13)+' \nsubject4: '+str(t14)+' \ntotalmarks4: '+str(t15)+' \nobtainedmarks4: '+str(t16)+' \nsuject5: '+str(t17)+' \ntotalmarks5: '+str(t18)+' \nobtainedmarks5: '+str(t19)+' \nsubject6: '+str(t20)+' \ntotalmarks6: '+str(t21)+' \nobtainedmarks6: '+str(t22)
    print(content)
    fp=open('msg.txt','a+')
    fp.truncate(0)
    for i in content:
        print(i)
        fp.write(i)
    fp.close()

    app_data = open('F:\\msg.txt','r+').read()
    msg = MIMEMultipart()    
    msg['Subject'] = 'python test code for document attachment'
    msg['From'] = '123jainashima@gmail.com'
    #password = getpass.getpass('enter password of email : ')
    msg['To'] =c
    body = MIMEText('python test code successfully sent')
    msg.attach(body)
    doc = MIMEApplication(app_data,name = os.path.basename('F:\\msg.txt'))
    msg.attach(doc)
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()    #enhanced high low output
    s.starttls()   #start time to live session
    s.login(msg['From'],'@123@789')
    s.sendmail(msg['From'],msg['To'],msg.as_string())
    s.quit()
    print('Email sent successfully')
    

    l1=Label(frame1,text="Enter Parents Email",font=("algerian",25,'bold'),borderwidth=12,fg='black',bg='gray84',width=20)
    l1.place(x=60,y=120)
    var1=StringVar()
    var1.set(c)
    e1=Entry(frame1,textvariable=var1,bg='white',fg='black',font=("Verdana",25,"bold"),borderwidth=12,width=20)
    e1.place(x=600,y=120)

    b1=Button(frame1,text="send",font=("algerian",25,'bold','underline'),fg='black',bg='gray84',bd=10,width=10)
    b1.place(x=200,y=500)
    b2=Button(frame1,text="BACK",command=lambda:back(root,frame1),font=("algerian",25,'bold','underline'),fg='black',bg='gray84',bd=10,width=10)
    b2.place(x=500,y=500)
    frame1.mainloop()
    
    
def login(root,frame):
    frame.destroy()
    frame=Frame(root,width=1366,height=768)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:\\Users\\user\\Desktop\\Attendence.png'))
    l=Label(frame,image=img)
    l.place(x=0,y=0)
    l=Label(frame,text="ADMIN LOGIN",font=("algerian",20,'bold','underline'),fg='black',bg='gray93',bd=12,width=80,relief='raised')
    l.place(x=0,y=20)

    l1=Label(frame,text="Enter Email",font=("algerian",25,'bold'),borderwidth=12,fg='black',bg='gray76',bd=14,width=20,relief='raised')
    l1.place(x=60,y=180)

    l2=Label(frame,text="Enter Password",font=("algerian",25,'bold'),borderwidth=12,fg='black',bg='gray76',bd=14,width=20,relief='raised')
    l2.place(x=60,y=290)
    e1=Entry(frame,bg='white',fg='black',width=50,bd=15,font=("Verdana 10 bold",12))
    e1.place(x=600,y=180)

    e2=Entry(frame,show='*',bg='white',fg='black',width=50,bd=15,font=("Verdana 10 bold",12))
    e2.place(x=600,y=290)

    b1=Button(frame,text="SUBMIT",command=lambda:loginsucess(root,frame,e1,e2),font=("algerian",15,'bold','underline'),fg='black',bd=15,bg='gray76',padx=20,width=5)
    b1.place(x=200,y=500)

    b2=Button(frame,text="BACK",command=lambda:back(root,frame),font=("algerian",15,'bold','underline'),fg='black',bd=15,bg='gray76',padx=20,width=5)
    b2.place(x=500,y=500)

    frame.mainloop()

def back(root,frame):
    main(root,frame)


def loginsucess(root,frame,e1,e2):
    txt1=e1.get()
    print(txt1)
    txt2=e2.get()
    print(txt2)
    conn=sqlite3.connect('table.db')
    cursor=conn.execute('select Email,Password from tables1')
    ans=msg.askquestion('Ask Question','do you want to proceed')
    print(ans)
    for row in cursor:
        print(row)
        if row[0]==txt1 and row[1]==txt2:
            print(row[0])
            print(row[1])
            print("login sucessfully")
            if ans=='yes':
                msg.showwarning('login sucessful','valid email or password')
                next_page_register(root,frame)
                 
            else:
                login(frame,root)
                
        else:
            msg.showwarning('login failed','invalid user name or password')
            login(root,frame)
    conn.commit()
    conn.close()
main(root,frame)


