import tkinter as tk
from tkinter import ttk

def window_sing():
    window_create = tk.Tk()
    window_create.title("Sing On")  # Définit le titre de la fenêtre
    window_create.geometry("500x400")  # Définit la taille de la fenêtre
    window_create.maxsize(500, 400)  # Définit la taille maximale de la fenêtre
    window_create.minsize(500, 400)  # Définit la taille minimale de la fenêtr

    # Définition de la couleur en utilisant les valeurs RGB et en la convertissant en code hexadécimal
    rgb_color = (139, 201, 194)
    hex_color = '#%02x%02x%02x' % rgb_color  # Convertit les valeurs RGB en hexadécimal
    window_create.configure(bg=hex_color)  # Applique la couleur d'arrière-plan à la fenêtre


