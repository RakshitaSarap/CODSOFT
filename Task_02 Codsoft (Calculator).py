import tkinter as tk

def button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

entry = tk.Entry(root, font=("Arial", 20))
entry.pack(fill=tk.BOTH, padx=10, pady=10, ipadx=10, ipady=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

row, col = 1, 0

for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, font=("Arial", 20), width=5, height=2)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
