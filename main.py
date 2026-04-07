#budget tracker gui

import tkinter
import sqlite3
import tkinter.messagebox as mb                # gui popups info, warnung, fehler anzeigen

#knöpfe mit oop
class budget_tracker:
    def __init__(self,root):
        #verbindung datenbank
        self.conn = sqlite3.connect("budget.db")
        self.c = self.conn.cursor()

        # Tabelle erstellen, falls noch nicht vorhanden
        self.c.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            typ TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
        """)                                    #real, gespeichert werden kan
        self.conn.commit()
        self.root = root
        self.root.title("Budget Tracker")
        self.root.geometry("600x450")         # größe fenster

        #variablen für liste(zwischenspeichern)
        self.typ = ""
        self.category = ""
        self.price = ""

        # fenster erstellen/öffnen
        # Eingabe für Typ
        self.frame_typ_row = tkinter.Frame(root)
        self.frame_typ_row.pack(anchor="center")                            #grid = nebeneinander #row= zeile
        self.entry_typ = tkinter.Entry(self.frame_typ_row)                  #column = spalte
        self.entry_typ.grid(row=0, column=0, padx=5, pady=5)                #padx = horizontaler Abstand (links + rechts)
                                                                            #pady = vertikaler Abstand (oben + unten)
        # Eingabe für Kategorie
        self.frame_category_row = tkinter.Frame(root)
        self.frame_category_row.pack(anchor="center")                       #anchor = alles im frame nach w, e, center ausrichten
        self.entry_category = tkinter.Entry(self.frame_category_row)        #center =mittig w=alles links e=alles rechts
        self.entry_category.grid(row=0, column=0, padx=5, pady=5)

        # Eingabe für Preis
        self.frame_price_row = tkinter.Frame(root)
        self.frame_price_row.pack(anchor="center")
        self.entry_price = tkinter.Entry(self.frame_price_row)
        self.entry_price.grid(row=0, column=0, padx=5, pady=5)

        #liste
        self.listbox = tkinter.Listbox(root, width=60 ,height=10)  #zeigt alle Einträge, liste im fenster #width=Breite  #height=sichtbare zeilen
        self.listbox.pack()

        #unterunterklassen
        self.frame_subcategory_row = tkinter.Frame(root)
        self.frame_subcategory_row.pack(anchor="center")
        self.entry_subcategory = tkinter.Entry(self.frame_subcategory_row)
        self.entry_subcategory.grid(row=0, column=0, padx=5, pady=5)

        # erstellen knöpfe
        self.button = tkinter.Button(self.frame_typ_row, text="Typ", command=self.button_typ_click)
        self.button.grid(row=0, column=1, padx=5, pady=5)

        self.button_category = tkinter.Button(self.frame_category_row, text="Category",command=self.button_category_click)
        self.button_category.grid(row=0, column=1, padx=5, pady=5)

        self.button_price = tkinter.Button(self.frame_price_row, text="Preis", command=self.button_price_click)
        self.button_price.grid(row=0, column=1, padx=5, pady=5)

        #speichern
        self.button_save = tkinter.Button(root, text="Speichern", command=self.save_entry)  #speichert alles
        self.button_save.pack()

        #laden
        self.button_load = tkinter.Button(root, text="Laden", command=self.load_all_entries)
        self.button_load.pack()

        #löschen
        self.button_delete_all = tkinter.Button(root, text="Alles löschen", command=self.delete_all_entries)
        self.button_delete_all.pack()

        #einzelen Eintrag löschen
        self.button_delete_selected_entry = tkinter.Button(root,text="Eintrag Löschen",command=self.delete_selected_entry)
        self.button_delete_selected_entry.pack()

        #rechnungsknopf
        self.button_total = tkinter.Button(root, text="Summe anzeigen", command=self.calculate_total)
        self.button_total.pack()

        #ergebnis in gui anzeigen
        self.total_label = tkinter.Label(root, text="Kontostand: 0")
        self.total_label.pack()


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

        #unterunterklassen
        self.button_subcategory = tkinter.Button(self.frame_subcategory_row, text="Unterunterkategorie",command=self.set_subcategory)
        self.button_subcategory.grid(row=0, column=1, padx=5, pady=5)

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

    def load_entry(self):
        selection = self.listbox.curselection()

        if selection:
            content = self.listbox.get(selection[0])           # curselection= gibt zurück, welcher Eintrag angeklickt wurde in liste
            typ, category, price = content.split(" ")          #text in einzelne werte trennen das ich die variablen benutzen kan

            #löschen alte werte
            self.entry_typ.delete(0, tkinter.END)
            self.entry_category.delete(0, tkinter.END)
            self.entry_price.delete(0, tkinter.END)

            #neue werte benutzen
            self.entry_typ.insert(0, typ)
            self.entry_category.insert(0, category)
            self.entry_price.insert(0, price)

            #variablen für aktualisierung
            self.typ = typ
            self.category = category
            self.price = price

    def set_subcategory(self):
        self.subcategory = self.entry_subcategory.get()
        print("Unterkategorie ausgewählt:", self.subcategory)

    #löschen
    def delete_all_entries(self):
        self.c.execute("DELETE FROM entries")
        self.conn.commit()
        self.listbox.delete(0, tkinter.END)
        print("Alle Einträge gelöscht")

    #berechnung der Gesamtsumme (Einnahmen-Ausgaben)
    def calculate_total(self):
        self.c.execute("SELECT typ, price FROM entries")
        rows = self.c.fetchall()

        income = 0
        expense = 0

        for typ, price in rows:
            if typ == "Einnahme":
                income += price
            elif typ == "Ausgabe":
                expense += price

        total = income - expense

        self.total_label.config(text=f"Einnahmen: {income} | Ausgaben: {expense} | Kontostand: {total}")      #config = ändern was schon existiert

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

    #unterklassen für button clicks+anzeige durch print
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

        if not self.price:
            mb.showerror("Fehler", "Bitte Preis eingeben!")
            return

        subcategory = self.entry_subcategory.get()
        full_category = f"{self.category} {subcategory}".strip()

        #in datenbank einfügen
        self.c.execute("INSERT INTO entries (typ, category , price) VALUES (?, ?, ?)",
            (self.typ, full_category, self.price))
        self.conn.commit()
        self.load_all_entries()

        mb.showinfo("Gespeichert", "Eintrag wurde gespeichert")

    #alle Einträge in Listbox laden
    def load_all_entries(self):
        self.listbox.delete(0, tkinter.END)  # alte Einträge entfernen
        self.c.execute("SELECT id, typ,  category, price FROM entries")  # alle Daten aus Datenbank holen
        rows = self.c.fetchall()
        for row in rows:
            id, typ, category, price = row
            display_text = f"{id} | {typ} | {category} | {price}"
            self.listbox.insert(tkinter.END, display_text)

    #ausgewählten eintrag löschen
    def delete_selected_entry(self):
        selection = self.listbox.curselection()
        if selection:
            content = self.listbox.get(selection[0])
            entry_id =content.split(" | ")[0]

            self.c.execute("DELETE FROM entries WHERE id=?", (entry_id,))
            self.conn.commit()

            self.load_all_entries()
            mb.showinfo("Erfolg", f"Eintrag {entry_id} wurde gelöscht")  # Popup
        else:
            mb.showwarning("Achtung", "Bitte wähle einen Eintrag aus!")  # Popup

#starten
root=tkinter.Tk()    #Tk-Klasse aufrufen und hauptfenster erstellen
tracker = budget_tracker(root)              # ruft die klasse auf und erstellt knöpfe etc
root.mainloop()     #starten schleife