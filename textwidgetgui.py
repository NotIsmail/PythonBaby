from tkinter import *
class MyText:
    def __init__(self,root) -> None:
        self.t=Text(root,width=2000,height=1000,font=('verdana',14,"bold"),fg="blue",bg="yellow",wrap=WORD)
        self.t.insert(END,"Hello This is Ismail\nI code in python\ni love la la land")
        self.t.pack(side=LEFT)
        self.img=PhotoImage(file="La_La_Land.png")
        self.t.image_create(END,image=self.img)
        self.t.tag_add("start",'1.0','1.11')
        self.t.tag_config('start',background='red',foreground='white',font=('Lucida console',20,'bold italic'))
        self.s=Scrollbar(root,orient=VERTICAL,command=self.t.yview)
        self.t.configure(yscrollcommand=self.s.set)
        self.s.pack(side=LEFT,fill=Y)
root=Tk()
mt=MyText(root)
root.mainloop()