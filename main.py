#budget tracker gui

import tkinter

#knöpfe mit oop
class budget_tracker:
    def __init__(self,root):
        self.root = root
        self.root.title("Budget Tracker")
        self.root.geometry("400x350")         # größe fenster

        #variablen für liste(zwischenspeichern)
        self.typ = ""
        self.category = ""
        self.price = ""

        # fenster erstellen/öffnen
        self.entry_typ = tkinter.Entry(root)        #Eingabe für Typ
        self.entry_typ.pack()
        self.entry_category = tkinter.Entry(root)   #Eingabe für Kategorie
        self.entry_category.pack()
        self.entry_price = tkinter.Entry(root)      #Eingabe für Preis
        self.entry_price.pack()

        #liste
        self.listbox = tkinter.Listbox(root)  #zeigt alle Einträge, liste im fenster
        self.listbox.pack()

        # erstellen knöpfe
        self.button = tkinter.Button(root, text="Typ", command=self.button_typ_click)
        self.button.pack()

        self.button_category = tkinter.Button(root, text="Category", command=self.button_category_click)
        self.button_category.pack()

        self.button_price = tkinter.Button(root, text="Preis", command=self.button_price_click)
        self.button_price.pack()

        #unterklassen knöpfe
        # _typ
        self.frame_typ = tkinter.Frame(root)        #frame =Mini-Container innerhalb des Fensters man kan alles darin verstecken (root im vergleich Hauptfenster)
        self.button_income = tkinter.Button(self.frame_typ, text="Einnahme", command=lambda: self.set_typ("Einnahme"))   #lambda: wenn geklickt wird → rufe set_typ(Einnahme) auf
        self.button_income.pack()

        self.button_expense = tkinter.Button(self.frame_typ, text="Ausgabe", command=lambda: self.set_typ("Ausgabe"))
        self.button_expense.pack()
        self.frame_typ.pack_forget()       #forget() verteckt erstmal den knopf

        #_category
        self.frame_category = tkinter.Frame(root)
        self.button_fixed_costs = tkinter.Button(self.frame_category, text="Fixkosten",command=lambda: self.set_category("Fixkosten"))
        self.button_fixed_costs.pack()

        self.button_hobbies = tkinter.Button(self.frame_category, text="Hobbys", command=lambda: self.set_hobbies("Hobbys"))
        self.button_hobbies.pack()

        self.button_food = tkinter.Button(self.frame_category, text="Essen", command=lambda: self.set_food("Essen"))
        self.button_food.pack()
        self.frame_category.pack_forget()

        #_price
        self.frame_price = tkinter.Frame(root)
        self.button_price_value = tkinter.Button(self.frame_price, text="Preis", command=lambda: self.set_price_value("Preis"))
        self.button_price_value.pack()
        self.frame_price.pack_forget()

        self.button_save = tkinter.Button(root, text="Speichern", command=self.save_entry)  #speichert alles
        self.button_save.pack()

        #knöpfe benutzen
    def button_typ_click(self):
        typ_wert = self.entry_typ.get()
        print("Typ:", typ_wert)

        self.hide_all_frames()  #alle Frames ausblenden
        self.frame_typ.pack()  #nur Typ-Frame anzeigen

    def button_category_click(self):
        category_wert = self.entry_category.get()
        print("Kategorie:", category_wert)

        self.hide_all_frames()
        self.frame_category.pack()  #nur Kategorie-Frame anzeigen

    def button_price_click(self):
        preis_wert = self.entry_price.get()
        print("Preis:", preis_wert)

        self.hide_all_frames()
        self.frame_price.pack()

    def hide_all_frames(self):
        self.frame_typ.pack_forget()
        self.frame_category.pack_forget()
        self.frame_price.pack_forget()

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
        self.typ = wert
        print("Typ ausgewählt:", wert)

    def set_category(self, wert):
        self.category = wert
        print("Kategorie ausgewählt:", wert)


    def set_hobbies(self, wert):
        self.category = wert
        print("Hobby ausgewählt:", wert)

    def set_food(self, wert):
        self.category = wert
        print("Essen ausgewählt:", wert)

    def set_price_value(self, wert):
        self.price = wert
        print("Preiswert ausgewählt:", wert)

    #alles speichern
    def save_entry(self):
        self.price = self.entry_price.get()

        input_value = f"{self.typ} {self.category} {self.price}"
        print("Gespeichert",input_value)

        self.listbox.insert(tkinter.END, input_value)

#starten
root=tkinter.Tk()    #Tk-Klasse aufrufen und hauptfenster erstellen
tracker = budget_tracker(root)              # ruft die klasse auf und erstellt knöpfe etc
root.mainloop()     #starten schleife