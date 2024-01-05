from tkinter import *
from tkinter import messagebox
from string import digits


cal = Tk()
cal.title('calculator')
cal.geometry('300x500')
cal.resizable(width=False,height=False)

itemlist = list()
itemlist = list(map(str,digits))
itemlist.append('+')
itemlist.append('-')
itemlist.append('/')
itemlist.append('*')
itemlist.append('.')
out = ''
n = 0
while n < 15:
    exec(f'def btn{n}(): global out ;out+=itemlist[{n}];l1.config(text=f"\t%s\t"%(out));')
    n+=1


def btn15():
    global out
    try:
        l1.config(text='\t'+f"{eval(out)}"+'\t')
        out = f"{eval(out)}"
    except:
        messagebox.showerror('خطایه ریاضی',"مقادیر وارد شده بر خلاف منطق ریاضی می باشد")
        out = ''
        l1.config(text='\t'*2)
def btn16():
    global out
    if len(out):
        out = out[:len(out)-1]
    l1.config(text='\t'+out+'\t')
    
def btn17():
    global out
    out = "\t"*2
    l1.config(text='\t'+out+'\t')


f1 = Frame(cal,bg='gray')
f1.pack(fill='both',expand=True)
l1 = Label(f1,text='   '*15,bg='white')
l1.place(relx=.5, rely=.1, anchor="c")
lis = list()

for i in range(0,15):
    exec(f"b{i} = Button(f1,text='{itemlist[i]}',command=btn{i},width=6, height=2)")

b15 = Button(f1,text='=',command=btn15,width=6, height=2)
b16 = Button(f1,text='←',font=(None,10),command=btn16,width=8, height=2)
b17 = Button(f1,text='clear',command=btn17,width=8, height=2)

num = 0
rely = 2
relx = 1
while num<15:
    if relx<10:
        print(relx,rely)
        exec(f"b{num}.place(relx=.{relx}, rely=.{rely}, anchor='c')")
        relx +=2
    else:
        rely+=1
        relx = 1
    if num==5:
        exec(f"b{num}.place(relx=.1, rely=.3, anchor='c')")
        relx +=2
    if num==10:
        exec(f"b{num}.place(relx=.1, rely=.4, anchor='c')")
        relx +=2
    num+=1
    
b15.place(relx=.5, rely=.5, anchor="c")
b16.place(relx=.8, rely=.5, anchor="c")
b17.place(relx=.2, rely=.5, anchor="c")


cal.mainloop()
