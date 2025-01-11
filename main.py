from tkinter import *
from tkinter.font import Font
import tkinter as tk
import requests
import random
import time

input = ""
ticking = False
my_input = []

BG = "#AF8F6F"
TYPEFACE ="#F8F4E1"

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()
WORD = []
words =[]
final = []
indexes = []
for word in WORDS:
    words = word.decode("utf-8")
    WORD.append(words)

time_left = 60

def get_speed():
    global word_entry
    global words
    global input
    global final
    global my_input
    global indexes
    word_entry.config(state=DISABLED)
    correct = []
    wrong = []
    for word in words:
        if word not in final:
            final.append(word)

    for word in my_input:
        if word in final and word not in correct:
            correct.append(word)
        elif word != "" and word not in wrong and word not in correct:
            wrong.append(word)
    for word in my_input:
        if word in wrong:
            index = my_input.index(word)
            indexes.append(index)


    text_canvas.itemconfig(text_id, text= f"You typed {len(correct)} wpm and made {len(wrong)} mistakes!")
    print(f"You typed {len(correct)} wpm and made {len(wrong)} mistakes!")
    time.sleep(1)

    word_entry.config(state=NORMAL)
    word_entry.delete("1.0", END)
    if len(wrong) > 0:
        for index in indexes:
            word_entry.insert(END, f"You typed {my_input[index]} instead of {final[index]}\n")
    word_entry.config(state=DISABLED)


def new_words(event):
    global words
    global final
    global input
    global my_input

    for word in words:
        if word not in final:
            final.append(word)

    input = word_entry.get("1.0", END).split(" ")
    input[-1] = input[-1].strip(" \n")
    if input[-1] == "":
        input.remove(input[-1])

    for word in input:
        if word != " " and word not in my_input:
            my_input.append(word)

    words = []
    for i in range(15):
        words.append(random.choice(WORD))

    text_canvas.itemconfig(text_id, text=" ".join(words))
    word_entry.delete("1.0", END)


def submit_word(event):
    global my_input
    input = word_entry.get("1.0", END).split(" ")
    input[-1] = input[-1].strip(" \n")
    if input[-1] == "":
        input.remove(input[-1])

    for word in input:
        if word not in my_input and word != " ":
            my_input.append(word)


def update_clock():
    global clock
    global time_left
    if time_left > 0:
        time_left = time_left - 1
        clock.config(text=f"Time Remaining: {time_left} seconds")
        window.after(1000, update_clock)
        return clock, time_left

    else:
        clock.config(text=f"Times Up!")
        get_speed()
        return clock, word_entry


def start_game():
    global time_left
    global clock
    global word_entry
    global ticking
    global words
    word_entry.focus()
    if not ticking:
        ticking = True
        update_clock()
        words = []
        for i in range(15):
            words.append(random.choice(WORD))

        text_canvas.itemconfig(text_id, text=" ".join(words))
        word_entry.delete("1.0", END)


window = Tk()

window.title("Speed Type Test")
window.config(padx=50, pady=50, bg=BG)

window.bind("<Return>", new_words)
window.bind("<space>", submit_word)


text_canvas = Canvas(width=500, height=300, bg=TYPEFACE, highlightthickness=0)
text_id = text_canvas.create_text(
    200, 125,
    text=" ",
    fill="black",
    width=380,
    font=Font(family='Times New Roman', size=26, weight='normal'),
    anchor=tk.CENTER
)

text_canvas.grid(column=1, row=2)
clock_font = Font(family='Helvetica', size=18)

clock = Label(text=f"Time Remaining: {time_left} seconds", bg= BG)
clock.grid(pady=(25, 25), column=1, row=0, columnspan=2)

word_entry = Text(height=10, width=49, font=Font(family='Times New Roman', size=20, weight='normal'))
word_entry.grid(pady=(10, 0), column=0, row=4, columnspan=3)


start = Button(text="Start", highlightthickness=0, command=start_game)
start.grid(pady=(0, 15), column=1, row=1)


window.mainloop()