import tkinter
from random import randint

def countdown():
    global time_left
    
    if time_left > 0:
        time_left = time_left - 1
        time_label.config(text="tid igjen: " + str(time_left))
        
root = tkinter.Tk()
root.title("fargespill")
root.geometry("475x360")

instructions = tkinter.Label(root,
                             text="skriv inn fargen PÅ ordet, ikke selve ordet!",
                             font=('Helvetica', 15))

instructions.pack()

points_label = tkinter.Label(root,
                             text="trykk enter for å starte.",
                             font=('Helvetica', 30))

points_label.pack()

label = tkinter.Label(root, font=('Helvetica', 100))
label.pack()

box = tkinter.Entry(root)

root.mainloop()

