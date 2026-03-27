#budget tracker gui

import tkinter

#knöpfe mit oop
class budget_tracker:
    def __init__(self,root):
        self.root = root
        self.root.title("Budget Tracker")
        self.root.geometry("300x200")         # größe fenster

        # fenster erstellen/öffnen
        self.entry_typ = tkinter.Entry(root)        #Eingabe für Typ
        self.entry_typ.pack()
        self.entry_typ.insert(0,"Typ")
        self.entry_category = tkinter.Entry(root)   #Eingabe für Kategorie
        self.entry_category.pack()
        self.entry_category.insert(0, "Kategorie")
        self.entry_price = tkinter.Entry(root)      #Eingabe für Preis
        self.entry_price.pack()
        self.entry_price.insert(0, "Preis")

    def button_typ_click(self):
        typ_wert = self.entry_typ.get()
        print(typ_wert)

    #klassen
    def typ(self):
        pass
    def category(self):
        pass
    def price(self):
        pass

    #unterklassen
    #def expenses(self):
    #def revenue(self):

    #erstellen knöpfe
        #self.button = tkinter.Button(root, text="Typ", command=self.button_typ_click)
        #self.button.pack()
        #self.button_category = tkinter.Button(root, text="Category", command=self.button_category_click)
        #self.button_category.pack()
        #self.button_price = tkinter.Button(root, text="Preis", command=self.button_price_click)
        #self.button_price.pack()


#starten
root=tkinter.Tk()    #Tk-Klasse aufrufen und hauptfenster erstellen
tracker = budget_tracker(root)              # ruft die klasse auf und erstellt knöpfe etc
root.mainloop()     #starten schleife