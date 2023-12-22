import tkinter as tk
from tkinter import ttk


def window_log():
    window_log = tk.Tk()
    window_log.title("Login")  # Définit le titre de la fenêtre
    window_log.geometry("500x400")  # Définit la taille de la fenêtre
    window_log.maxsize(500, 400)  # Définit la taille maximale de la fenêtre
    window_log.minsize(500, 400)  # Définit la taille minimale de la fenêtr
    # Définition de la couleur en utilisant les valeurs RGB et en la convertissant en code hexadécimal
    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color  # Convertit les valeurs RGB en hexadécimal
    window_log.configure(bg=hex_color)  # Applique la couleur d'arrière-plan à la fenêtre

    tk.Label(window_log, text="TRAINING : LOGIN", font=("Arial", 15)).grid(row=0, column=0, padx=140, pady=10)

    frame_log = tk.Frame(window_log)
    frame_log.grid()

    tk.Label(frame_log, text="Nom d'utilisateur").grid(sticky="W")
    entry_user = tk.Entry(frame_log)
    entry_user.grid()

    tk.Label(frame_log, text="Mot de passe").grid(sticky="W")
    entry_password = tk.Entry(frame_log)
    entry_password.grid()

    btn_to_login = tk.Button(frame_log, text="Se connecter", width=12)
    btn_to_login.grid(pady=5)

    tk.Label(frame_log,text="Pas de compte ?").grid()
    btn_login_to_singon = tk.Button(frame_log,text="S'inscrire")
    btn_login_to_singon.grid()