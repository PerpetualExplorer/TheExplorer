from tkinter import*
import cmath

w=Tk();
w.geometry("300x300")
w.title("CALCULATOR")
w.wm_iconbitmap("C:\\Users\\Syed\\python & SQL\\krithiga class\\Calci.ico")


def add():
    p=int(e1.get())
    q=int(e2.get())
    a=p+q
    la=Label(w,text=a,font=("Helvetica","20","bold")).place(x=160,y=170)

def sub():
    p = int(e1.get())
    q = int(e2.get())
    a = p - q
    la = Label(w, text=a,font=("Helvetica", "20", "bold")).place(x=160,y=170)


def mul():
    p = int(e1.get())
    q = int(e2.get())
    a = p * q
    la = Label(w, text=a,font=("Helvetica", "20", "bold")).place(x=160,y=170)

def div():
    p = int(e1.get())
    q = int(e2.get())
    a = p / q
    la = Label(w, text=a,font=("Helvetica", "20", "bold")).place(x=160,y=170)

def per():
    p = int(e1.get())
    q = int(e2.get())
    a = (p / q) * 100
    la = Label(w, text=a,font=("Helvetica", "20", "bold")).place(x=160,y=170)

def sq():
    p = int(e1.get())
    q = int(e2.get())
    a = p ** q
    la = Label(w, text=a,font=("Helvetica", "20", "bold")).place(x=160,y=170)

def sqr():
    p = int(e1.get())
    q = int(e2.get())
    a = p ** (1/q)
    la = Label(w, text=a,font=("Helvetica","20","bold")).place(x=160,y=170)



#def n1():


#def n2():

#def n3():


#def n4():

#def n5():

#def n6():

#def n7():

#def n8():


#def n9():



#def n0():



#l1=Label(w,text="ENTER THE NUMBERS:",fg="BLACK",bg="WHITE",font=("TIM","16","bold"))
#l1.place(x=10,y=20)
l2=Label(w,text="NUMBER1",fg="BLACK",font=("Helvetica","12","bold")).place(x=10,y=50)
l3=Label(w,text="NUMBER2",fg="BLACK",font=("Helvetica","12","bold")).place(x=10,y=80)
l2=Label(w,text="ANSWER",fg="BLACK",font=("Helvetica","16","bold")).place(x=160,y=140)

e1=Entry(w)
e1.place(x=120,y=50)
e2=Entry(w)
e2.place(x=120,y=80)


"""b1=Button(w,text="1",fg="WHITE",bg="BLACK").place(x=140,y=200)
b2=Button(w,text="2",fg="WHITE",bg="BLACK").place(x=170,y=200)
b3=Button(w,text="3",fg="WHITE",bg="BLACK").place(x=200,y=200)
b4=Button(w,text="4",fg="WHITE",bg="BLACK").place(x=140,y=170)
b5=Button(w,text="5",fg="WHITE",bg="BLACK").place(x=170,y=170)
b6=Button(w,text="6",fg="WHITE",bg="BLACK").place(x=200,y=170)
b7=Button(w,text="7",fg="WHITE",bg="BLACK").place(x=140,y=140)
b8=Button(w,text="8",fg="WHITE",bg="BLACK").place(x=170,y=140)
b9=Button(w,text="9",fg="WHITE",bg="BLACK").place(x=200,y=140)
b0=Button(w,text="0",fg="WHITE",bg="BLACK").place(x=170,y=230)
"""
b_a=Button(w,text="+",command=add,fg="WHITE",bg="BLACK").place(x=50,y=140)
b_s=Button(w,text="-",command=sub,fg="WHITE",bg="BLACK").place(x=80,y=140)
b_m=Button(w,text="*",command=mul,fg="WHITE",bg="BLACK").place(x=50,y=170)
b_d=Button(w,text="/",command=div,fg="WHITE",bg="BLACK").place(x=80,y=170)
b_p=Button(w,text="%",command=per,fg="WHITE",bg="BLACK").place(x=110,y=170)
b_sq=Button(w,text="square",command=sq,fg="WHITE",bg="BLACK").place(x=50,y=200)
b_sqr=Button(w,text="square root",command=sqr,fg="WHITE",bg="BLACK").place(x=50,y=230)














w.mainloop()
