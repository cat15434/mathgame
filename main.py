import random
import tkinter as tk
from pathlib import Path

import time as ti

window=tk.Tk()




#initilze score
global score
score = 0



def end():
    exit()
def again():
    global score


    score=score-score
    scoreLabel.config(text="Score:" + str(score))
    window.after(50, yes.destroy)
    window.after(50, no.destroy)
    window.after(50,play_again.destroy)
    window.after(50,value6.destroy)


    gameloop()



entry=tk.Entry(window)
def gameloop():
    with open((Path(__file__).parent / "highscore.txt").resolve(), "r") as f:
        highscore = f.read()


    a= random.randint(0,101)
    b= random.randint(0,101)
    c=a*b
    z=str(c)
    value2 = tk.Label(text=a)
    value1 = tk.Label(text=b)
    value3 = tk.Label(text=c)
    value5 = tk.Label(text="Correct")

    value7 = tk.Label(text = "mmmm beans")


    print(c)

    def awnserrecived(event):

        
        print(entry.get())
        f=entry.get()
        if 'beans' in f :
         print("mmmm beans")
         value7.pack()
        window.after(2000,value7.destroy)
        if f == z:
         global score
         f = int(entry.get())
         print ("correct")
         score= score + 1
         scoreLabel.config(text="Score:"+str(score))
         print(score)
         value5.pack()
         window.after(2000, value5.destroy)
         window.after(100,value2.destroy)
         window.after(100, value1.destroy)
         window.after(100, value3.destroy)
         entry.delete(first=0,last=10)

         gameloop()

        elif f != z:

         global value6
         value6 = tk.Label(text="Game Over")
         global play_again
         play_again = tk.Label(text="Would You Like To Play Again?")
         f = int(entry.get())
         print("incorrect")

         window.after(50, value1.destroy)
         window.after(50,value2.destroy)
         window.after(50,value3.destroy)
         value6.pack()

         play_again.pack()
         global no
         no = tk.Button(text="No", command=end)
         global yes
         yes = tk.Button(text="Yes", command=again)
         no.pack()
         yes.pack()





#create score label



    entry.bind("<Return>",awnserrecived)
    value1.pack()
    value2.pack()
    value3.pack()
scoreLabel = tk.Label(text="Score:" + str(score))


scoreLabel.pack(side=tk.BOTTOM)
entry.pack()
window.after(1000,gameloop)
window.mainloop()
