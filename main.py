from tkinter import *
import random
import pandas as pd

#Constants
FONT = "Arial"
score = 0
total_words = 0
BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
data_dict = {}

#csv data
try:
    data = pd.read_csv("./data/words_to_learn.csv")
    total_words = len(data)
except FileNotFoundError:
    data = pd.read_csv("./data/german_words_100.csv")
    data_dict = data.to_dict(orient="records")
    total_words = 100

else:
    data_dict = data.to_dict(orient="records")


#next card
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_image,image=card_front)
    canvas.itemconfig(title_text,text="German",fill="black")
    canvas.itemconfig(word_text,text= current_card["German"],fill="black")
    canvas.itemconfig(score_text,text= f"Score: {score}/{total_words}",fill="black")
    flip_timer = window.after(3000, flip_card)

#flip card
def flip_card():
    canvas.itemconfig(card_image,image=card_back)
    canvas.itemconfig(title_text,text="English",fill="white")
    canvas.itemconfig(word_text,text= current_card["English"],fill="white")
    canvas.itemconfig(score_text,text= f"Score: {score}/{total_words}",fill="white")


def is_known():
    global score
    score += 1
    data_dict.remove(current_card)
    new_data = pd.DataFrame(data_dict)
    new_data.to_csv("data/words_to_learn.csv",index=False)
    next_card()




#UI setup
window = Tk()
window.title("Flashy - DE to EN")
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)



card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right_button_image = PhotoImage(file="./images/right.png")
wrong_button_image = PhotoImage(file="./images/wrong.png")

canvas = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)
card_image = canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400,150,font=(FONT,40,"italic"),fill="black")
word_text = canvas.create_text(400,263,font=(FONT,60,"bold"),fill="black")
score_text = canvas.create_text(400,450, font=(FONT,30,"normal"),fill="black")
canvas.grid(row=0,column=0,columnspan=2)

# score_label = Label(text=f"Score: {score}",font=(FONT,30,"normal"))
# score_label.grid(row=1,column=)



right_button = Button(image=right_button_image,bg=BACKGROUND_COLOR,
                      highlightthickness=0,borderwidth=0,command=is_known)
right_button.grid(row=1,column=1)
wrong_button = Button(image=wrong_button_image,bg=BACKGROUND_COLOR,
                      highlightthickness=0,borderwidth=0,command=next_card)
wrong_button.grid(row=1,column=0)


next_card()


















window.mainloop()