import sqlite3
from tkinter import messagebox as msg
from tkinter import *
from PIL import ImageTk,Image
import pyttsx3 as py
import scrolling_area
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
    img=ImageTk.PhotoImage(Image.open('C:\\Users\\user\\Desktop\\student-849825__340.jpg'))
    l=Label(frame,image=img)
    l.place(x=0,y=0)
    img2=ImageTk.PhotoImage(Image.open('C:\\Users\\user\\Desktop\\download (1).png'))
    l=Label(frame,image=img2)
    l.place(x=120,y=180)
    img3=ImageTk.PhotoImage(Image.open('C:\\Users\\user\\Desktop\\download (1).png'))
    l=Label(frame,image=img3)
    l.place(x=850,y=180)
#name of project
    l=Label(frame,text="Friendance",font=("algerian",50,'bold','underline'),fg='white',bg='gray10',bd=10,width=35,relief='raised')
    l.place(x=0,y=10)

    b1=Button(frame,text="REGISTER",font=("algerian",30,'bold','underline'),fg='white',bg='black',bd=15,padx=20,width=9,command=lambda:register(root,frame))
    b1.place(x=120,y=355)
    b1.bind('<Button 1>',xyz)
    
    b2=Button(frame,text="LOGIN",font=("algerian",30,'bold','underline'),fg='white',bd=15,bg='black',padx=20,width=9,command=lambda:login(root,frame))
    b2.place(x=850,y=355)

    frame.mainloop()


def register(root,frame):
    frame.destroy()
    frame=Frame(root,width=1366,height=768)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:\\Users\\user\\Desktop\\technical.jpg'))
    l=Label(frame,image=img)
    l.place(x=0,y=0)
    img1=ImageTk.PhotoImage(Image.open('C:\\Users\\user\\Desktop\\download.jpg'))
    l=Label(frame,image=img1)
    l.place(x=600,y=600)
    
    l=Label(frame,text="STUDENT REGISTER",font=("algerian",20,'bold','underline'),fg='black',bg='gold',bd=5,width=80,relief='raised')
    l.place(x=0,y=10)

    

    l1=Label(frame,text="Enter Name",font=("algerian",20,'bold'),borderwidth=12,fg='black',bg='cyan',bd=10,width=20,relief='raised')
    l1.place(x=20,y=60)

    l2=Label(frame,text="Enter Rollnumber",font=("algerian",20,'bold'),fg='black',bg='cyan',bd=10,width=20,relief='raised')
    l2.place(x=20,y=120)

    l3=Label(frame,text="Enter Branch",font=("algerian",20,'bold'),fg='black',bd=10,bg='cyan',width=20,relief='raised')
    l3.place(x=20,y=180)

    l4=Label(frame,text="Enter Semester",font=("algerian",20,'bold'),fg='black',bd=10,bg='cyan',width=20,relief='raised')
    l4.place(x=20,y=240)

    l5=Label(frame,text="Enter Year",font=("algerian",20,'bold'),fg='black',bd=10,bg='cyan',width=20,relief='raised')
    l5.place(x=20,y=300)


    l6=Label(frame,text="Enter Student_Email",font=("algerian",20,'bold'),fg='black',bd=10,bg='cyan',width=20,relief='raised')
    l6.place(x=20,y=360)
    
    l7=Label(frame,text="Enter Parents_Email",font=("algerian",20,'bold'),fg='black',bd=10,bg='cyan',width=20,relief='raised')
    l7.place(x=20,y=420)


    l8=Label(frame,text="Enter Password",font=("algerian",20,'bold'),fg='black',bd=10,bg='cyan',width=20,relief='raised')
    l8.place(x=20,y=480)

    l9=Label(frame,text="Address",font=("algerian",20,'bold'),fg='black',bd=10,bg='cyan',width=20,relief='raised')
    l9.place(x=20,y=540)

    l10=Label(frame,text="Phone Number",font=("algerian",20,'bold'),fg='black',bd=10,bg='cyan',width=20,relief='raised')
    l10.place(x=20,y=600)

    e1=Entry(frame,bg='white',fg='black',width=50,bd=15,font=("Verdana 10 bold",12))
    e1.place(x=500,y=60)

    e2=Entry(frame,bg='white',fg='black',width=50,bd=15,font=("Verdana 10 bold",12))
    e2.place(x=500,y=120)
    
    branch=StringVar()
    branch.set('select the branch')
    e3=OptionMenu(frame,branch,'cse','ece','ee','civil')
    e3.place(x=500,y=180)
    e3.config(width=71,bd=7)

    year=IntVar()
    year.set('select the semester')
    e4=OptionMenu(frame,year,'1','2','3','4','5','6','7','8')
    e4.place(x=500,y=240)
    e4.config(width=71,bd=7)
    

    e5=Entry(frame,bg='white',fg='black',width=50,bd=15,font=("Verdana 10 bold",12))
    e5.place(x=500,y=300)

    e6=Entry(frame,bg='white',fg='black',width=50,bd=15,font=("Verdana 10 bold",12))
    e6.place(x=500,y=360)

    e7=Entry(frame,bg='white',fg='black',width=50,bd=15,font=("Verdana 10 bold",12))
    e7.place(x=500,y=420)

    e8=Entry(frame,show='*',bg='white',fg='black',width=50,bd=15,font=("Verdana 10 bold",12))
    e8.place(x=500,y=480)
    
    e9=Entry(frame,bg='white',fg='black',width=50,bd=15,font=("Verdana 10 bold",12))
    e9.place(x=500,y=540)
    
    e10=Entry(frame,bg='white',fg='black',width=50,bd=15,font=("Verdana 10 bold",12))
    e10.place(x=500,y=600)

    b1=Button(frame,text="SUBMIT",command=lambda:fun(root,frame,e1,e2,branch,year,e5,e6,e7,e8,e9,e10),font=("algerian",15,'bold','underline'),fg='black',bd=15,bg='salmon',padx=20,width=5)
    b1.place(x=1200,y=90)

    b2=Button(frame,text="BACK",command=lambda:back(root,frame),font=("algerian",15,'bold','underline'),fg='black',bd=15,bg='salmon',padx=20,width=5)
    b2.place(x=1200,y=180)

    frame.mainloop()

