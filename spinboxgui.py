from tkinter import *
class MySpin:
    def __init__(self,root) -> None:
        self.f=Frame(root,height=900,width=750)
        self.f.propagate(0)
        self.f.pack()
        self.val1=IntVar()
        self.val2=StringVar()
        self.spin1=Spinbox(self.f,from_=5,to=10,textvariable=self.val1,width=15,bg="white",fg="black",font=("arial",14))
        self.spin2=Spinbox(self.f,values=('La La Land','Eternal Sunshine of the spotless mind','500 days of summer'),textvariable=self.val2,width=15,bg="white",fg="black",font=("arial",14))
        self.b=Button(self.f,text="Your Chosen values",command=self.display)
        self.spin1.place(x=50,y=50)
        self.spin2.place(x=50,y=100)
        self.b.place(x=50,y=150)
    def display(self):
        res1=self.spin1.get()
        res2=self.spin2.get()
        lbl1=Label(text="your rank for the movie:"+str(res1)).place(x=50,y=200)
        lbl2=Label(text=f"your rank for the movie:{res2}").place(x=50,y=200)
root=Tk()  
sb=MySpin(root)
root.mainloop()