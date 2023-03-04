import tkinter as ochko
from osnova_21 import *
import random
from class_21 import *

display = ochko.Tk()
display.title(f"21 OCHKO{random.choice(list(my_dict))}")
display.geometry("1900x600")
display.configure(bg="seagreen")

Label = ochko.Label(
    master=display,
    text=f"{random.choice(list(my_dict))} ИГРА 21 {random.choice(list(my_dict))}",
    fg="black",
    bg="red",
    width=20,
    height=3,
    font=("Times", 25)
)
Label.grid(row=1, column=2,padx=200)

playyer = ochko.Label(
    master=display,
    text="Игрок",
    fg="red",
    bg="black",
    height=2,
    width=20,
    font=("Arial", 20)
)
playyer.grid(row=5, column=1, padx=100)

mast_pl = ochko.Label(
    master=display,
    text="",
    height=1,
    width=0,
    bg="seagreen",
    font=("Arial", 15)
)
mast_pl.grid(row=6, column=1, sticky="e", padx=100)

dilleer = ochko.Label(
    master=display,
    text="Дилер",
    fg="red",
    bg="black",
    height=2,
    width=20,
    font=("Arial", 20)
)
dilleer.grid(row=5, column=3, padx=100)

mast_dl = ochko.Label(
    master=display,
    text="",
    height=1,
    width=0,
    bg="seagreen",
    font=("Arial", 15)
)
mast_dl.grid(row=6, column=3,sticky="e", padx=100)

exitt = ochko.Label(
    text="0:0",
    bg="black",
    fg="red",
    font=("Arial", 25),
    width=10,
    height=2
)
exitt.grid(row=5, column=2,pady=20)

question = ochko.Label(
    master=display,
    text="Хотите сыграть в 21 ?",
    fg="red",
    bg="black",
    height=3,
    width=27,
    font=("Arial", 20)   
)
question.grid(row=7, column=2, padx=0, pady=20)

def proverca_2():
    if play.player_status == "LOOS" or play.player_status == "WIN" or play.nichia == "НИЧЬЯ":
        vivodd.config(
            text=f"{play.vivod}"
        )
        mast_dl.config(
            text=f"{play.players_osn2}"
        )
        mast_pl.config(
            text=f"{play.players_osn1}"
        )
        question.config(
            text="Хотите еще сыграть в 21?"
        )
        exitt.config(
            text=f"{play.players1} : {play.players2}"
        )
        play.prov()
        
        but_yes["command"] = but_f
        but_no["command"] = ex
    display.after(random.randint(50,55), proverca_2)

def ex():
    exit()

def b_no():
    play.giv_card_diller()
    play.proverca()
    mast_dl.config(
        text=f"{play.players_osn2}"
    )
    exitt.config(
        text=f"{play.players1} : {play.players2}"
    )

def b_yes():
    play.giv_card_player()
    play.proverca() 
    mast_pl.config(
        text=f"{play.players_osn1}"
    )
    exitt.config(
            text=f"{play.players1} : {play.players2}"
        )
       
def but_f():
    play.rand_razdacha_player()
    play.ochko()
    vivodd.config(
        text="..."
    )
    mast_dl.config(
        text=f"{play.players_osn2}",
        bg="red"
    )
    mast_pl.config(
        text=f"{play.players_osn1}",
        bg="red"
    )
    question.config(
        text="Хотите взять еще одну карту ?"
    )
    exitt.config(
            text=f"{play.players1} : {play.players2}"
        )
    but_yes["command"]= b_yes
    but_no["command"] = b_no
    play.proverca()

but_yes = ochko.Button(
    master=display,
    text="ДА",
    bg="red",
    height=2,
    width=15,
    font=("Arial", 15),
    command=but_f
)
but_yes.grid(row=8, column=2, padx=0)

but_no = ochko.Button(
    master=display,
    text="НЕТ",
    bg="red",
    height=2,
    width=15,
    font=("Arial", 15),
    command=b_no
)
but_no.grid(row=9, column=2, padx=0)

vivodd = ochko.Label(
    master=display,
    text="...",
    bg="black",
    fg="red",
    height=2,
    width=12,
    font=("Arial", 20)
)
vivodd.grid(row=6, column=2, pady=0)

display.after(random.randint(50,55), proverca_2)

display.mainloop()