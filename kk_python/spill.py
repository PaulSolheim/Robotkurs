import tkinter
from random import randint

farger_engelsk = ['Red', 'Blue', 'Green', 'Pink', 'Black',
               'Yellow', 'Orange', 'Purple', 'Brown']
farger_norsk = ['Rød', 'Blå', 'Grønn', 'Rosa', 'Svart',
           'Gul', 'Oransje', 'Lilla', 'Brun']
fargenr = 0
poeng = 0
tid_igjen = 30

def start_spillet(event):
    if tid_igjen == 30:
        nedtelling()
    neste_farge()
    
def neste_farge():
    global fargenr
    global poeng
    if tid_igjen > 0:
        boks.focus_set()
        
    if boks.get().lower() == farger_norsk[fargenr].lower():
        poeng = poeng + 1
        
    boks.delete(0, tkinter.END)
    
    fargenr = randint(0, len(farger_norsk)-1)
    tekstnr = randint(0, len(farger_norsk)-1)
    
    tekst.config(fg=str(farger_engelsk[fargenr]), text=str(farger_norsk[tekstnr]))
    poeng_tekst.config(text="Poeng: " + str(poeng))
    
def nedtelling():
    global tid_igjen
    
    if tid_igjen > 0:
        tid_igjen = tid_igjen - 1
        tid_tekst.config(text="Tid igjen: " + str(tid_igjen))
        tid_tekst.after(1000, nedtelling)
    else:
        tid_tekst.pack_forget()
        tekst.pack_forget()
        boks.pack_forget()
            
vinduet = tkinter.Tk()
vinduet.title("fargespill")
vinduet.geometry("475x360")

instruks = tkinter.Label(vinduet,
                             text="skriv inn fargen PÅ ordet, ikke selve ordet!",
                             font=('Helvetica', 15))
instruks.pack()

poeng_tekst = tkinter.Label(vinduet,
                             text="trykk enter for å starte.",
                             font=('Helvetica', 30))
poeng_tekst.pack()

tid_tekst = tkinter.Label(vinduet,
                          text="Tid igjen: " + str(tid_igjen),
                          font=('Helvetica', 30))
tid_tekst.pack()

tekst = tkinter.Label(vinduet, font=('Helvetica', 100))
tekst.pack()

boks = tkinter.Entry(vinduet)

vinduet.bind('<Return>', start_spillet)
boks.pack()
boks.focus_set()

vinduet.mainloop()