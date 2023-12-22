from tkinter import *


window_display = Tk()
window_display.title("Affichage score")
window_display.geometry("1100x900")
#  variable
#  Affiche le nom des colonnes au dessus de la liste des résultats.
results_name = [("Élève", "Date Début", "Temps", "Exercice", "Nombre OK", "Nombre Total", "Pourcentage Réussi")]
#  Affiche le nom des colonnes au dessus de la liste de la moyenne.
average_name = [("NbLignes", "Temps Total", "Nb OK", "Nb Total", "% Total")]
# color définition
rgb_color = (139, 201, 194)
hex_color = '#%02x%02x%02x' % rgb_color  # translation in hexa
window_display.configure(bg=hex_color)
window_display.grid_columnconfigure(0, weight=1)
# Frame 1
frame_1 = Frame(window_display, bg=hex_color)
frame_1.grid(row=0, column=0)

#  Affiche le titre de la table.
lbl_title_display = Label(frame_1, text="TRAINING : AFFICHAGE", font=("Arial", 15))
lbl_title_display.grid(row=0, column=0, padx=400, pady=10)



window_display.mainloop()

