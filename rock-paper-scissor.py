import random
import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.title("rock paper scissor Game")

user_score = 0
comp_score = 0
user_choice = ""
comp_choice = ""


def choice_to_number(choice):
    rps = {'rock': 0, 'paper': 1, 'scissor': 2}
    return rps[choice]


def number_to_choice(number):
    rps = {0: 'rock', 1: 'paper', 2: 'scissor'}
    return rps[number]


def random_computer_choice():
    return random.choice(['rock', 'paper', 'scissor'])


def result(human_choice, computer_chooice):
    global user_score
    global comp_choice
    user = choice_to_number(human_choice)
    comp = choice_to_number(computer_chooice)
    if (user == comp):
        print("Tie")
    elif ((user-comp) % 3 == 1):
        print("you win")
    else:
        print("comp win")
    text_area = tk.Text(master=window, height=12, width=30, bg="#FFFF99")
    text_area.grid(column=0, row=4)
    answer = "your choice : {uc} \nComputer choice: {cc} \n your score: {u}"
    text_area.insert(tk.END, answer)


def rock():
    global user_choice
    global comp_choice
    user_choice = 'rock'
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)


def paper():
    global user_choice
    global comp_choice
    user_choice = 'paper'
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)


def scissor():
    global user_choice
    global comp_choice
    user_choice = 'scissor'
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)


button1 = tk.Button(text="Rock",bg="skyblue",command=rock)
button1.grid(column=0,row=1)
button2 = 