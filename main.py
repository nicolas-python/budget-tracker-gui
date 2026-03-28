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
        self.entry_category = tkinter.Entry(root)   #Eingabe für Kategorie
        self.entry_category.pack()
        self.entry_price = tkinter.Entry(root)      #Eingabe für Preis
        self.entry_price.pack()

        # erstellen knöpfe
        self.button = tkinter.Button(root, text="Typ", command=self.button_typ_click)
        self.button.pack()

        self.button_category = tkinter.Button(root, text="Category", command=self.button_category_click)
        self.button_category.pack()

        self.button_price = tkinter.Button(root, text="Preis", command=self.button_price_click)
        self.button_price.pack()

        #unterklassen knöpfe_typ
        self.button_income = tkinter.Button(root, text="Einnahme", command=lambda: self.set_typ("Einnahme"))   #lambda: wenn geklickt wird → rufe set_typ(Einnahme) auf
        self.button_income.pack_forget()                        #forget() verteckt erstmal den knopf

        self.button_expense = tkinter.Button(root, text="Ausgabe", command=lambda: self.set_typ("Ausgabe"))
        self.button_expense.pack_forget()        #forget() verteckt erstmal den knopf

        #_category
        self.button_fixed_costs = tkinter.Button(root, text="Fixkosten",command=lambda: self.set_category("Fixkosten"))
        self.button_fixed_costs.pack_forget()

        self.button_hobbies = tkinter.Button(root, text="Hobbys", command=lambda: self.set_hobbies("Hobbys"))
        self.button_hobbies.pack_forget()

        self.button_food = tkinter.Button(root, text="Essen", command=lambda: self.set_food("Essen"))
        self.button_food.pack_forget()

        #_price
        self.button_price_value = tkinter.Button(root, text="Preis", command=lambda: self.set_price_value("Preis"))
        self.button_price_value.pack_forget()


        #knöpfe benutzen
    def button_typ_click(self):
        typ_wert = self.entry_typ.get()
        print("Typ:", typ_wert)

        self.button_income.pack()
        self.button_expense.pack()

    def button_category_click(self):
        kategorie_wert = self.entry_category.get()
        print("Kategorie:", kategorie_wert)

        self.button_fixed_costs.pack()
        self.button_hobbies.pack()
        self.button_food.pack()

    def button_price_click(self):
        preis_wert = self.entry_price.get()
        print("Preis:", preis_wert)

        self.button_price_value.pack()

    #klassen
    def typ(self):
        self.button_income.pack()
        self.button_expense.pack()

    def category(self):
        self.button_fixed_costs.pack()
        self.button_hobbies.pack()
        self.button_food.pack()

    def price(self):
        self.button_price_value.pack()

    #unterklassen für butten clicks+anzeige durch print
    def set_typ(self, wert):
        print("Typ ausgewählt:", wert)

    def set_category(self, wert):
        print("Kategorie ausgewählt:", wert)

    def set_hobbies(self, wert):
        print("Hobby ausgewählt:", wert)

    def set_food(self, wert):
        print("Essen ausgewählt:", wert)

    def set_price_value(self, wert):
        print("Preiswert ausgewählt:", wert)

#starten
root=tkinter.Tk()    #Tk-Klasse aufrufen und hauptfenster erstellen
tracker = budget_tracker(root)              # ruft die klasse auf und erstellt knöpfe etc
root.mainloop()     #starten schleife