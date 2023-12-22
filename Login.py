import tkinter as tk
from tkinter import ttk
from singon import *


def window_log():
    window_log = tk.Tk()
    window_log.title("Login")  # Définit le titre de la fenêtre
    window_log.geometry("200x210")  # Définit la taille de la fenêtre
    window_log.resizable(False, False)
    # Définition de la couleur en utilisant les valeurs RGB et en la convertissant en code hexadécimal
    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color  # Convertit les valeurs RGB en hexadécimal
    window_log.configure(bg=hex_color)  # Applique la couleur d'arrière-plan à la fenêtre

    tk.Label(window_log, text="LOGIN", font=("Arial", 15)).grid(row=0, column=0, padx=65, pady=10)

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

    btn_zone = tk.Frame(frame_log)
    btn_zone.grid(row=7, column=0)

    tk.Label(btn_zone,text="Pas de compte ?").grid(row=0, column=0, sticky="W")
    btn_login_to_singon = tk.Button(btn_zone,text="S'inscrire")
    btn_login_to_singon.grid(row=0, column=1, sticky="E")

    def open_sing_on():
        window_log.destroy()
        window_sing()

    btn_login_to_singon.bind("<Button-1>", lambda e: open_sing_on())