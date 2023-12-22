import tkinter as tk
from tkinter import ttk
import Login

def window_sing():
    window_sing = tk.Tk()
    window_sing.title("Sing On")  # Définit le titre de la fenêtre
    window_sing.geometry("215x330")  # Définit la taille de la fenêtre

    # Définition de la couleur en utilisant les valeurs RGB et en la convertissant en code hexadécimal
    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color  # Convertit les valeurs RGB en hexadécimal
    window_sing.configure(bg=hex_color)  # Applique la couleur d'arrière-plan à la fenêtre

    tk.Label(window_sing, text="SING UP", font=("Arial", 15)).grid(row=0, column=0, padx=65, pady=10)

    frame_sing = tk.Frame(window_sing)
    frame_sing.grid()

    tk.Label(frame_sing, text="Nom").grid(sticky="W", padx=13)
    entry_name = tk.Entry(frame_sing)
    entry_name.grid()

    tk.Label(frame_sing, text="Prenom").grid(sticky="W", padx=13)
    entry_last_name = tk.Entry(frame_sing)
    entry_last_name.grid()

    tk.Label(frame_sing, text="Pseudo").grid(sticky="W", padx=13)
    entry_ps = tk.Entry(frame_sing)
    entry_ps.grid()

    tk.Label(frame_sing, text="Mot de passe").grid(sticky="W", padx=13)
    entry_mdp = tk.Entry(frame_sing)
    entry_mdp.grid()

    tk.Label(frame_sing, text="Confirme mot de passe").grid(sticky="W", padx=13)
    entry_cmdp = tk.Entry(frame_sing)
    entry_cmdp.grid()

    btn_to_login = tk.Button(frame_sing, text="S'inscrire", width=12)
    btn_to_login.grid(pady=5)

    btn_zone = tk.Frame(frame_sing)
    btn_zone.grid(row=11, column=0)

    tk.Label(btn_zone,text="Déjà un compte ?").grid(row=0, column=0, sticky="W")
    btn_singon_to_login = tk.Button(btn_zone,text="Se connecter")
    btn_singon_to_login.grid(row=0, column=1, sticky="E")

    def open_login():
        window_sing.destroy()
        Login.window_log()

    btn_singon_to_login.bind("<Button-1>", lambda e: open_login())