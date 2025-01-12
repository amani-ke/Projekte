import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.root.configure(bg="lightblue")  
        self.spieler_symbol = "X"
        self.system_symbol = "O"
        self.aktueller_spieler = self.spieler_symbol

        self.spielfeld = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.erstelle_gui()

    def erstelle_gui(self):
        for zeile in range(3):
            for spalte in range(3):
                button = tk.Button(
                    self.root,
                    text="",
                    font=("Arial", 24),
                    width=5,
                    height=2,
                    bg="lightgray", 
                    command=lambda z=zeile, s=spalte: self.benutzer_zug(z, s)
                )
                button.grid(row=zeile, column=spalte)
                self.buttons[zeile][spalte] = button

        # "Spiel beenden" oder "Nochmal spielen"
        self.neues_spiel_button = tk.Button(self.root, text="Nochmal spielen", font=("Arial", 14), command=self.neues_spiel)
        self.neues_spiel_button.grid(row=3, column=0, columnspan=3, pady=10)
        self.neues_spiel_button.config(state="disabled")  

    def benutzer_zug(self, zeile, spalte):
        if self.spielfeld[zeile][spalte] == " ":
            self.spielfeld[zeile][spalte] = self.spieler_symbol
            self.buttons[zeile][spalte].config(text=self.spieler_symbol, state="disabled", fg="blue", bg="lightblue")
            if self.sieg_prüfen(self.spieler_symbol):
                self.spiel_ende("Herzlichen Glückwunsch! Du hast gewonnen!", "lightgreen")
                return
            if self.unentschieden_prüfen():
                self.spiel_ende("Unentschieden! Das Spielfeld ist voll.", "lightyellow")
                return
            self.system_zug()
        else:
            messagebox.showwarning("Ungültiger Zug", "Dieses Feld ist bereits belegt.")

    def system_zug(self):
        freie_felder = [(z, s) for z in range(3) for s in range(3) if self.spielfeld[z][s] == " "]
        if freie_felder:
            zeile, spalte = freie_felder[0]  
            self.spielfeld[zeile][spalte] = self.system_symbol
            self.buttons[zeile][spalte].config(text=self.system_symbol, state="disabled", fg="red", bg="lightcoral")
            if self.sieg_prüfen(self.system_symbol):
                self.spiel_ende("Das System hat gewonnen! Versuch's nochmal.", "lightcoral")
                return
            if self.unentschieden_prüfen():
                self.spiel_ende("Unentschieden! Das Spielfeld ist voll.", "lightyellow")

    def sieg_prüfen(self, spieler):
        for i in range(3):
            if all(self.spielfeld[i][j] == spieler for j in range(3)) or \
               all(self.spielfeld[j][i] == spieler for j in range(3)):
                return True
        if all(self.spielfeld[i][i] == spieler for i in range(3)) or \
           all(self.spielfeld[i][2 - i] == spieler for i in range(3)):
            return True
        return False

    def unentschieden_prüfen(self):
        return all(self.spielfeld[z][s] != " " for z in range(3) for s in range(3))

    def spiel_ende(self, nachricht, farbe):
        messagebox.showinfo("Spielende", nachricht)
        self.root.configure(bg=farbe)  
        for zeile in range(3):
            for spalte in range(3):
                self.buttons[zeile][spalte].config(state="disabled") 
        self.neues_spiel_button.config(state="normal")  

    def neues_spiel(self):
        self.spielfeld = [[" " for _ in range(3)] for _ in range(3)]
        for zeile in range(3):
            for spalte in range(3):
                self.buttons[zeile][spalte].config(text="", state="normal", bg="lightgray")
        
        self.root.configure(bg="lightblue")  
        self.neues_spiel_button.config(state="disabled")  
        self.aktueller_spieler = self.spieler_symbol  
        self.spielfeld[1][1] = " " 

# Hauptprogramm
if __name__ == "__main__":
    root = tk.Tk()
    spiel = TicTacToe(root)
    root.mainloop()
