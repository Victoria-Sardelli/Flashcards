"""
    file: Flashcards.py
    author: Victoria Lauren Sardelli
    date: 12/8/14
    description: Flashcards
"""

from tkinter import *


def secondStage(event):
    """
    erases welcome screen
    :param event: user clicks "Continue" button
    :return:
    """
    welcomeLabel.pack_forget()
    welcomeButton.pack_forget()

    #Second Stage => user inputs amount of flashcards to make

    amtCards.pack()

    answer.pack()

    numEnter.pack()
    numEnter.bind("<Button-1>", thirdStage)

def thirdStage(event):
    amtCards.pack_forget()
    global num
    num = int(answer.get())

    answer.pack_forget()
    numEnter.pack_forget()
    makeCards(num, 1)

def makeCards(num, x):
    global y
    y = x

    currCard["text"] = "Card #" + str(y)
    currCard.pack()
    oneSide.pack()

    spacer.pack()
    twoSide.pack()

    cardEnter.pack()
    cardEnter.bind("<Button-1>", addToDict)


def addToDict(event):
    a = oneSide.get()
    b = twoSide.get()
    vocab[a]=b
    oneSide.delete(0, END)
    twoSide.delete(0, END)

    if y == num:
        currCard.pack_forget()
        oneSide.pack_forget()
        spacer.pack_forget()
        twoSide.pack_forget()
        cardEnter.pack_forget()
        beginFlashcards()

    else:
        return makeCards(num, y+1)

def beginFlashcards():
    beginCards.pack()
    beginCards.bind("<Button-1>", displayCards)

def displayCards(event):
    beginCards.pack_forget()
    topFrame.pack_forget()
    bottomFrame.pack_forget()
    '''newFrame.pack(side=TOP)
    newBotFrame.pack()'''
    for key in vocab.keys():
        oneWord["text"] = key
        oneWord.pack()
        flipButton.pack()
        flipButton.bind("<Button-1>", flipped)

def flipped(event):
    oneWord["text"] = vocab[oneWord["text"]]
    '''twoWord["text"] = vocab[oneWord["text"]]
    twoWord.pack()'''




vocab = {}

root = Tk()
root.geometry("500x500")
root.configure(background="pale turquoise")


topFrame = Frame(root) #I only put it there so that the welcome label and button would be in center of window!
topFrame.config(height = 150, width = 250, background="pale turquoise")
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.config(height=350, width = 250, background="pale turquoise")
bottomFrame.pack()

#first stage
welcomeLabel = Label(bottomFrame, text="Welcome to Tori's Flashcard Program!", font="Raleway", anchor=N, background="pale turquoise")
welcomeButton = Button(bottomFrame, text="Continue", anchor=N, activebackground="pale turquoise")
welcomeButton.bind("<Button-1>", secondStage)
welcomeLabel.pack()
welcomeButton.pack()

#second stage
amtCards = Label(bottomFrame, text="How many flashcards do you want to make?", font="Raleway", background="pale turquoise")
numEnter = Button(bottomFrame, text="Enter", font="Raleway", activebackground="pale turquoise")
answer = Entry(bottomFrame)

#makeCards stage
oneSide = Entry(bottomFrame)
spacer = Label(bottomFrame, background="pale turquoise")
twoSide = Entry(bottomFrame)
cardEnter = Button(bottomFrame, text="Enter", font="Raleway", activebackground="pale turquoise")
currCard = Label(bottomFrame, text="Card #" + str(1), font="Raleway", background="pale turquoise")

#displayCards stage
newFrame = Frame(root)
newFrame.config(height = 150, width = 500)
newBotFrame = Frame(root)
newBotFrame.config(height = 350, width = 500)
beginCards = Button(bottomFrame, text="Flashcard Game", font="Raleway", activebackground="pale turquoise")
oneWord = Label(root, text="", font="Raleway", background="pale turquoise", height=10)
twoWord = Label(newBotFrame, text="", font="Raleway", background="pale turquoise")
flipButton = Button(root, text="Flip", font="Raleway", anchor=N, activebackground="pale turquoise")

root.mainloop()