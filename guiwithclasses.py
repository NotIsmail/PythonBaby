from tkinter import *
class MyButton:
    def __init__(self,root) -> None:
        self.f=Frame(root,height=500,width=600,bg="Red")
        self.f.propagate(0)
        self.f.pack()
        self.b1=Button(self.f,text="button 1",height=2,width=10,bg="red",fg="black",activebackground="white",activeforeground="blue",command=lambda:self.ClickButton(1))
        self.b2=Button(self.f,text="button 2",height=2,width=10,bg="yellow",fg="black",activebackground="white",activeforeground="blue",command=lambda:self.ClickButton(2))
        self.b3=Button(self.f,text="button 3",height=2,width=10,bg="green",fg="black",activebackground="white",activeforeground="blue",command=lambda:self.ClickButton(3))
        self.b1.pack()
        self.b2.pack()
        self.b3.pack()
    def ClickButton(self,num):
        if num==1:
            self.f["bg"]='red'
        if num==2:
            self.f["bg"]='yellow'
        if num==3:
            self.f["bg"]='green'
root=Tk()
mb=MyButton(root)
root.mainloop()