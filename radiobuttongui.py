from tkinter import *
class MyRadio:
    def __init__(self,root) -> None:
        self.f=Frame(root,height=500,width=500)
        self.f.propagate(0)
        self.f.pack()
        self.var=IntVar()
        self.r=Radiobutton(self.f,bg='black',fg='white',font=('vernada',30,'bold'),text='male',variable=self.var,value=1,command=self.display)
        self.r1=Radiobutton(self.f,bg='black',fg='white',font=('vernada',30,'bold'),text='female',variable=self.var,value=2,command=self.display)
        self.r.place(x=50,y=100)        
        self.r1.place(x=200,y=100)        
    def display(self):
        x=self.var.get()
        str=''
        if x==1:
            str+='male'
        if x==2:
            str+='female'
        lbl=Label(text=str,fg='black').place(x=50,y=150,width=200,height=20)
root=Tk()
mb=MyRadio(root)
root.mainloop()
