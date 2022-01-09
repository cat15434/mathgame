import random
import tkinter as tk
from pathlib import Path



window=tk.Tk()




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
    global score
    entry.config(state="normal")
    score=0
    scoreLabel.config(text="Score:" + str(score))
    window.after(50, yes.destroy)
    window.after(50, no.destroy)
    window.after(50,play_again.destroy)
    window.after(50,value6.destroy)
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
         value7.pack()
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
         value5.pack()
#deletes all labels as needed
         window.after(2000, value5.destroy)
         window.after(100,value2.destroy)
         window.after(100, value1.destroy)
         window.after(100, value3.destroy)
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
         value6.pack()
         entry.delete(first=0,last=10)
         entry.config(state="disabled")
         entry.unbind('<Return>')
#print the play again text
         play_again.pack()
#import no button response
         global no
         no = tk.Button(text="No", command=end)
#import yes button response
         global yes
         yes = tk.Button(text="Yes", command=again)
#show buttons on window
         no.pack()
         yes.pack()
#this is for when user input is not an int but a alphabetical response
     except ValueError:
         notint=tk.Label(text="that's not a number please enter a number.")
         entry.delete(first=0,last=10)
         notint.pack()
         window.after(1000,notint.destroy)








#makes the submit mechanic for user response
    entry.bind("<Return>",awnserrecived)
#show the rng numbers and the awnser with .packs
    value1.pack()
    value2.pack()
    value3.pack()
#create score & highscore labels
scoreLabel = tk.Label(text="Score:" + str(score))
highscoretext = tk.Label(text="HighScore:" + str(highscore))
#make the packs visable as needed
highscoretext.pack(side=tk.BOTTOM)
scoreLabel.pack(side=tk.BOTTOM)
entry.pack()
#this allows us to create a gameloop inside the window loop of tkinter
window.after(1000,gameloop)
#run windowloop from tkinter
window.mainloop()
