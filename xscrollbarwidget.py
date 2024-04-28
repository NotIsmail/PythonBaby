from tkinter import *
class MyScroll:
    def __init__(self,root) -> None:
        self.t=Text(root,width=70,height=15,bg='black',fg='white',font=('verdana',30,'bold'),wrap=NONE)
        for i in range(20):
            self.t.insert(END,"hello there how ypu doing i am not actually prepared and have a lot to code and study god knows wt am i gonna do")
        self.t.pack(side=TOP,fill=X)
        self.h=Scrollbar(root,orient=HORIZONTAL,command=self.t.xview)
        self.t.configure(xscrollcommand=self.h.set)
        self.h.pack(side=BOTTOM,fill=X)
root=Tk()
ms=MyScroll(root)
root.mainloop()