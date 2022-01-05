import random
import tkinter as tk
window=tk.Tk()


f=tk.Entry()

a= random.randint(0,101)
b= random.randint(0,101)
d=int(f.get())
c=a*b
value2 = tk.Label(text=a)
value1 = tk.Label(text=b)
value3 = tk.Label(text=c)


f.pack()
value1.pack()
value2.pack()
value3.pack()



window.mainloop()