from tkinter import *
import random

def code_gen():
    Lst_of_nmbr = [str(x) for x in range(0, 10)]
    code = []
    for _ in range(6):
        code.append(random.choice(Lst_of_nmbr))

    code_fin = ' '.join(code)

    newWindow = Toplevel(Master)
    newWindow.geometry("200x200")
    Code_lbl = Label(newWindow, text=code_fin).place(relx=0.5, rely=0.5, anchor="center")


Master = Tk()
Master.title("Code Generator")
Master.geometry("200x200")
Clck_bttn = Button(Master, text="Click To Start", command=code_gen).place(relx=0.5, rely=0.5, anchor="center")
Master.mainloop()