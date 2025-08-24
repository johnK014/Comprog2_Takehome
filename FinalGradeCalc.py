import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

student_records = {}


def compute_final_grade(raw):
    if 50 <= raw <= 54:
        return 3.0
    elif 55 <= raw <= 60:
        return 2.75
    elif 61 <= raw <= 66:
        return 2.5
    elif 67 <= raw <= 72:
        return 2.25
    elif 73 <= raw <= 78:
        return 2.0
    elif 79 <= raw <= 84:
        return 1.75
    elif 85 <= raw <= 90:
        return 1.5
    elif 91 <= raw <= 97:
        return 1.25
    elif 98 <= raw <= 100:
        return 1.0
    else:
        return 5.0


def generate_fields():
    try:
        quiz_count = int(quiz_count_entry.get())
        unit_count = int(unit_count_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
        return

    generate_quiz_fields(quiz_count)
    generate_unit_fields(unit_count)


def generate_quiz_fields(count):
    for i in range(count):
        tk.Label(quiz_frame, text=f"Quiz {i+1} Score:").grid(row=i, column=0)
        score_entry = tk.Entry(quiz_frame, width=10)
        score_entry.grid(row=i, column=1)
        quiz_score_entries.append(score_entry)

        tk.Label(quiz_frame, text="Items:").grid(row=i, column=2)
        item_entry = tk.Entry(quiz_frame, width=10)
        item_entry.grid(row=i, column=3)
        quiz_item_entries.append(item_entry)


def generate_unit_fields(count):
    for i in range(count):
        tk.Label(unit_frame, text=f"Unit {i+1} Score:").grid(row=i, column=0)
        score_entry = tk.Entry(unit_frame, width=10)
        score_entry.grid(row=i, column=1)
        unit_score_entries.append(score_entry)

        tk.Label(unit_frame, text="Items:").grid(row=i, column=2)
        item_entry = tk.Entry(unit_frame, width=10)
        item_entry.grid(row=i, column=3)
        unit_item_entries.append(item_entry)


def save_data():
    name = name_entry.get().strip()
    if not name:
        messagebox.showerror("Input Error", "Student name is required.")
        return

    try:
        quiz_scores = [float(e.get()) for e in quiz_score_entries]
        quiz_items = [float(e.get()) for e in quiz_item_entries]
        unit_scores = [float(e.get()) for e in unit_score_entries]
        unit_items = [float(e.get()) for e in unit_item_entries]
        term_score = float(term_score_entry.get())
        term_items = float(term_item_entry.get())
    except ValueError:
        messagebox.showerror(
            "Input Error", "All scores and items must be numeric.")
        return

    quiz_total = (sum(quiz_scores) / sum(quiz_items)) * \
        0.30 * 100 if sum(quiz_items) else 0
    unit_total = (sum(unit_scores) / sum(unit_items)) * \
        0.40 * 100 if sum(unit_items) else 0
    term_total = (term_score / term_items) * 0.30 * 100 if term_items else 0

    raw_grade = round(quiz_total + unit_total + term_total, 2)
    final_grade = compute_final_grade(raw_grade)

    student_records[name] = {
        "raw_grade": raw_grade,
        "final_grade": final_grade
    }

    filename = "student_grades.csv"
    write_header = not os.path.exists(
        filename) or os.path.getsize(filename) == 0
    csvfile = open(filename, "a", newline='')
    writer = csv.writer(csvfile, delimiter=' ')
    if write_header:
        writer.writerow(["student_name", "raw_grade", "final_grade"])
    for student, data in student_records.items():
        writer.writerow([student, data["raw_grade"], data["final_grade"]])

    csvfile.close()

    messagebox.showinfo(
        "Success", f"{name}'s Final Grade: {final_grade} ({raw_grade})")
    clear_data()


def open_table_window():
    filename = "student_grades.csv"
    if not os.path.exists(filename):
        messagebox.showerror("Error", "CSV file not found.")
        return

    csvfile = open(filename, "r", newline='')
    reader = csv.reader(csvfile, delimiter=' ')
    headers = next(reader)

    table_window = tk.Toplevel()
    table_window.title("Student Records Table")
    table_window.geometry("500x400")

    tree = ttk.Treeview(table_window, columns=headers, show="headings")
    for col in headers:
        tree.heading(col, text=col)
        tree.column(col, width=100)
        tree.column(col, anchor=tk.CENTER)
    tree.pack(padx=10, pady=10, expand=True, fill='both')

    for row in reader:
        tree.insert("", tk.END, values=row)

    csvfile.close()


def clear_data():
    name_entry.delete(0, tk.END)
    quiz_count_entry.delete(0, tk.END)
    unit_count_entry.delete(0, tk.END)
    term_score_entry.delete(0, tk.END)
    term_item_entry.delete(0, tk.END)

    for e in quiz_score_entries + quiz_item_entries + unit_score_entries + unit_item_entries:
        e.delete(0, tk.END)


# GUI Setup
app = tk.Tk()
app.title("Student Grade Calculator")
app.geometry("600x900")

tk.Label(app, text="Student Name:").pack()
name_entry = tk.Entry(app, width=40)
name_entry.pack()

tk.Label(app, text="Number of Quizzes:").pack()
quiz_count_entry = tk.Entry(app, width=10)
quiz_count_entry.pack()

tk.Label(app, text="Number of Unit Tests:").pack()
unit_count_entry = tk.Entry(app, width=10)
unit_count_entry.pack()

tk.Button(app, text="Generate Fields", command=generate_fields).pack(pady=5)

tk.Label(app, text="Enter Quiz Scores and Total Items").pack(pady=5)
quiz_frame = tk.Frame(app)
quiz_frame.pack()
quiz_score_entries = []
quiz_item_entries = []

tk.Label(app, text="Enter Unit Test Scores and Total Items").pack(pady=5)
unit_frame = tk.Frame(app)
unit_frame.pack()
unit_score_entries = []
unit_item_entries = []

tk.Label(app, text="Enter Term Test Score and Items").pack(pady=5)
term_frame = tk.Frame(app)
term_frame.pack()
term_score_entry = tk.Entry(term_frame, width=10)
term_score_entry.grid(row=0, column=0)
term_item_entry = tk.Entry(term_frame, width=10)
term_item_entry.grid(row=0, column=1)

tk.Button(app, text="Save Data", command=save_data).pack(pady=10)
tk.Button(app, text="View Records", command=open_table_window).pack(pady=5)
tk.Button(app, text="Clear Fields", command=clear_data).pack(pady=5)

app.mainloop()
