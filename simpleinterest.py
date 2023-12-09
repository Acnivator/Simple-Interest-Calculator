import tkinter as tk

parent_window = tk.Tk()

parent_window.geometry("400x300")

parent_window.title("Interest Calculator")

parent_window.configure(bg="white")

heading_label = tk.Label(parent_window, text="Interest Calculator", font=("Arial", 18), bg="white")
heading_label.place(x=100, y=20)

principal_label = tk.Label(parent_window, text="Principal:", font=("Arial", 12), bg="white")
principal_label.place(x=50, y=80)

principal_entry = tk.Entry(parent_window, font=("Arial", 12))
principal_entry.place(x=150, y=80)

rate_label = tk.Label(parent_window, text="Rate of Interest:", font=("Arial", 12), bg="white")
rate_label.place(x=50, y=120)

rate_entry = tk.Entry(parent_window, font=("Arial", 12))
rate_entry.place(x=180, y=120)

time_label = tk.Label(parent_window, text="Time:", font=("Arial", 12), bg="white")
time_label.place(x=50, y=160)

time_entry = tk.Entry(parent_window, font=("Arial", 12))
time_entry.place(x=120, y=160)

calculate_button = tk.Button(parent_window, text="Calculate", font=("Arial", 12), bg="blue", fg="white")
calculate_button.place(x=150, y=200)

result_frame = tk.LabelFrame(parent_window, text="Result", font=("Arial", 12), bg="white")
result_frame.place(x=50, y=240, width=300, height=40)

result_label = tk.Label(result_frame, text="", font=("Arial", 12), bg="white")
result_label.pack()

def calculate_interest():

    p = float(principal_entry.get())
    
    r = float(rate_entry.get())
    
    t = float(time_entry.get())
    
    interest = (p * r * t) / 100
    
    interest = round(interest, 2)
    
    result_label.destroy()
    
    result_label = tk.Label(result_frame, text=f"The interest is: {interest}", font=("Arial", 12), bg="white")
    result_label.pack()

calculate_button.configure(command=calculate_interest)

parent_window.mainloop()