import tkinter
from random import randint

farger_engelsk = ['Red', 'Blue', 'Green', 'Pink', 'Black',
               'Yellow', 'Orange', 'Purple', 'Brown']
farger_norsk = ['Rød', 'Blå', 'Grønn', 'Rosa', 'Svart',
           'Gul', 'Oransje', 'Lilla', 'Brun']

tid_igjen = 30

def nedtelling():
    global tid_igjen
    
    if tid_igjen > 0:
        tid_igjen = tid_igjen - 1
        tid_label.config(text="tid igjen: " + str(tid_igjen))
        
vinduet = tkinter.Tk()
vinduet.title("fargespill")
vinduet.geometry("475x360")

instruks = tkinter.Label(vinduet,
                             text="skriv inn fargen PÅ ordet, ikke selve ordet!",
                             font=('Helvetica', 15))

instruks.pack()

poeng_label = tkinter.Label(vinduet,
                             text="trykk enter for å starte.",
                             font=('Helvetica', 30))

poeng_label.pack()

label = tkinter.Label(vinduet, font=('Helvetica', 100))
label.pack()

boks = tkinter.Entry(vinduet)

vinduet.mainloop()

