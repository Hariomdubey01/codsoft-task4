import tkinter as tk
from tkinter import messagebox
import random

choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0
round_number = 1

def play(user_choice):
    global user_score, computer_score, round_number

    computer_choice = random.choice(choices)

    result_text = f"You chose {user_choice} | Computer chose {computer_choice}\n"

    if user_choice == computer_choice:
        result = "🤝 It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Scissors" and computer_choice == "Paper") or
        (user_choice == "Paper" and computer_choice == "Rock")
    ):
        result = "🎉 You Win!"
        user_score += 1
    else:
        result = "💻 Computer Wins!"
        computer_score += 1

    result_text += f"\n\n{result}"

    result_label.config(text=result_text)
    score_label.config(text=f"Score → You: {user_score} | Computer: {computer_score}")
    round_label.config(text=f"Round: {round_number}")
    round_number += 1

def reset_game():
    global user_score, computer_score, round_number
    user_score = 0
    computer_score = 0
    round_number = 1
    result_label.config(text="")
    score_label.config(text="Score → You: 0 | Computer: 0")
    round_label.config(text="Round: 1")

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.configure(bg="#1f1f2e")
root.resizable(False, False)

window_width, window_height = 450, 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coord = (screen_width - window_width) // 2
y_coord = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_coord}+{y_coord}")

FONT_TITLE = ("Segoe UI", 18, "bold")
FONT_TEXT = ("Segoe UI", 12)
BTN_COLOR = "#6c5ce7"
BTN_HOVER = "#a29bfe"
BTN_RESET = "#00b894"

tk.Label(root, text="🪨 📄 ✂️  Rock Paper Scissors", font=FONT_TITLE, bg="#1f1f2e", fg="white").pack(pady=15)

round_label = tk.Label(root, text=f"Round: {round_number}", font=FONT_TEXT, bg="#1f1f2e", fg="white")
round_label.pack()

score_label = tk.Label(root, text=f"Score → You: 0 | Computer: 0", font=FONT_TEXT, bg="#1f1f2e", fg="white")
score_label.pack(pady=5)


result_label = tk.Label(root, text="", font=("Segoe UI", 12, "italic"), bg="#1f1f2e", fg="#00ffcc",
                        wraplength=400, justify="center")
result_label.pack(pady=10)


button_frame = tk.Frame(root, bg="#1f1f2e")
button_frame.pack(pady=5)

def create_choice_button(text):
    btn = tk.Button(button_frame, text=text, font=FONT_TEXT, bg=BTN_COLOR, fg="white",
                    width=12, height=2, relief="flat", command=lambda: play(text))
    btn.pack(side=tk.LEFT, padx=10)

    btn.bind("<Enter>", lambda e: btn.config(bg=BTN_HOVER))
    btn.bind("<Leave>", lambda e: btn.config(bg=BTN_COLOR))


for choice in choices:
    create_choice_button(choice)

reset_frame = tk.Frame(root, bg="#1f1f2e")
reset_frame.pack(pady=20)

reset_button = tk.Button(reset_frame, text="🔁 Reset Game", font=FONT_TEXT, bg=BTN_RESET, fg="white",
                         command=reset_game, relief="flat", padx=10, pady=6)
reset_button.pack()
reset_button.bind("<Enter>", lambda e: reset_button.config(bg="#26de81"))
reset_button.bind("<Leave>", lambda e: reset_button.config(bg=BTN_RESET))

root.mainloop()
