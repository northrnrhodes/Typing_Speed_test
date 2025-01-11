from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
import tkinter as tk
import requests
import random
import time
from datetime import datetime

# start_time = time.time()
# time.sleep(60)
# end_time = time.time()
#
# elapsed_time = end_time -start_time
# print(elapsed_time)


BG = "#AF8F6F"
TYPEFACE ="#F8F4E1"

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()
WORD = []
for word in WORDS:
    words = word.decode("utf-8")
    WORD.append(words)




class Brains:
    def __init__(self):
        self.window = Tk()

        self.window.title("Speed Type Test")
        self.window.config(padx=50, pady=50, bg=BG)
        self.new_words()
        self.time_left = 60
        self.text_canvas = Canvas(width=500, height=300, bg=TYPEFACE, highlightthickness=0)
        self.text_canvas.create_text(200, 125, text=" ".join(self.words), fill="black", width=380, font=Font(family='Times New Roman', size=26, weight='normal'))
        self.text_canvas.grid(column=1, row=1)
        self.clock_font = Font(family='Helvetica', size=18)
        self.clock = Label(text=f"Time Remaining: {self.time_left} seconds", bg=BG, font=self.clock_font)

        self.clock.grid(pady=(25, 25), column=1, row=0, columnspan=2)

        self.word_entry = Text(height=10, width=49, font=Font(family='Times New Roman', size=20, weight='normal'))
        self.word_entry.grid(pady=(10, 0), column=0, row=3, columnspan=3)





    def display_speed(self):
        pass


    def new_words(self):
        self.words = []
        for i in range(30):
            self.words.append(random.choice(WORD))


    def update_clock(self, time_left):
        if time_left > 0:
            print(time_left)
            time_left = time_left -  1
            self.clock = Label(text=f"Time Remaining: {time_left} seconds", bg=BG, font=self.clock_font)
            return time_left, self.clock


        else:
            self.time_left = 0
            return False




