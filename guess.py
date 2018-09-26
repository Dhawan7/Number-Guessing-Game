from tkinter import *
import random
root = Tk()

def guess():
    a = random.randint(10,20)
    try:
        ui = int(ip.get())
        if a > ui:
            Lb2.config(text="Number You Guessed Is Lesser",bg='red')
        elif a < ui:
            Lb2.config(text="Number You Guessed Is Greater",bg='red')
        elif a == ui:
            Lb2.config(text="**Congratulations!!! You Cracked It!!!**\nCorrect Match:{}\nYour Input: {}".format(a,ui),bg='green')
        else:
            Lb2.config(text="Erong input!!! ",bg='red')
    except ValueError:
        Lb2.config(text="Please Enter integers only!!",bg='red')

Lb = Label(root, text="Guess Any Number",font=('cursive',20),bg='Yellow', fg='red')
Lb.pack(pady=5)
Lb2 = Label(root, fg='white')
Lb2.pack(pady=5)
ip = Entry()
ip.pack(pady=5)
btn = Button(text='Guess',width=15,bg='green',fg='white',command=guess)
btn.pack(pady=10)
btn2 = Button(text='Exit',width=15,bg='red',fg='white',command=exit)
btn2.pack(pady=10)
root.mainloop()
