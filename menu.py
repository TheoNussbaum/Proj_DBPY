'''
Auteur : Nussbaum Théo
Date : 15.12.2023
Version : 0.2
'''

# Importation des modules
import tkinter as tk
from tkinter import ttk
from Login import *
from singon import *
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

    # Création de labels, d'entrées et de boutons pour l'interface utilisateur
    tk.Label(window_result, text="TRAINING : AFFICHAGE", font=("Arial", 15)).grid(row=0, column=0, padx=400, pady=10)

    tk.Label(frame_entry_result, text='Pseudo:', font=("Arial", 10)).grid(row=1, column=0, padx=40, pady=5)
    entry_pseudo = tk.Entry(frame_entry_result, font=("Arial", 10))
    entry_pseudo.grid(row=1, column=1)

    tk.Label(frame_entry_result, text='Exercice:', font=("Arial", 10)).grid(row=1, column=2, padx=40, pady=5)
    entry_ex = tk.Entry(frame_entry_result, font=("Arial", 10))
    entry_ex.grid(row=1, column=3)

    tk.Label(frame_entry_result, text='Date début:', font=("Arial", 10)).grid(row=1, column=4, padx=40, pady=5)
    entry_date_s = tk.Entry(frame_entry_result, font=("Arial", 10))
    entry_date_s.grid(row=1, column=5)

    tk.Label(frame_entry_result, text='Date fin:', font=("Arial", 10)).grid(row=1, column=6, padx=40, pady=5)
    entry_date_e = tk.Entry(frame_entry_result, font=("Arial", 10))
    entry_date_e.grid(row=1, column=7)

    btn_resut = tk.Button(frame_entry_result, text="Voir résultats", font=("Arial", 10))
    btn_resut.grid()
    btn_resut.bind("<Button-1>", lambda e: display_tuple_in_table((title + display_table_result()), (title_average + display_table_average())))

    btn_create = tk.Button(frame_entry_result,text="+", font=("Arial", 10))
    btn_create.grid(row=2, column=7, sticky="E")

    tk.Label(frame_menu,text="ID :", font=("Arial", 10)).grid(row=0, column=0)
    entry_id = tk.Entry(frame_menu)
    entry_id.grid(row=0, column=1)

    btn_edit = tk.Button(frame_menu,text="Modifier", font=("Arial", 10))
    btn_edit.grid(row=0, column=2)

    btn_del = tk.Button(frame_menu,text="Supprimer", font=("Arial", 10))
    btn_del.grid(row=0, column=3)

    # Fonction pour afficher les résultats et les moyennes dans des tableaux
    def display_tuple_in_table(results_tuple, average_tuple):
        # Boucle à travers les tuples et création des lablels pour afficher les données dans les frames spécifiés
        for line in range(0, len(results_tuple)):
            for col in range(0, len(results_tuple[line])):
                # Création des labels pour les résultats
                lbl_results = tk.Label(frame_result, text=results_tuple[line][col], width=15, font=("Arial", 10))
                lbl_results.grid(row=line, column=col, pady=1, sticky="w")


        # Attribution des couleurs en fonction des pourcentages de réussite
            if line > 0:  # Exclude the first row
                width_lbl = round(results_tuple[line][7] / 6.5)
                width_colors = ""
                if results_tuple[line][7] <= 25:
                    width_colors = "red"
                elif results_tuple[line][7] >= 26 and results_tuple[line][7] <= 75:
                    width_colors = "yellow"
                elif results_tuple[line][7] > 75:
                    width_colors = "green"
                lbl_results.config(text="", bg=width_colors, width=width_lbl)


        # Boucle pour afficher les moyennes dans des labels et appliquer les bonnes couleurs
        for line in range(0, len(average_tuple)):
            for col in range(0, len(average_tuple[line])):
                lbl_average = tk.Label(frame_total, text=average_tuple[line][col], width=15, font=("Arial", 10))
                lbl_average.grid(row=line, column=col, padx=2, pady=2, sticky="w")

            # Attribution des couleurs en fonction des pourcentages de réussite
            if line > 0:  # Exclude the first row
                width_lbl = round(average_tuple[line][4] / 6.5)
                width_colors = ""
                if average_tuple[line][4] <= 25:
                    width_colors = "red"
                elif average_tuple[line][4] >= 26 and average_tuple[line][4] <= 75:
                    width_colors = "yellow"
                elif average_tuple[line][4] > 75:
                    width_colors = "green"
                lbl_average.config(text="", bg=width_colors, width=width_lbl)

    # Fonction pour supprimer une ligne
    def delete(event):
        delete_from_id(entry_id.get())

        for widget in frame_total.winfo_children():
            widget.destroy()

        for widget in frame_result.winfo_children():
            widget.destroy()

        display_tuple_in_table(title + display_table_result(), title_average + display_table_average())

    # Fonction pour crée une autre fenêtre
    def window_edit(event):
        # Crée une nouvelle fenêtre
        global window_edit
        window_edit = tk.Tk()
        window_edit.title("Modification")  # Définit le titre de la fenêtre
        window_edit.geometry("500x400")  # Définit la taille de la fenêtre
        window_edit.maxsize(500, 400)  # Définit la taille maximale de la fenêtre
        window_edit.minsize(500, 400)  # Définit la taille minimale de la fenêtre

        # Définition de la couleur en utilisant les valeurs RGB et en la convertissant en code hexadécimal
        rgb_color = (139, 201, 194)
        hex_color = '#%02x%02x%02x' % rgb_color  # Convertit les valeurs RGB en hexadécimal
        window_edit.configure(bg=hex_color)  # Applique la couleur d'arrière-plan à la fenêtre

        # Crée un cadre dans la fenêtre principale
        frame_edit_title = tk.Frame(window_edit)
        frame_edit_title.grid(row=0, column=0)

        # Ajoute des labels et des champs de saisie dans la fenêtre
        tk.Label(window_edit, text="TRAINING : MODIFICATION", font=("Arial", 15)).grid(row=0, column=0, padx=130,
                                                                                       pady=10)
        tk.Label(window_edit, text="Temps", font=("Arial", 10)).grid()
        entry_temps = tk.Entry(window_edit)
        entry_temps.grid()
        tk.Label(window_edit, text="nb OK", font=("Arial", 10)).grid()
        entry_ok = tk.Entry(window_edit)
        entry_ok.grid()
        tk.Label(window_edit, text="nb Total", font=("Arial", 10)).grid()
        entry_total = tk.Entry(window_edit)
        entry_total.grid()

        # Ajoute un bouton "Terminer" dans la fenêtre
        btn_edit1 = tk.Button(window_edit, text="Terminer")
        btn_edit1.grid()
        btn_edit1.bind("<Button-1>", lambda e: edit_row())  # Lie l'événement de clic du bouton à la fonction edit_row()

        def edit_row():
            percentage_successful = 100 * (int(entry_ok.get()) / int(entry_total.get()))

            for widget in frame_total.winfo_children():
                widget.destroy()

            for widget in frame_result.winfo_children():
                widget.destroy()

            # Appelle la fonction edit_result() avec les valeurs saisies dans les champs de saisie
            edit_result(entry_temps.get(), entry_ok.get(), entry_total.get(), percentage_successful, entry_id.get())
            # Affiche le résultat dans une table en appelant les fonctions display_table_result() et display_table_average()
            display_tuple_in_table(title + display_table_result(), title_average + display_table_average())
            window_edit.destroy()  # Ferme la fenêtre d'édition après l'édition

    def window_create(event):
        # Crée une nouvelle fenêtre
        window_create = tk.Tk()
        window_create.title("Création")  # Définit le titre de la fenêtre
        window_create.geometry("500x400")  # Définit la taille de la fenêtre
        window_create.maxsize(500, 400)  # Définit la taille maximale de la fenêtre
        window_create.minsize(500, 400)  # Définit la taille minimale de la fenêtre

        # Définition de la couleur en utilisant les valeurs RGB et en la convertissant en code hexadécimal
        rgb_color = (139, 201, 194)
        hex_color = '#%02x%02x%02x' % rgb_color  # Convertit les valeurs RGB en hexadécimal
        window_create.configure(bg=hex_color)  # Applique la couleur d'arrière-plan à la fenêtre

        frame_edit_title = tk.Frame(window_create)
        frame_edit_title.grid(row=0, column=0)

        # Ajoute des labels et des champs de saisie dans la fenêtre
        tk.Label(window_create, text="TRAINING : CRÉATION", font=("Arial", 15)).grid(row=0, column=0, padx=140, pady=10)
        tk.Label(window_create, text="Pseudo", font=("Arial", 10)).grid()
        entry_pseudo_create = tk.Entry(window_create)
        entry_pseudo_create.grid()

        tk.Label(window_create, text="Date heur", font=("Arial", 10)).grid()
        entry_date_create = tk.Entry(window_create)
        entry_date_create.grid()

        tk.Label(window_create, text="Temps", font=("Arial", 10)).grid()
        entry_temps_create = tk.Entry(window_create)
        entry_temps_create.grid()

        tk.Label(window_create, text="Exercice", font=("Arial", 10)).grid()
        entry_exercice_create = tk.ttk.Combobox(window_create, values=["GEO1", "INFO2", "INFO5"])
        entry_exercice_create.grid()

        tk.Label(window_create, text="nb OK", font=("Arial", 10)).grid()
        entry_ok_create = tk.Entry(window_create)
        entry_ok_create.grid()

        tk.Label(window_create, text="nb Total", font=("Arial", 10)).grid()
        entry_total_create = tk.Entry(window_create)
        entry_total_create.grid()

        # Ajoute un bouton "Terminer" dans la fenêtre
        btn_create1 = tk.Button(window_create, text="Terminer")
        btn_create1.grid()
        btn_create1.bind("<Button-1>",lambda e: insert_row())  # Lie l'événement de clic du bouton à la fonction insert_row()

        def insert_row():
            percentage_successful = 100 * (int(entry_ok_create.get()) / int(entry_total_create.get()))
            # Appelle la fonction insert_from_id() avec les valeurs saisies dans les champs de saisie
            insert_from_id(entry_pseudo_create.get(), entry_date_create.get(), entry_temps_create.get(),entry_exercice_create.get(), entry_ok_create.get(), entry_total_create.get(),percentage_successful)
            # Affiche le résultat dans une table en appelant les fonctions display_table_result() et display_table_average()
            display_tuple_in_table(title + display_table_result(), title_average + display_table_average())
            window_create.destroy()  # Ferme la fenêtre de création après l'insertion

    # Bind les boutons pour ouvrire une nouvelle fenêtre
    btn_del.bind("<Button-1>", lambda e: delete(e))
    btn_edit.bind("<Button-1>", lambda e: window_edit(e))
    btn_create.bind("<Button-1>", lambda e: window_create(e))

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

# labels createion and positioning
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

btn_login = tk.Button(window, text="Login", font=("Arial", 15))
btn_login.grid(row=0, column=3, padx=2)
btn_login.bind("<Button-1>",lambda e: window_log())

btn_register = tk.Button(window, text="Sing On", font=("Arial", 15))
btn_register.grid(row=0, column=2, sticky="E")
btn_register.bind("<Button-1>",lambda e: window_sing())

btn_finish = tk.Button(window, text="Quitter", font=("Arial", 15))
btn_finish.grid(row=2+ 2*len(a_exercise)//3 , column=1)
btn_finish.bind("<Button-1>", quit)


# main loop
window.mainloop()
