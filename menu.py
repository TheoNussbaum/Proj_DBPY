# Training (GEO01)
# TN 24.11.2023
# PRO DB PY

import tkinter as tk
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


#call display_results
def display_result(event):
    window_result = tk.Tk()
    window_result.title("Affichage braintraining")
    window_result.geometry("1175x900")

    # color définition
    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color  # translation in hexa
    window_result.configure(bg=hex_color)

    tk.Label(window_result, text="TRAINING : AFFICHAGE", font=("Arial", 15)).grid(row=0, column=0, ipady=5, padx=40, pady=40)

    frame_entry_result = tk.Frame(window_result)
    frame_entry_result.grid()
    frame_result = tk.Frame(window_result, width=1140, height=500)
    frame_result.grid(pady=20)
    frame_total = tk.Frame(window_result)
    frame_total.grid()

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

    tk.Label(frame_total, text="NbLignes", font=("Arial", 10)).grid(row=1, column=0, padx=40, pady=5)
    tk.Label(frame_total, text="Temps total", font=("Arial", 10)).grid(row=1, column=1, padx=40, pady=5)
    tk.Label(frame_total, text="Nb OK", font=("Arial", 10)).grid(row=1, column=2, padx=40, pady=5)
    tk.Label(frame_total, text="Nb Total", font=("Arial", 10)).grid(row=1, column=3, padx=40, pady=5)
    tk.Label(frame_total, text="% Total", font=("Arial", 10)).grid(row=1, column=4, padx=40, pady=5)


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
