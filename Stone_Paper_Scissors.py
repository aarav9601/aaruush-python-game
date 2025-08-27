#Running a simple stone paper scissors game using tkinter

#This code creates a GUI application for a Stone Paper Scissors game using the tkinter library in Python. 
#It includes a warning window that animates into view, a main game window with buttons for user choices, and a point system to track scores. 
#The game continues until either the user or the computer reaches 10 points, at which point a "Play Again" button appears to reset the game. 

import tkinter as tk
import random

def animate_window(window, target_x, target_y, step=20):
        window.after(10, animate_window, window, target_x, target_y, step)

def show_rule_window():
    warning_window.destroy()
    rule_window.deiconify()

def show_main_window():
    rule_window.destroy()
    windows.deiconify()
    
# Point system variables
user_points = 0
computer_points = 0
max_points = 10

def play(user_choice):
    global user_points, computer_points
    choices = ["Rock", "Paper", "Scissor"]
    computer_choice = random.choice(choices)
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissor") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissor" and computer_choice == "Paper"):
        result = "You Win!"
        user_points += 1
    else:
        result = "You Lose!"
        computer_points += 1

    result_label.config(
        text=f"Your choice: {user_choice}\nComputer: {computer_choice}\nResult: {result}\n\nYour Points: {user_points}\nComputer Points: {computer_points}"
    )

    # Check for game end
    if user_points >= max_points or computer_points >= max_points:
        if user_points > computer_points:
            end_text = "Game Over! You Win!"
        elif computer_points > user_points:
            end_text = "Game Over! Computer Wins!"
        else:
            end_text = "Game Over! It's a Tie!"
        result_label.config(
            text=f"{end_text}\n\nYour Points: {user_points}\nComputer Points: {computer_points}"
        )
        play_again_btn.pack(pady=10) 
        # Disable choice buttons
        rock_btn.config(state="disabled")
        paper_btn.config(state="disabled")
        scissor_btn.config(state="disabled")

def play_again():
    global user_points, computer_points
    user_points = 0
    computer_points = 0
    result_label.config(text="")
    play_again_btn.pack_forget() 
    rock_btn.config(state="normal")
    paper_btn.config(state="normal")
    scissor_btn.config(state="normal")

windows = tk.Tk()
windows.title("Stone Paper Scissors")
windows.geometry("1080x720") 
windows.withdraw()

# Rule Window (hidden initially)
rule_window = tk.Toplevel()
rule_window.title("Rules")
rule_window.geometry("800x600")
rule_window.withdraw()

font2 = ("Arial", 35, "bold")
font3 = ("Arial", 25, "bold")

rules_label = tk.Label(
    rule_window, 
    text="Rules: \n \n 1. Rock crushes Scissors \n 2. Scissors cuts Paper \n 3. Paper covers Rock \n \n First to 10 points wins!",
    font=font2, 
    justify="center"
)
rules_label.pack(pady=20)

continue_rule_btn = tk.Button(
    rule_window,
    text="Continue",
    font=font3,
    bg="green",
    command=show_main_window
)
continue_rule_btn.pack(pady=40)

# Centering the warning window
warning_width = 1000
warning_height = 720
screen_width = windows.winfo_screenwidth()
screen_height = windows.winfo_screenheight()
target_x = (screen_width // 2) - (warning_width // 2)
target_y = (screen_height // 2) - (warning_height // 2)
start_y = 0

# Warning Window
warning_window = tk.Toplevel()
warning_window.title("Warning")
warning_window.geometry(f"{warning_width}x{warning_height}+{target_x}+{start_y}")

warning_label = tk.Label(
    warning_window, 
    text="Team Envision Project \n \n This game is under Development \n \n Note:This is a Computer Based Game ", 
    font=font2, 
    justify="center"
)
warning_label.pack(pady=60)

continue_button = tk.Button(
    warning_window, 
    text="Continue", 
    font=font3 , 
    bg="red",
    command=show_rule_window
)
continue_button.pack(pady=100)

# Animation
warning_window.after(10, animate_window, warning_window, target_x, target_y)

warning_window.deiconify() 

#Text and Input
from tkinter import font

font1 = font.Font(family='Arial', size=20)
label1 = tk.Label(windows, text="Stone Paper Scissor Game: ", font=font1)
label1.pack(pady=20)


# GIF 
# Load GIF frames (chat gpt helped)
frames = []
i = 0
while True:
    try:
        frame = tk.PhotoImage(file="C:\\Users\\Aarav Goel\\Documents\\Aaruush\\Images\\GIF.gif", format=f"gif -index {i}")
        frames.append(frame)
        i += 1
    except tk.TclError:
        break

img_label = tk.Label(windows)
img_label.pack(pady=20)

def animate_gif(label, frames, delay, idx=0):
    label.configure(image=frames[idx])
    windows.after(delay, animate_gif, label, frames, delay, (idx + 1) % len(frames))

# Start GIF animation
windows.after(0, animate_gif, img_label, frames, 100)

# Rock Paper Game Logic
button_frame = tk.Frame(windows)
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissor_btn = tk.Button(button_frame, text="Scissor", width=10, command=lambda: play("Scissor"))
scissor_btn.grid(row=0, column=2, padx=10)

result_label = tk.Label(windows, text="", font=("Arial", 18))
result_label.pack(pady=20)

# Play Again button (initially hidden)
play_again_btn = tk.Button(windows, text="Play Again", font=("Arial", 14), command=play_again)
play_again_btn.pack_forget()



windows.mainloop()

