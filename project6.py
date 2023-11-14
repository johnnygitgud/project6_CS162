import tkinter as tk
import random
import time

# Create the main window
root = tk.Tk()
root.title("Sorting Visualization")
root.minsize(800, 600)

# Create a list of 10 random integers
# List comprehension is used: remember that the loop executes before the expression
# The expression in this case is random.randint
rand_list = [random.randint(1, 100) for i in range(10)]
print(rand_list)

# Create a canvas to display rectangles
canvas = tk.Canvas(root, width=600, height=300)
canvas.pack(pady=20)

# Initialize the rectangles with random heights
#Question for Joseph? How are rectangles created without a slant when the y coordinates are not the same?
#Does tkinter just ignore the slope?
rectangles = []
for index, value in enumerate(rand_list):
    x1 = 10 + index * 60
    x2 = x1 + 40
    y1 = 250
    y2 = y1 - value * 2
    rect = canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
    rectangles.append(rect)

# Function to highlight and swap rectangles
def highlight_and_swap(a, b):
    canvas.itemconfig(rectangles[a], fill="red")
    canvas.itemconfig(rectangles[b], fill="red")
    root.update()
    time.sleep(0.2)
    rand_list[a], rand_list[b] = rand_list[b], rand_list[a]
    redraw_rectangles()
    canvas.itemconfig(rectangles[a], fill="blue")
    canvas.itemconfig(rectangles[b], fill="blue")
    root.update()
    time.sleep(0.2)

# Function to redraw rectangles
def redraw_rectangles():
    for i, value in enumerate(rand_list):
        x1 = 10 + i * 60
        x2 = x1 + 40
        y1 = 250
        y2 = y1 - value * 2
        canvas.coords(rectangles[i], x1, y1, x2, y2)

# Function to perform sorting (Bubble Sort)
def perform_sort(): 
    n = len(rand_list)
    print(n)
    for i in range(n):
        print(i)
        for j in range(0, n-i-1):
            print(j)
            if rand_list[j] > rand_list[j+1]:
                highlight_and_swap(j, j+1)

# Create a button to start the sort process
sort_button = tk.Button(root, text="Start Sort", command=perform_sort)
sort_button.pack()

# Main event loop
root.mainloop()