def fun(root,frame,e1,e2,branch,year,e5,e6,e7,e8,e9,e10):
    t1=e1.get()
    t2=e2.get()
    t3=branch.get()
    t4=year.get()
    t5=e5.get()
    t6=e6.get()
    t7=e7.get()
    t8=e8.get()
    t9=e9.get()
    t10=e10.get()
    
    conn=sqlite3.connect("major.db")
    cursor=conn.execute('''create table if not exists major2
    (Student_Name TEXT,
    Rollnumber INTVAR PRIMARY KEY,
    Branch TEXT,
    Semester int,
    Year int,
    Student_Email intvar,
    Parents_Email intvar,
    Password intvar,
    Address intvar,
    Mobile_Number int(10));''')
    conn.execute('''Insert into major2 VALUES(?,?,?,?,?,?,?,?,?,?)''',(t1,t2,t3,int(t4),int(t5),t6,t7,t8,t9,int(t10)))
    conn.commit()
    ans=msg.askquestion('sucessfully registered','do you want to proceed')
    
    if ans=='yes':
        next_page_register(root,frame)
    else:
        register(root,frame)
    frame.mainloop()

def next_page_register(root,frame):
    
    frame.destroy()
    frame=Frame(root,width=1366,height=768)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:\\Users\\user\\Desktop\\9cNrA8HypvTzMNQhG5xzBK.jpg'))
    l=Label(frame,image=img)
    l.place(x=0,y=0)
    
    l2=Label(frame,text="Rollnumber",font=("algerian",20,'bold'),borderwidth=17,fg='black',bg='tomato',relief='raised')
    l2.place(x=25,y=150)
    e3=Entry(frame,bg='white',fg='black',width=10,bd=12,font=("times",15,"bold"))
    e3.place(x=250,y=150)
            
    b1=Button(frame,text="View Marks",command=lambda:show(root,frame,e3),font=("algerian",25,'bold'),bg='VioletRed1',width=20,bd=10)
    b1.place(x=500,y=200)
    b2=Button(frame,text="View Attendance",font=("algerian",25,'bold'),bg='VioletRed1',width=20,bd=10,command=lambda:view_attendance(root,frame))
    b2.place(x=500,y=400)

    frame.mainloop()
    
