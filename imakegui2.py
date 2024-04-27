#this is the tkinter basic shit where u gotta create a root window the most basic shit 
from tkinter import *
from tkinter import font     #for fonts we have to import font package separately
root=Tk()
root.title("La La Land")    # we can set title of the tkinter box 
root.geometry("400x300")    #we can even set the size of tkinter box
#root.wm_iconbitmap("image.ico")    #we can change the icon of tkinter to anything
# list_of_fonts=list(font.families())   #to accesas all the fonts in the form of list 
# print(list_of_fonts)
c=Canvas(root,bg="AliceBlue",width=1200,height=700,cursor='mouse')
id=c.create_polygon(100,200,300,400,500,600,width=33,fill="green",outline="black",smooth=1,activefill="lightblue")
fnt=('YouYuan',40,'underline')
id=c.create_text(500,200,text="Hey Ismail",font=fnt,fill='black',activefill="green")
id=c.create_arc(100,100,400,300,width=3,start=270,extent=180,outline='red',style="arc",activefill="blue")
file1=PhotoImage(file="La_La_Land.png")
file2=PhotoImage(file="La_La_Land.png")
id=c.create_image(100,200,anchor=CENTER,image=file1,activeimage=file2)
c.pack()
root.mainloop()