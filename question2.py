# NICOLE SUE IDORA ANAK SEMUAL
# 20DDT21F1041

import tkinter as tk
from tkinter import ttk

def Combine():
    Name1 = str(entry1.get())
    Name2 = str(entry2.get())
    result = Name1 + Name2
    lblResult.config(fg='black')
    lblJwp.config(text=result)
    lblJwp.config(fg='black')

def Clear():
    Combine.close()

def UsernameExit():
    AutomaticUsername.destroy()

AutomaticUsername = tk.Tk()
AutomaticUsername.title("AutomaticUsername")
AutomaticUsername.geometry("500x230")

frame = ttk.LabelFrame(AutomaticUsername, text="Username Suggestion")
frame.place(x=10, y=10, width=480, height=170)

lbl1 = ttk.Label(frame, text="First Name: ")
lbl1.place(x=27, y=10) 

entry1 = ttk.Entry(frame, width=40)
entry1.place(x=150, y=10)

lbl2 = ttk.Label(frame, text="Second Name: ")
lbl2.place(x=10, y=40)

entry2 = ttk.Entry(frame, width=40)
entry2.place(x=150, y=40)

btnCombine = tk.Button(frame, text="Combine", command=Combine)
btnCombine.place(x=280, y=100)

btnClear = tk.Button(frame, text="Clear",command=Clear)
btnClear.place(x=350, y=100)

btnExit = tk.Button(text="Exit", command=UsernameExit)
btnExit.place(x=420, y=190)

lblResult = tk.Label(AutomaticUsername, text="Suggested : ")
lblResult.place(x=36, y=100)

lblResult1 = tk.Label(text="@gmail.com")
lblResult1.place(x=230,y=100)

#lblResult2.tk.Label(A)

lblJwp = tk.Label(AutomaticUsername, text="name",fg='white')
lblJwp.place(x=160, y=100)

AutomaticUsername.mainloop()


