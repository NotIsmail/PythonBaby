from tkinter import *
class MyButtons:
    def __init__(self,root) -> None:
        self.f=Frame(root,height=350,width=500)
        self.f.propagate(0)
        self.f.pack()
        self.b=Button(self.f,text="Click here",height=2,width=10,bg="white",fg="black",activebackground="light green",activeforeground="green",command=self.ClickButton)
        self.b1=Button(self.f,text="quit",height=2,width=10,bg="white",fg="black",activebackground="red",activeforeground="black",command=quit)
        self.b.grid(row=0,column=1)
        self.b1.grid(row=0,column=2)
    def ClickButton(self):
        self.lbl=Label(self.f,text="Hello There",height=2,width=20,font=('courier',-30,'bold'),fg="black")
        self.lbl.grid(row=2,column=0)
root=Tk()
mb=MyButtons(root)
root.mainloop()