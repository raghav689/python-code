import tkinter as tk


def click(event):
    text = event.widget.cget("text")
    current_text = entry.get()

    if text == "=":
        try:
            # Evaluate the expression and show the result
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            # Handle any errors (e.g., invalid expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        # Clear the entry widget
        entry.delete(0, tk.END)
    else:
        # Append the button text to the entry widget
        entry.insert(tk.END, text)


# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget for input
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Create buttons
for i, text in enumerate(buttons):
    button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 18))
    button.grid(row=1 + i // 4, column=i % 4)
    button.bind("<Button-1>", click)

# Run the application
root.mainloop()
