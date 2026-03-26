#budget tracker gui

import tkinter


# fenster erstellen/öffnen
root = tkinter.Tk()                 # root= fenster
root.title("budget_tracker")

entry = tkinter.Entry(root)         # entry=das gui feld insert=text schreiben
entry.pack()

root.mainloop()