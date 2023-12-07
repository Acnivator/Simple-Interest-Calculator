import tkinter as tk
from tkinter import Label, Entry, Button, LabelFrame

def calculate_interest():
    try:
        p = float(principal_entry.get())
        r = float(rate_entry.get())
        t = float(time_entry.get())

        result = (p * r * t) / 100
        result = round(result, 2)

        result_show_label.config(text=f"Simple Interest: {result}")
    except ValueError:
        result_show_label.config(text="Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Simple Interest Calculator")
root.geometry("400x300")
root.configure(bg='#f0f0f0')

# Heading Label
heading_label = Label(root, text="Simple Interest Calculator", font=("Calibri", 16, "bold"), bg='#f0f0f0')
heading_label.place(x=50, y=10)

# Principal Label and Entry
principal_label = Label(root, text="Principal:", font=("Calibri", 12), bg='#f0f0f0')
principal_label.place(x=50, y=60)
principal_entry = Entry(root)
principal_entry.place(x=180, y=60)

# Rate of Interest Label and Entry
rate_label = Label(root, text="Rate of Interest:", font=("Calibri", 12), bg='#f0f0f0')
rate_label.place(x=50, y=100)
rate_entry = Entry(root)
rate_entry.place(x=180, y=100)

# Time Label and Entry
time_label = Label(root, text="Time (in years):", font=("Calibri", 12), bg='#f0f0f0')
time_label.place(x=50, y=140)
time_entry = Entry(root)
time_entry.place(x=180, y=140)

# Calculation Button
calculate_button = Button(root, text="Calculate", command=calculate_interest, bg='#4caf50', fg='white')
calculate_button.place(x=180, y=180)

# Result Frame Container
result_frame = LabelFrame(root, text="Result", font=("Calibri", 12), bg='#f0f0f0', padx=10, pady=10)
result_frame.place(x=50, y=220)

# Result Show Label
result_show_label = Label(result_frame, text="", font=("Calibri", 12), bg='#f0f0f0')
result_show_label.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
