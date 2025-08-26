import tkinter as tk
import random


def check_guess():
    global guess_count, target
    try:
        guess = int(entry.get())
        guess_count += 1

        if guess < 1 or guess > 100:
            feedback.config(text="Please enter a number from 1 to 100.")
        elif guess < target:
            feedback.config(text="Too low, try again.")
        elif guess > target:
            feedback.config(text="Too high, try again.")
        else:
            feedback.config(text=f"Correct! Guessed in {guess_count} tries.")
    except ValueError:
        feedback.config(text="Invalid input. Enter an integer.")


def reset_game():
    global target, guess_count
    target = random.randint(1, 100)
    guess_count = 0
    entry.delete(0, tk.END)
    feedback.config(text="New number generated. Try again!")


# --- GUI Setup ---
app = tk.Tk()
app.title("Random Number Guessing Game")
app.geometry("350x250")

target = random.randint(1, 100)
guess_count = 0

tk.Label(app, text="Guess a number between 1 and 100").pack(pady=10)

entry = tk.Entry(app, width=10, font=("Arial", 14))
entry.pack()

feedback = tk.Label(app, text="", font=("Arial", 12))
feedback.pack(pady=5)

button_frame = tk.Frame(app)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Submit Guess",
          command=check_guess).pack(side=tk.LEFT, padx=10)
tk.Button(button_frame, text="Reset Game",
          command=reset_game).pack(side=tk.LEFT, padx=10)

app.mainloop()
