import tkinter as tk

window = tk.Tk()

for i in range(3):
    for j in range(3):
        frname = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frname.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frname, text=f"Row {i}\nColumn {j}")
        label.pack()
        
window.mainloop()