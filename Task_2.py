#creating calculator with gui
from tkinter import *
window=Tk()
window.title("Calculator")
window.geometry("600x600")
window.configure(bg="blue")
s=""
l1=Text(window,bg="grey",font=("Arial",30),width="22",height=1,pady=20)
l1.pack()
f=Frame(window)
f.configure(bg="blue")
b1=Button(f,text="1",width="5",height=1,font=("Arial",20),command=lambda:click(1))
b1.grid(column=0,row=1)
b2=Button(f,text="2",width="5",height=1,font=("Arial",20),command=lambda:click(2))
b2.grid(column=1,row=1)
b3=Button(f,text="3",width="5",height=1,font=("Arial",20),command=lambda:click(3))
b3.grid(column=2,row=1)
b4=Button(f,text="4",width="5",height=1,font=("Arial",20),command=lambda:click(4))
b4.grid(column=0,row=2,padx=20,pady=20)
b5=Button(f,text="5",width="5",height=1,font=("Arial",20),command=lambda:click(5))
b5.grid(column=1,row=2,padx=20,pady=20)
b6=Button(f,text="6",width="5",height=1,font=("Arial",20),command=lambda:click(6))
b6.grid(column=2,row=2,padx=20,pady=20)
b7=Button(f,text="7",width="5",height=1,font=("Arial",20),command=lambda:click(7))
b7.grid(column=0,row=3,padx=20,pady=20)
b8=Button(f,text="8",width="5",height=1,font=("Arial",20),command=lambda:click(8))
b8.grid(column=1,row=3,padx=20,pady=20)
b9=Button(f,text="9",width="5",height=1,font=("Arial",20),command=lambda:click(9))
b9.grid(column=2,row=3,padx=20,pady=20)
b10=Button(f,text="0",width="5",height=1,font=("Arial",20),command=lambda:click(0))
b10.grid(column=0,row=4,padx=20,pady=20)
b11=Button(f,text="+",width="5",height=1,font=("Arial",20),command=lambda:click("+"))
b11.grid(column=3,row=1,padx=20,pady=20)
b12=Button(f,text="-",width="5",height=1,font=("Arial",20),command=lambda:click("-"))
b12.grid(column=3,row=2,padx=20,pady=20)
b13=Button(f,text="*",width="5",height=1,font=("Arial",20),command=lambda:click("*"))
b13.grid(column=3,row=3,padx=20,pady=20)
b14=Button(f,text="/",width="5",height=1,font=("Arial",20),command=lambda:click("/"))
b14.grid(column=1,row=4,padx=20,pady=20)
b15=Button(f,text="=",width="5",height=1,font=("Arial",20),command=lambda:click("="))
b15.grid(column=2,row=4,padx=20,pady=20)
b16=Button(f,text="clear",width="5",height=1,font=("Arial",20),command=lambda:click("clear"))
b16.grid(column=3,row=4,padx=20,pady=20)
b17=Button(f,text="backspace",width="8",height=1,font=("Arial",20),command=lambda:click("backspace"))
b17.grid(column=0,row=5,padx=20,pady=20)
b18=Button(f,text=".",width="5",height=1,font=("Arial",20),command=lambda:click("."))
b18.grid(column=1,row=5,padx=20,pady=20)
b19=Button(f,text="00",width="5",height=1,font=("Arial",20),command=lambda:click("00"))
b19.grid(column=2,row=5,padx=19,pady=20)
f.pack()

def click(a):
    global s
    #clearing the whole expression
    if(a=="clear"):
        s=""
        l1.insert(1.0,s)
        l1.delete(1.0,END)
    elif(a=="="):
        try:
               
            e=s.lstrip("0") 
            
            #evaluting the expression
            d=str(eval(e))
            l1.delete(1.0,END)
            l1.insert(1.0,d)

        except Exception as e:

            l1.delete(1.0,END)
            l1.insert(1.0,"Error")
            print(f"Error:{e}")

    elif(a=="backspace"):
        try:
            s=s.rstrip(s[-1])
            l1.delete(1.0,END)
            l1.insert(1.0,s)

        except Exception as e:

            l1.delete(1.0,END)
            l1.insert(1.0,"no numbers to remove")
            print(f"Error:{e}")

    else:
        s=s+str(a)
        l1.delete(1.0,END)
        l1.insert(1.0,s)

window.mainloop()