def show(root,frame,e3):
    n=e3.get()
    frame.destroy()
    frame=Frame(root,width=1366,height=768,bg='pink')
    frame.place(x=0,y=0)
    l=Label(frame,text="show data",font=("algerian",50,'bold','underline'),fg='white',bg='gray10',bd=10,width=33)
    l.place(x=0,y=10)
    scl=scrolling_area.Scrolling_Area(frame,width=1366,height=768)
    scl.place(x=33,y=140)
    table=scrolling_area.Table(scl.innerframe,['Sub_1','Tot_M1','Ob_m1','Sub_2','Tot_M2','Ob_m2','Sub_3','Tot_M3','Ob_m','Sub_4','Tot_M4','Ob_m4','Sub_5','Tot_M5','Ob_m5','Sub_6','Tot_M6','Ob_m6'],column_minwidths=[50,60,60,50,60,60,50,60,60,50,60,60,50,60,60,50,60,0])
    table.pack(expand=True,fill=X)
    table.on_change_data(scl.update_viewport)
    conn=sqlite3.connect("table.db")
    cursor=conn.execute("select Sub_1,Tot_Marks1,Ob_marks1,Sub_2,Tot_Marks2,Ob_marks2,Sub_3,Tot_Marks3,Ob_marks3,Sub_4,Tot_Marks4,Ob_marks4,Sub_5,Tot_Marks5,Ob_marks5,Sub_6,Tot_Marks6,Ob_marks6 from table3 where Rollnumber=%s"%n)
    data=[]
    for row in cursor:
        column=[]
        data.append(column)
        for r in row:
            column.append(r)
    table.set_data(data)
    frame.mainloop()
    
def login(root,frame):
    frame.destroy()
    frame=Frame(root,width=1366,height=768)
    frame.place(x=0,y=0)
    img=ImageTk.PhotoImage(Image.open('C:\\Users\\user\\Desktop\\Background-Bananer_phixr-min.jpg'))
    l=Label(frame,image=img)
    l.place(x=0,y=0)
    l=Label(frame,text="STUDENT LOGIN",font=("algerian",20,'bold','underline'),fg='black',bg='gold',bd=7,width=80,relief='raised')
    l.place(x=0,y=10)


    l1=Label(frame,text="Enter Email",font=("algerian",30,'bold'),bg='cyan',width=20,relief='raised',bd=10)
    l1.place(x=60,y=180)


    l2=Label(frame,text="Enter Password",font=("algerian",30,'bold'),bg='cyan',width=20,relief='raised',bd=10)
    l2.place(x=60,y=300)


    e1=Entry(frame,width=45,bg='white',fg='black',bd=15,font=("Verdana 10 bold",12))
    e1.place(x=700,y=180)

    e2=Entry(frame,show='*',width=45,bg='white',fg='black',bd=15,font=("Verdana 10 bold",12))
    e2.place(x=700,y=300)
    

    #e3=Entry(frame,width=30,font=(30))
    #e3.place(x=800,y=420)

    b1=Button(frame,text="SUBMIT",command=lambda:loginsucess(root,frame,e1,e2),font=("algerian",15,'bold','underline'),fg='black',bd=15,bg='salmon',padx=20,width=5)
    b1.place(x=350,y=500)

    b2=Button(frame,text="BACK",command=lambda:back(root,frame),font=("algerian",15,'bold','underline'),fg='black',bd=15,bg='salmon',padx=20,width=5)
    b2.place(x=550,y=500)
    frame.mainloop()

def loginsucess(root,frame,e1,e2):
    f=0
    txt1=e1.get()
    print(txt1)
    txt2=e2.get()
    print(txt2)
    conn=sqlite3.connect('major.db')
    cursor=conn.execute('select Student_Email,Password from major2')
    
    for row in cursor:
        print(row[0])
        print(row[1])
        if(row[0]==txt1 and row[1]==txt2):
            f=1
            break

    if(f==1):
        ans=msg.askquestion('Ask Question','do you want to proceed')
        if ans=='yes':
                msg.showwarning('login sucessful','valid email or password')
                next_page_register(root,frame)
        else:
            login(frame,root)

    else:
        msg.showwarning('login failed','invalid user name or password')

        login(root,frame)

    conn.commit()
    


    
def back(root,frame):
    main(root,frame)


main(root,frame)

