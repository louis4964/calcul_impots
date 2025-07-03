import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

def impots(adult_parts, E, e, R, Pension, verbose=True):
    
    def fiscalité(quotient):
        if quotient < 11497:
            return 0
        elif 11498 <= quotient < 29315:
            return 0.11 * (quotient - 11498)
        elif 29316 <= quotient < 83823:
            return 0.11 * 17817 + 0.3 * (quotient - 29316)
        elif 83824 <= quotient < 180293:
            return 0.11 * 17817 + 0.3 * 54507 + 0.4 * (quotient - 83824)
        else:
            return 0.11 * 17817 + 0.3 * 54507 + 0.4 * 96469 + 0.45 * (quotient - 180294)
    
    # Calcul des parts fiscales
    if e < 3:
        Parts = adult_parts + 0.5 * e
    else:
        Parts = adult_parts + 0.5 * (e - 1) + 1
    
    # Vérification des pensions
    if E > 0:
        if Pension > 6674 * E:
            raise ValueError("Pension trop élevée : maximum autorisé = 6 674 € par étudiant.")
        R_fiscal = R - Pension
    else:
        R_fiscal = R

    # Calculs
    quotient_f = R_fiscal / Parts
    impots_avec_qf = fiscalité(quotient_f) * Parts
    quotient_sans_qf = R / Parts
    impots_sans_qf = fiscalité(quotient_sans_qf) * Parts

    reduction_max = e * 1759
    gain_qf = impots_sans_qf - impots_avec_qf

    if gain_qf > reduction_max:
        impots_final = impots_sans_qf - reduction_max
        msg = f"Réduction QF plafonnée à {reduction_max} €."
    else:
        impots_final = impots_avec_qf
        if e == 0:
            msg = "Pas de réduction liée au quotient familial : aucun enfant à charge."
        else:
            msg = f"Réduction QF appliquée : {gain_qf:.2f} €."

    revenu_net = R - impots_final
    revenu_mensuel = revenu_net / 12

    if verbose:
        print("="*30)
        print(f"Vos impôts s'élèveront à {round(impots_final,2)} € cette année.")
        print(f"Soit un revenu après impôts de {round(revenu_net,2)} € soit {round(revenu_mensuel,2)} € par mois.")
        print(msg)
        print("="*30)

    return [impots_final, revenu_net, revenu_mensuel]

class Page3(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Titre
        tk.Label(self, text="Bienvenue sur la page de calcul d'impôt et d'emprunt",
                 justify="left", font=("Arial", 16, "bold")).pack(anchor="w", padx=5, pady=10)

        # Frame principale qui contient les deux colonnes
        main_frame = tk.Frame(self)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Frame gauche : entrées et bouton
        left_frame = tk.Frame(main_frame)
        left_frame.pack(side="left", anchor="n", padx=10)

        self.adult_parts = self._create_entry(left_frame, "Nombre d'adulte(s)", "2", 1, 0)
        self.E = self._create_entry(left_frame, "Nombre d'étudiant ", "0", 1, 1)
        self.e = self._create_entry(left_frame, "Nombre d'enfant", "2", 3, 0)
        self.R = self._create_entry(left_frame, "Revenus imposable", "40000", 3, 1)
        self.Pension = self._create_entry(left_frame, "Montant de la pension annuel de l'étudiant \n(< 6674 par étudiant)", "2400", 5, 0)

        # Bouton + résultat
        tk.Button(left_frame, text="Lancer la simulation", command=self.simulate).grid(row=7, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(left_frame, text="", fg="blue", wraplength=300)
        self.result_label.grid(row=8, column=0, columnspan=2, pady=10)

        # Frame droite : description
        right_frame = tk.Frame(main_frame)
        right_frame.pack(side="right", anchor="n", padx=20)

        texte_titre = "Description"
        texte_accueil = """ 
La fonction impôts calcule le montant de l'impôt sur le revenu en France à partir de plusieurs paramètres : 
- le nombre d'adultes (A),
- d'enfants à charge (e),
- un indicateur (E) qui détermine si une pension est versée,
- le revenu annuel brut (R),
- et éventuellement une pension annuelle versée à un enfant étudiant.

1. Le nombre de parts fiscales est calculé selon la composition du foyer.
2. Si une pension est versée, la fonction vérifie qu’elle ne dépasse pas le plafond légal (6 674 € par enfant).
3. Le revenu imposable est divisé par le nombre de parts pour obtenir le quotient familial.
4. L’impôt est ensuite calculé selon le barème progressif officiel.
5. Enfin, le montant de l’impôt, le revenu net annuel et mensuel sont retournés.
"""

        tk.Label(right_frame, text=texte_titre, font=("Arial", 12, "bold"), anchor="w", justify="left").pack(anchor="w")
        tk.Message(right_frame, text=texte_accueil, width=400, justify="left", font=("Arial", 11)).pack(anchor="w")

 
    def _create_entry(self, parent, label_text, default, r, column):
       label = tk.Label(parent, text=label_text, anchor="w", justify="right")
       label.grid(row=r, column=column, sticky="w", padx=10, pady=5)
       entry = tk.Entry(parent)
       entry.insert(0, default)
       entry.grid(row=r + 1, column=column, padx=10, pady=5)
       return entry
   
    def simulate(self):
        try:
            adult_parts = float(self.adult_parts.get())
            E = float(self.E.get())
            e = float(self.e.get())
            R = float(self.R.get())
            Pension = int(self.Pension.get())

            impots_final, net_annuel, net_mensuel = impots(adult_parts, E, e, R, Pension, verbose=True)

            self.result_label.config(
                text=(
                    f"Vos impôts s'élèveront à {round(impots_final, 2)} € cette année.\n"
                    f"Revenu après impôts : {round(net_annuel, 2)} € par an,\n"
                    f"{round(net_mensuel, 2)} € par mois."
                )
            )

        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulateur Financier Polyvalent")
        self.geometry("900x500")
        
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        
        self.frames = {}
        frame = Page3(container, self)
        self.frames[Page3] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(Page3)

    def show_frame(self, page_class):
        """Affiche une page donnée"""
        frame = self.frames[page_class]
        frame.tkraise()

if __name__ == "__main__":
    app = Application()
    app.mainloop()