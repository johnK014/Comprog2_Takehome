from tkinter import messagebox
import tkinter as tk


def convert_to_roman():
    roman_numerals = ["I", "II", "III", "IV",
                      "V", "VI", "VII", "VIII", "IX", "X"]
    try:
        number = int(entry.get())
        if 1 <= number <= 10:
            output_label.config(
                text=f"Roman numeral: {roman_numerals[number - 1]}")
        else:
            messagebox.showerror(
                "Invalid Input", "Please enter a number between 1 and 10.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")


app = tk.Tk()
app.geometry("300x200")
app.title("Roman Numeral Converter")

tk.Label(app, text="Enter a number (1–10)").pack(pady=5)
entry = tk.Entry(app)
entry.pack(pady=5)

tk.Button(app, text="Convert", command=convert_to_roman).pack(pady=5)
output_label = tk.Label(app, text="", font=("Arial", 14))
output_label.pack(pady=10)

app.mainloop()
