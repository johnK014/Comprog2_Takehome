import tkinter as tk
from tkinter import messagebox
import random


def setup_game():
    global target, guess_count, entry, result
    target = random.randint(1, 100)
    guess_count = 0

    app.title("Random Number Guessing Game")
    app.geometry("350x250")

    tk.Label(app, text="Guess a number between 1 and 100").pack(pady=10)

    entry = tk.Entry(app, width=10, font=("Arial", 14))
    entry.pack()

    result = tk.Label(app, text="", font=("Arial", 12))
    result.pack(pady=5)

    button_frame = tk.Frame(app)
    button_frame.pack(pady=10)

    submit_btn = tk.Button(
        button_frame, text="Submit Guess", command=check_guess)
    submit_btn.pack(side=tk.LEFT, padx=10)

    reset_btn = tk.Button(button_frame, text="Reset Game", command=reset_game)
    reset_btn.pack(side=tk.LEFT, padx=10)


def check_guess():
    global guess_count, target
    try:
        guess = int(entry.get())
        guess_count += 1

        if guess < 1 or guess > 100:
            result.config(text="Please enter a number from 1 to 100.")
        elif guess < target:
            result.config(text="Too low, try again.")
        elif guess > target:
            result.config(text="Too high, try again.")
        else:
            result.config(
                text=f"Congratulations! You guessed it in {guess_count} tries!")
    except ValueError:
        result.config(text="Invalid input. Enter an integer.")


def reset_game():
    global target, guess_count
    target = random.randint(1, 100)
    guess_count = 0
    entry.delete(0, tk.END)
    result.config(text="New number generated. Try again!")


app = tk.Tk()
setup_game()
app.mainloop()
