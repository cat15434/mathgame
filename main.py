import random
import tkinter as tk
from pathlib import Path



window=tk.Tk()
window.configure(bg='light blue')



#initilze score
global score
score = 0
#initilze highscore
global highscore
with open((Path(__file__).parent / "highscore.txt").resolve(), "r") as f:
    highscore = f.read()



#Make Play again button event for no response
def end():
    exit()

#Make Play again button event for yes response
def again():
    global correctawnser
    global score
    entry.config(state="normal")
    score=0
    scoreLabel.config(text="Score:" + str(score),bg="light blue")
    window.after(50, yes.destroy)
    window.after(50, no.destroy)
    window.after(50,play_again.destroy)
    window.after(50,value6.destroy)
    window.after(50,correctawnser.destroy)
    highscoretext.config(text="Highscore:"+str(highscore))
    entry.delete(first=0, last=10)

    gameloop()




#make entry window
entry=tk.Entry(window)

#this identifies the main game loop to gen random nums and calculate plus get awnsers
def gameloop():


#create random variables
    a= random.randint(0,101)
    b= random.randint(0,101)
#calculate and turn the awnser into a string for labels
    c=a*b
    z=str(c)
#Create label for each number
    value2 = tk.Label(text=a)
    value1 = tk.Label(text=b)
    value3 = tk.Label(text=c)
#create label for correct text
    value5 = tk.Label(text="Correct")
#mmmm beans
    value7 = tk.Label(text = "mmmm beans")

#print c in the console just in case
    print(c)

#make the event for getting the user awnser
    def awnserrecived(event):
#this try statement fixes errors due to value error i.e use types 'e' instead of a int
     try:
        print(entry.get())
        f=entry.get()
#initiate if statement for beans easter egg
        if 'beans' in f :
         print("mmmm beans")
         value7.grid(row=0,column=2)
#destroy the .pack for mmmm beans or value7
        window.after(2000,value7.destroy)
#if the user input is a valid respons and isnt beans but an int then this is the correct awnser response
        if f == z:
#import globals as needed
         global score
         global highscore
#turn f into an int
         f = int(entry.get())
         print ("correct")
#update score
         score= score + 1
#score label make sure score is a str as .Label can only itarate str variables
         scoreLabel.config(text="Score:"+str(score))
#this is new for this program from the og rather than only showing at end highscore updates if passed
         if score > int(highscore):
             highscoretext.config(text="HighsScore:"+ str(score))
         print(score)
#place correct label or value5.pack
         value5.grid(row=1,column=2)
#deletes all labels as needed
         window.after(2000, value5.destroy)
         window.after(1,value2.destroy)
         window.after(1, value1.destroy)
         window.after(1, value3.destroy)
#clears entery to blank
         entry.delete(first=0,last=10)

         gameloop()


# response for wrong int awnser
        elif f != z:

#import value 6 actions
         global value6
#create game over label
         value6 = tk.Label(text="Game Over")
#if the score is higher than highscore go into highscore.txt and update from prev highscore
         if score > int(highscore):
             highscore = score
             highscoretext.config(text="new highscore:" + str(score))
             with open("highscore.txt", "w") as f:
                 f.write(str(highscore))
#make play again statement
         global play_again
         play_again = tk.Label(text="Would You Like To Play Again?")
         f = int(entry.get())
         print("incorrect")
#destroy all the .packs needed
         window.after(50, value1.destroy)
         window.after(50,value2.destroy)
         window.after(50,value3.destroy)
         value6.grid(row=1,column=2)
         entry.delete(first=0,last=10)
         global correctawnser
         correctawnser=tk.Label(text="The Correct Answer was: " + z)
         correctawnser.grid(row=5,column=2)
         entry.config(state="disabled")
         entry.unbind('<Return>')
#print the play again text
         play_again.grid(row=2,column=2)
#import no button response
         global no
         no = tk.Button(text="No", command=end,height=5,width=10)
#import yes button response
         global yes
         yes = tk.Button(text="Yes", command=again,height=5,width=10)
#show buttons on window
         no.grid(row=3,column=2)
         yes.grid(row=4,column=2)
#this is for when user input is not an int but a alphabetical response
     except ValueError:
         notint=tk.Label(text="that's not a number please enter a number.")
         entry.delete(first=0,last=10)
         notint.grid(row=2,column=2)
         window.after(1000,notint.destroy)








#makes the submit mechanic for user response
    entry.bind("<Return>",awnserrecived)
#show the rng numbers and the awnser with .packs

    value1.grid(row=2,column=3)
    value2.grid(row=2,column=1)

    value1.config(font=("Arial",50),bg="light blue")
    value2.config(font=("Arial",50),bg="light blue")
timessign=tk.Label(text="x")
timessign.config(font=("Arial",50))

#create score & highscore labels

scoreLabel = tk.Label(text="Score:" + str(score))
highscoretext = tk.Label(text="HighScore:" + str(highscore))
#make the packs visable as needed
highscoretext.grid(row=5,column=2)
scoreLabel.grid(row=4,column=2)
scoreLabel.config(font=("Arial",35),bg="light blue")
highscoretext.config(font=("Arial",30),bg="light blue")
entry.grid(row=0,column=2)
timessign.grid(row=2,column=2)
timessign.config(bg="light blue")
howto=tk.Label(text="enter your awnser for the product of the 2 numbers above in the entry box")
howto.grid(row=7,column=2)
howto.config(font=("Arial",15),bg="light blue")
#this allows us to create a gameloop inside the window loop of tkinter



window.after(1000,gameloop)

#run windowloop from tkinter
window.mainloop()
