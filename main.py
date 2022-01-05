import random
import tkinter as tk

import time as ti

window=tk.Tk()


entry=tk.Entry(window)
def play():
    button2 = tk.Button(command=play())
    button3=button2
    a= random.randint(0,101)
    b= random.randint(0,101)
    c=a*b
    z=str(c)
    value2 = tk.Label(text=a)
    value1 = tk.Label(text=b)
    value3 = tk.Label(text=c)
    value5 = tk.Label(text="Correct")
    value6 = tk.Label(text = "Game Over")
    value7 = tk.Label(text = "mmmm beans")
    print(c)
    def hi() :
        print(entry.get())
        f=entry.get()
        if 'beans' in f :
            print("mmmm beans")
            value7.pack()
            window.after(2000,value7.destroy)
        if f == z:
            f = int(entry.get())
            print ("correct")
            value5.pack()
            window.after(2000, value5.destroy)

        elif f != z:
            f = int(entry.get())
            print("incorrect")
            value6.pack()
            window.after(2000, value6.destroy)


    button=tk.Button(command=play())

    entry.bind("<Return>",hi)
    value1.pack()
    value2.pack()
    value3.pack()
    entry.pack()
    button.pack()

window.mainloop()
