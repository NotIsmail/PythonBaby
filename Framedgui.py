#here we are creating frame which is useful for containing the widgets whereas the canvas iis used to contain the drawing and shti
from tkinter import *
def ButtonClick():
    print("you have clicked me")
root=Tk()
root.title("Frame 1")
f=Frame(root,height=400,width=500,bg="yellow",cursor="pirate")
f.propagate(0)
b=Button(f,text="click here",width=15,height=2,bg="yellow",fg="blue",activebackground="green",activeforeground="red",command=ButtonClick)
b.pack()
#b.bind("<Button-1>",ButtonClick)     #instead of this and the fucntion we can use the command function which does the same thing
f.pack()
root.mainloop()