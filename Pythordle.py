import customtkinter as ctk
import tkinter as tk
import random
from customtkinter import *
from tkinter import messagebox

messagebox.showinfo("How to play", "You have 6 turns to guess a 5-letter word. \
If a letter in your guess is enclosed in [square brackets], you guessed the letter correctly. \
If a letter is enclosed in (brackets), it is in the word, but you got its position wrong. \
Note that if you enter a word longer than five letters, only the first five letters are checked.")
turns = 6
words = ('HINGE', 'GRACE', 'TRUCK', 'CHURN', 'PLIER', 'GAUGE', 'FINCH', 'PRIZE', 'STERN', 'HOUND', 'CRACK', 'SNARL', 'KLUTZ', 'SLEEK', 'AUDIT')
word = words[random.randint(0, 14)]
progress = '_____'
lastGuess = ''
history = ''
progressList = list(progress)
def checkGuess() :
    global turns
    global lastGuess
    global progress
    global progressList
    global history
    if turns > 1 :
        progress = ''
        lastGuess = ''
        turns = turns - 1
        guessedWord = wordEntry.get()
        guess = guessedWord.upper()
        for i in range(5) :
            if guess[i]==word[i] :
                progressList[i] = f"[{guess[i]}]"
                lastGuess+=guess[i]
            elif guess[i] in word and guess.count(guess[i])==word.count(guess[i]) :
                lastGuess+=guess[i]
                progressList[i] = f"({guess[i]})"
            else :
                progressList[i] = guess[i]
                lastGuess+=guess[i]
        for i in progressList :
            progress+=f"{i} "
        history+=progress
        guessFetch.set(f"Turns left: {turns}")
        outOfPlaceTuple = tuple()
        outOfPlaceCount = 0
        history+="\n"
    else :
        guessFetch.set(f"\nYou're out of turns!\nThe word was {word}.")
    historyFetch.set(f"{history}")
    if lastGuess==word :
        guessFetch.set(f"\nYou guessed the word!\nThe word was {word}.\nTurns taken: {6-turns}\n(By the way, I learnt Tkinter and made this in a single day.)")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.title("Pythordle")
root.geometry("400x400")
guessFetch = ctk.StringVar()
historyFetch = ctk.StringVar()
title = ctk.CTkLabel(master=root, text="PYTHORDLE", font=("Bahnschrift", 36))
title.place(relx=0.5, rely=0.04, anchor=ctk.N)
subtitle = ctk.CTkLabel(master=root, text="BY SIDDHARTH JAI GOKULAN", font=("Bahnschrift", 12))
subtitle.place(relx=0.5, rely=0.13, anchor=ctk.N)
wordEntry = ctk.CTkEntry(master=root, placeholder_text="Type your guess here!")
wordEntry.place(relx=0.5, rely = 0.2, anchor=ctk.N)
checkButton = ctk.CTkButton(master=root, text="Check", width=380, command=checkGuess)
checkButton.place(relx=0.5, rely=0.3, anchor=ctk.N)
guessText = ctk.CTkLabel(master=root, textvariable=guessFetch, font=("Bahnschrift", 12), wraplength=400)
guessText.place(relx=0.5, rely = 0.8, anchor=ctk.N)
guessHistory = ctk.CTkLabel(master=root, textvariable=historyFetch, font=("Bahnschrift", 20))
guessHistory.place(relx=0.5, rely = 0.4, anchor=ctk.N)

root.mainloop()