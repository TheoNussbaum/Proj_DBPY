'''
Auteur : Nussbaum Théo
Date : 15.12.2023
Version : 0.2
'''

import tkinter as tk
from database import *
import geo01
import info02
import info05

# exercises array
a_exercise=["geo01", "info02", "info05"]
albl_image=[None, None, None] # label (with images) array
a_image=[None, None, None] # images array
a_title=[None, None, None] # array of title (ex: GEO01)

dict_games = {"geo01": geo01.open_window_geo_01, "info02": info02.open_window_info_02, "info05": info05.open_window_info_05}

# call other windows (exercices)
def exercise(event,exer):
    dict_games[exer](window)


# Cette fonction crée une interface graphique pour afficher les résultats du programme de braintraining.
def display_result(event):
    # Création de la fenêtre principale
    window_result = tk.Tk()
    window_result.title("Affichage braintraining")  # Titre de la fenêtre
    window_result.geometry("1175x900")  # Définition de la taille de la fenêtre

    # Titres pour les colonnes de données
    title = [("ID", "Elève", "Date heure", "Temps", "Exercice", "nb OK", "nb Total", "% réussi")]
    title_average = [("NbLignes", "Temps total", "Nb OK", "Nb Total", "% Total")]

    # Définition de la couleur de fond
    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color  # Conversion en hexadécimal
    window_result.configure(bg=hex_color)  # Application de la couleur de fond
    window_result.grid_columnconfigure(0, weight=1)

    # Division de la fenêtre en différentes frames pour organiser les éléments
    fram_title = tk.Frame(window_result)
    fram_title.grid(row=0, column=0)
    frame_entry_result = tk.Frame(window_result)
    frame_entry_result.grid(row=1, column=0)
    frame_result = tk.Frame(window_result, width=15)
    frame_result.grid(row=2, column=0, pady=20)
    frame_total = tk.Frame(window_result)
    frame_total.grid(row=3, column=0)
    frame_menu = tk.Frame(window_result)
    frame_menu.grid(row=4, column=0, pady=20)

    # Création de label, d'entrées et de boutons pour l'interface utilisateur
    tk.Label(window_result, text="TRAINING : AFFICHAGE", font=("Arial", 15)).grid(row=0, column=0, padx=400, pady=10)

    tk.Label(frame_entry_result, text='Pseudo:', font=("Arial", 10)).grid(row=1, column=0, padx=40, pady=5)
    entry_pseudo = tk.Entry(frame_entry_result, font=("Arial", 10))
    entry_pseudo.grid(row=1, column=1)

    tk.Label(frame_entry_result, text='Exercice:', font=("Arial", 10)).grid(row=1, column=2, padx=40, pady=5)
    entry_pseudo = tk.Entry(frame_entry_result, font=("Arial", 10))
    entry_pseudo.grid(row=1, column=3)

    tk.Label(frame_entry_result, text='Date début:', font=("Arial", 10)).grid(row=1, column=4, padx=40, pady=5)
    entry_pseudo = tk.Entry(frame_entry_result, font=("Arial", 10))
    entry_pseudo.grid(row=1, column=5)

    tk.Label(frame_entry_result, text='Date fin:', font=("Arial", 10)).grid(row=1, column=6, padx=40, pady=5)
    entry_pseudo = tk.Entry(frame_entry_result, font=("Arial", 10))
    entry_pseudo.grid(row=1, column=7)

    btn_resut = tk.Button(frame_entry_result, text="Voir résultats", font=("Arial", 10))
    btn_resut.grid()
    btn_resut.bind("<Button-1>", lambda e: display_tuple_in_table((title + display_table_result()), (title_average + display_table_average())))

    btn_creat = tk.Button(frame_menu,text="Ajouter une ligne", font=("Arial", 10))
    btn_creat.grid(row=0, column=0)

    tk.Label(frame_menu,text="ID :", font=("Arial", 10)).grid(row=0, column=2)
    entry_id = tk.Entry(frame_menu)
    entry_id.grid(row=0, column=3)

    btn_edit = tk.Button(frame_menu,text="Modifier", font=("Arial", 10))
    btn_edit.grid(row=0, column=1)

    btn_del = tk.Button(frame_menu, text="Supprimer", font=("Arial", 10))
    btn_del.grid(row=0, column=4)

    # Fonction pour supprimer une ligne spécifique
    def delete():
        delete_from_id(entry_id.get())  # Supprime la ligne demandée.

        for widget in frame_result.winfo_children():
            widget.destroy()

        display_tuple_in_table(title + display_table_result(), title_average + display_table_average())

    btn_del.bind("<Button-1>", lambda e: delete())

    # Fonction pour afficher les résultats et les moyennes dans des tableaux
    def display_tuple_in_table(results_tuple, average_tuple):
        # Boucle à travers les tuples et création des libellés pour afficher les données dans les cadres spécifiés
        for line in range(0, len(results_tuple)):
            for col in range(0, len(results_tuple[line])):
                # Création des libellés pour les résultats
                lbl_results = tk.Label(frame_result, text=results_tuple[line][col], width=15, font=("Arial", 10))
                lbl_results.grid(row=line, column=col, sticky="w")

        # Attribution des couleurs en fonction des pourcentages de réussite
        if line > 0:  # Exclude the first row
                width_lbl = round(results_tuple[line][6] / 6.5)
                print(width_lbl)
                lbl_results.config(text="")
                if results_tuple[line][6] <= 25:
                    lbl_results.config(bg='red', width=width_lbl)
                elif results_tuple[line][6] >= 26 and results_tuple[line][-1] <= 75:
                    lbl_results.config(bg='yellow', width=width_lbl)
                elif results_tuple[line][6] > 75:
                    lbl_results.config(bg='green', width=width_lbl)

        # Boucle pour afficher les moyennes dans des libellés et appliquer les couleurs en conséquence
        for line in range(0, len(average_tuple)):
            for col in range(0, len(average_tuple[line])):
                lbl_average = tk.Label(frame_total, text=average_tuple[line][col], width=15, font=("Arial", 10))
                lbl_average.grid(row=line, column=col, padx=2, pady=2, sticky="w")

            # Attribution des couleurs en fonction des pourcentages de réussite
            if line > 0:  # Exclude the first row
                width_lbl = round(results_tuple[line][6] / 6.5)
                lbl_average.config(text="")
                if results_tuple[line][6] <= 25:
                    lbl_average.config(bg='red', width=width_lbl)
                elif results_tuple[line][6] >= 26 and results_tuple[line][-1] <= 75:
                    lbl_average.config(bg='yellow', width=width_lbl)
                elif results_tuple[line][6] > 75:
                    lbl_average.config(bg='green', width=width_lbl)

    def window_edit(event):
        window_edit = tk.Tk()
        window_edit.title("Modifier")
        window_edit.geometry("1175x900")

        # color définition
        rgb_color = (139, 201, 194)
        hex_color = '#%02x%02x%02x' % rgb_color  # translation in hexa
        window_edit.configure(bg=hex_color)
        window_edit.grid_columnconfigure(0, weight=1)

        frame_edit_title = tk.Frame(window_edit)
        frame_edit_title.grid(row=0, column=0)

        tk.Label(window_edit, text="TRAINING : MODIFIER", font=("Arial", 15)).grid(row=0, column=0, padx=400, pady=10)

        tk.Label(window_edit, text="ID").grid()
        entry_id1 = tk.Entry(window_edit)
        entry_id1.grid()
        tk.Label(window_edit, text="Temps", font=("Arial", 10)).grid()
        entry_temps = tk.Entry(window_edit)
        entry_temps.grid()
        tk.Label(window_edit, text="nb OK", font=("Arial", 10)).grid()
        entry_ok = tk.Entry(window_edit)
        entry_ok.grid()
        tk.Label(window_edit, text="nb Total", font=("Arial", 10)).grid()
        entry_total = tk.Entry(window_edit)
        entry_total.grid()

        btn_edit1 = tk.Button(window_edit, text="Terminer")
        btn_edit1.grid()
        btn_edit.bind("<Button-1>", lambda e: edit_result(entry_temps.get(), entry_ok.get(), entry_total.get()))



    btn_edit.bind("<Button-1>", lambda e: window_edit(e))
