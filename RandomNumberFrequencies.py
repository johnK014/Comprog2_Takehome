import random
import tkinter as tk


def generate_frequencies():
    freq = {}

    for _ in range(100):
        num = random.randint(1, 10)
        freq[num] = freq.get(num, 0) + 1

    output_box.delete("1.0", tk.END)

    output_box.insert(tk.END, "--- Frequency Report ---\n\n")
    for k in sorted(freq):
        output_box.insert(tk.END, f"Number {k}: {freq[k]} times\n")


# GUI setup
app = tk.Tk()
app.title("Random Number Frequency Tracker")
app.geometry("350x400")

tk.Label(app, text="Click the button to generate 100 random numbers").pack(pady=10)

tk.Button(app, text="Generate Frequencies",
          command=generate_frequencies).pack(pady=5)

output_box = tk.Text(app, width=50, height=15, font=("Courier", 10))
output_box.pack(pady=10)

app.mainloop()
