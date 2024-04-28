from tkinter import *
class MyMessage:
    def __init__(self,root) -> None:
        self.f=Frame(root,height=450,width=550)
        self.f.propagate(0)
        self.f.pack()
        self.m=Message(self.f,text="La La Land is the fucking best thing ever made",width=200,font=("times",20,"bold"),fg="dark goldenrod")
        self.m.pack(side=LEFT)
root=Tk()
mes=MyMessage(root)
root.mainloop()
        