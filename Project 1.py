import tkinter as tk

root = tk.Tk()
root.title("Canvas and Shapes")
root.geometry("400x300")

canvas = tk.Canvas(root, bg="white", width=300, height=200)
canvas.pack()

# Draw a red rectangle
canvas.create_rectangle(50, 50, 150, 100, fill="red")

# Draw a blue oval
canvas.create_oval(200, 50, 250, 100, fill="blue")

# Draw a green line
canvas.create_line(50, 150, 250, 150, fill="green", width=5)

root.mainloop()
