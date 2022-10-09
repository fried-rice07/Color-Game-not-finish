from tkinter import *
import tkinter as tk
import random
roll_dice=tk.Tk()
roll_dice.geometry("400x460")
roll_dice.title("Roll Dice")
root=Tk()
root.configure(background="gray")
#TItle of window ,resize
root.title("WaCHU GONNA DU SER WHACHU GONNA DU")
root.geometry("400x660")
#text in the window

q=Label(root,text="COLOR GAME",height="2",bg="gray",width="30",fg="white",relief=RAISED,font=("FELIX TITLING",23,"bold"))
q.place(x=1,y=0)
q.pack(padx=1)
dices=tk.Label(roll_dice,text="",height="11",font=("Arial",300))
#questioning
q1=Label(root,text="Choose Your Color",height="2",width="28",bg="white",relief=FLAT,font=("Arial",20))
q1.place(x=1,y=100)
q1.pack(padx=2)
#define function!
#def roll():

def balance():
    try:
        bal=int(my_balance.get())
        balance1 = Label(root, text="Your Money Now is")
        balance1.pack()

        balance=Label(root,text=bal,bg="black",fg="white")
        balance.pack()
        my_balance.delete(0,END)
    except ValueError:
         print("Invalid!")
def but1():
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    print(f'{random.choice(dice)}')
    dices.configure(text=f'{random.choice(dice)}')
    dices.pack()
    try:
        balance=int(my_balance.get())
        a=int(my_box1.get())
        b=int(my_box2.get())
        c=int(my_box3.get())
        d=int(my_box4.get())

        answer1= balance-a
        answer.config(text=answer1)

    except ValueError:
        answer.config(text="Invalid")




#bg=""- for background and fg=""- foregreund
#button list
button=tk.Button(roll_dice,command=but1)
button.place(x=100000,y=10000)
#button1
button1=Button(root,text="1",height="6",width="15",bg="blue",cursor="hand2",relief=FLAT,font="Verdana 15")
button1.place(x=2,y=148)
my_button1=Label(root,text="Enter A Value:")
my_button1.place(x=2,y=250)
my_box1=Entry(root)
my_box1.place(x=80,y=250)


#button2
button2=Button(root,text="2",height="6",width="15",bg="red",cursor="hand2",relief=FLAT,font="Verdana 15")
button2.place(x=200,y=148)
my_button2=Label(root,text="Enter A Value:")
my_button2.place(x=200,y=250)
my_box2=Entry(root)
my_box2.place(x=279,y=250)

#button3
button3=Button(root,text="3",height="6",width="15",bg="green",cursor="hand2",relief=FLAT,font="Verdana 15")
button3.place(x=1,y=300)
my_button3=Label(root,text="Enter A Value:")
my_button3.place(x=1,y=420)
my_box3=Entry(root)
my_box3.place(x=80,y=420)

#button4
button4=Button(root,text="4",height="6",width="15",bg="yellow",cursor="hand2",relief=FLAT,font="Verdana 15")
button4.place(x=200,y=300)
my_button4=Label(root,text="Enter A Value:")
my_button4.place(x=200,y=420)
my_box4=Entry(root)
my_box4.place(x=279,y=420)
#command
my_button44=Button(root,text="Enter & Scroll Dice",bg="black",fg="white",command=but1)
my_button44.place(x=140,y=380)
#button5
button5=Button(root,text="5",height="6",width="15",bg="purple",cursor="hand2",relief=FLAT,font="Verdana 15")
button5.place(x=1,y=469.1)
#button6
button6=Button(root,text="6",height="6",width="15",bg="Cyan",cursor="hand2",relief=FLAT,font="Verdana 15")
button6.place(x=200,y=469.1)
#balance
my_balance=Entry(root)
my_balance.place(x=108,y=640)
bal1=Button(root,text="Enter Your Money")
bal1.place(x=1,y=638)
my_balance1=Button(root,text="Enter",command=balance)
my_balance1.place(x=198,y=638)


answer=Label(root,text="",bg="black",fg="white")
answer.place(x=180,y=350)
root.mainloop()

