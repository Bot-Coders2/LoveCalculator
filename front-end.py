from tkinter import *
from tkinter import messagebox
w=Tk()
w.title("ANNOTHAY NAKU")
w.geometry("800x500")
w.configure(bg='pink')
def cal():
    s1=yna.get()
    s2=cna.get()
    if(s1=='' or s2==''):
        messagebox.showerror("Error",'name cannot be empty')
    else:
        c=flames(s1,s2)
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