# Main window
window = tk.Tk()
window.title("Training, entrainement cérébral")
window.geometry("1100x900")

# color définition
rgb_color = (139, 201, 194)
hex_color = '#%02x%02x%02x' % rgb_color # translation in hexa
window.configure(bg=hex_color)
window.grid_columnconfigure((0,1,2), minsize=300, weight=1)

# Title création
lbl_title = tk.Label(window, text="TRAINING MENU", font=("Arial", 15))
lbl_title.grid(row=0, column=1,ipady=5, padx=40,pady=40)

# labels creation and positioning
for ex in range(len(a_exercise)):
    a_title[ex]=tk.Label(window, text=a_exercise[ex], font=("Arial", 15))
    a_title[ex].grid(row=1+2*(ex//3),column=ex % 3 , padx=40,pady=10) # 3 label per row

    a_image[ex] = tk.PhotoImage(file="img/" + a_exercise[ex] + ".gif") # image name
    albl_image[ex] = tk.Label(window, image=a_image[ex]) # put image on label
    albl_image[ex].grid(row=2 + 2*(ex // 3), column=ex % 3, padx=40, pady=10) # 3 label per row
    albl_image[ex].bind("<Button-1>", lambda event, ex = ex :exercise(event=None, exer=a_exercise[ex])) #link to others .py
    print(a_exercise[ex])

# Buttons, display results & quit
btn_display = tk.Button(window, text="Display results", font=("Arial", 15))
btn_display.grid(row=1+ 2*len(a_exercise)//3 , column=1)
btn_display.bind("<Button-1>",lambda e: display_result(e))

btn_finish = tk.Button(window, text="Quitter", font=("Arial", 15))
btn_finish.grid(row=2+ 2*len(a_exercise)//3 , column=1)
btn_finish.bind("<Button-1>", quit)

# main loop
window.mainloop()
