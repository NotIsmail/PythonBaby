from tkinter import *
class Mycheck:
    def __init__(self,root) -> None:
        self.f=Frame(root,height=500,width=500)
        self.f.propagate(0)
        self.f.pack()
        self.var1=IntVar()
        self.var2=IntVar()
        self.var3=IntVar()
        self.c1=Checkbutton(self.f,bg="yellow",fg="green",text='Python',font=('verdana',10,'underline'),variable=self.var1,command=self.display)
        self.c2=Checkbutton(self.f,bg="yellow",fg="green",text='Java',font=('verdana',10,'underline'),variable=self.var2,command=self.display)
        self.c3=Checkbutton(self.f,bg="yellow",fg="green",text='.NET',font=('verdana',10,'underline'),variable=self.var3,command=self.display)
        self.c1.place(x=50,y=100)
        self.c2.place(x=200,y=100)
        self.c3.place(x=350,y=100)
    def display(self):
        x=self.var1.get()
        y=self.var2.get()
        z=self.var3.get()
        str=''
        if x==1:
            str+='python'
        if y==1:
            str+='java'
        if z==1:
            str+='.net'
        lbl=Label(text=str,fg="blue").place(x=50,y=150,width=200,height=20)
root=Tk()
mc=Mycheck(root)
root.mainloop()
        