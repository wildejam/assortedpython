import tkinter as tk

HEIGHT = 700
WIDTH = 800
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='blue')
frame.place(relwidth=1, relheight=1)

button = tk.Button(root, text="Test button", bg='gray', fg='red')
button.pack()

root.mainloop()