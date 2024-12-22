import tkinter as tk
from tkinter import messagebox
import random
import time

# Mapping choices
CHOICES = ["Rock", "Scissor", "Paper"]
EMOJIS = ["✊", "✌", "✋"]  # Rock, Scissor, Paper emojis

# Global variables for scores
player_score = 0
ai_score = 0

# Function to evaluate the result
def evaluate(player_move, ai_move):
    if player_move == ai_move:
        return 0  # Draw
    if (player_move == 0 and ai_move == 1) or \
       (player_move == 1 and ai_move == 2) or \
       (player_move == 2 and ai_move == 0):
        return 1  # Player wins
    return -1  # AI wins

# Function for AI's move
def get_ai_move():
    return random.randint(0, 2)

# Update result and scoreboard
def update_result(player_move):
    global player_score, ai_score

    ai_move = get_ai_move()
    result = evaluate(player_move, ai_move)

    result_label.config(text=f"AI chose: {CHOICES[ai_move]} {EMOJIS[ai_move]}")

    if result == 1:
        result_message.config(text="\U0001F389 You win!", fg="green")
        player_score += 1
    elif result == -1:
        result_message.config(text="\U0001F622 AI wins!", fg="red")
        ai_score += 1
    else:
        result_message.config(text="\U0001F610 It's a draw!", fg="blue")

    player_score_label.config(text=f"Player: {player_score}")
    ai_score_label.config(text=f"AI: {ai_score}")

# Quit game confirmation
def quit_game():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        root.destroy()

# Main tkinter window
root = tk.Tk()
root.title("Rock, Scissor, Paper Game")
root.geometry("400x500")
root.config(bg="#f4f4f4")

# Title and logo
title_frame = tk.Frame(root, bg="#f4f4f4")
title_frame.pack(pady=20)

logo_label = tk.Label(title_frame, text="\U0001F3AE", font=("Helvetica", 40), bg="#f4f4f4")  # Game controller emoji
logo_label.pack()

title = tk.Label(title_frame, text="Rock, Scissor, Paper", font=("Helvetica", 18, "bold"), bg="#f4f4f4", fg="#333")
title.pack()

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f4f4f4", fg="#555")
result_label.pack()

# Result message
result_message = tk.Label(root, text="", font=("Helvetica", 16, "bold"), bg="#f4f4f4")
result_message.pack(pady=10)

# Scoreboard
scoreboard_frame = tk.Frame(root, bg="#f4f4f4")
scoreboard_frame.pack(pady=10)

player_score_label = tk.Label(scoreboard_frame, text="Player: 0", font=("Helvetica", 14), bg="#f4f4f4", fg="#333")
player_score_label.grid(row=0, column=0, padx=20)

ai_score_label = tk.Label(scoreboard_frame, text="AI: 0", font=("Helvetica", 14), bg="#f4f4f4", fg="#333")
ai_score_label.grid(row=0, column=1, padx=20)

# Buttons for choices
button_frame = tk.Frame(root, bg="#f4f4f4")
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text=f"Rock {EMOJIS[0]}", font=("Helvetica", 14), width=10, command=lambda: update_result(0))
rock_button.grid(row=0, column=0, padx=10)

scissor_button = tk.Button(button_frame, text=f"Scissor {EMOJIS[1]}", font=("Helvetica", 14), width=10, command=lambda: update_result(1))
scissor_button.grid(row=0, column=1, padx=10)

paper_button = tk.Button(button_frame, text=f"Paper {EMOJIS[2]}", font=("Helvetica", 14), width=10, command=lambda: update_result(2))
paper_button.grid(row=0, column=2, padx=10)

# Quit button
quit_button = tk.Button(root, text="Quit", font=("Helvetica", 14), bg="red", fg="white", command=quit_game)
quit_button.pack(pady=20)

# Run the application
root.mainloop()
