import tkinter as tk
from tkinter import messagebox


def calculate_sleep_debt():
    desired_sleep_per_day = 8
    total_desired_sleep = desired_sleep_per_day * 7
    total_actual_sleep = 0

    try:
        for i in range(7):
            hours = float(entries[i].get())
            if hours < 0:
                messagebox.showerror(
                    "Invalid Input", f"Day {i+1}: Sleep hours can't be negative.")
                return
            total_actual_sleep += hours
    except ValueError:
        messagebox.showerror(
            "Invalid Input", "Please enter valid numbers for all days.")
        return

    sleep_debt = total_desired_sleep - total_actual_sleep

    report = f"Total sleep needed: {total_desired_sleep} hours\n"
    report += f"Total sleep you got: {total_actual_sleep} hours\n\n"

    if sleep_debt > 0:
        report += f"You have a sleep debt of {sleep_debt:.1f} hours. Time to catch up!"
    else:
        report += "No sleep debt detected. I'm jealous of your sleep discipline!"

    output_label.config(text=report)


# GUI setup
app = tk.Tk()
app.title("Sleep Debt Calculator")
app.geometry("350x400")

tk.Label(app, text="Enter your sleep hours for the past 7 days:").pack(pady=20)

entries = []
for i in range(7):
    frame = tk.Frame(app)
    frame.pack()
    tk.Label(frame, text=f"Day {i+1}:").pack(side=tk.LEFT)
    entry = tk.Entry(frame)
    entry.pack(side=tk.LEFT)
    entries.append(entry)

tk.Button(app, text="Calculate Sleep Debt",
          command=calculate_sleep_debt).pack(pady=20)

output_label = tk.Label(app, text="", font=(
    "Arial", 12), wraplength=300, justify="left")
output_label.pack(pady=10)

app.mainloop()
