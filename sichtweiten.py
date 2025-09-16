import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import numpy as np

# Funktion zur Berechnung der Sichtweite
def berechne_sichtweite(v, t_react, a_brake, t_zug, s_safety):
    """
    v: Geschwindigkeit in km/h
    t_react: Reaktionszeit in s
    a_brake: Bremsverzögerung in m/s²
    t_zug: Zugangszeit in s
    s_safety: Sicherheitszuschlag in m
    """
    v_ms = v / 3.6  # Umrechnung km/h -> m/s
    s_react = v_ms * t_react
    s_brake = (v_ms**2) / (2 * a_brake)
    s_zug = v_ms * t_zug
    s_total = s_react + s_brake + s_zug + s_safety
    return s_total, (s_react, s_brake, s_zug, s_safety)

# Funktion zur Visualisierung
def plot_sichtweite(sichtweite, komponenten):
    labels = ["Reaktionsweg", "Bremsweg", "Zugangszeit", "Sicherheitszuschlag"]
    plt.figure(figsize=(8,5))
    plt.bar(labels, komponenten, color="skyblue")
    plt.axhline(y=sichtweite, color="r", linestyle="--", label=f"Gesamt: {sichtweite:.1f} m")
    plt.ylabel("Distanz (m)")
    plt.title("Sichtweiten-Berechnung")
    plt.legend()
    plt.show()

# Callback für Button
def berechnen():
    try:
        v = float(entry_v.get())
        t_react = float(entry_t_react.get())
        a_brake = float(entry_a_brake.get())
        t_zug = float(entry_t_zug.get())
        s_safety = float(entry_s_safety.get())

        s_total, komponenten = berechne_sichtweite(v, t_react, a_brake, t_zug, s_safety)
        messagebox.showinfo("Ergebnis", f"Benötigte Sichtweite: {s_total:.2f} m")
        plot_sichtweite(s_total, komponenten)

    except ValueError:
        messagebox.showerror("Fehler", "Bitte gültige Zahlen eingeben!")

# GUI erstellen
root = tk.Tk()
root.title("Sichtweiten-Rechner")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0)

ttk.Label(frame, text="Geschwindigkeit (km/h):").grid(row=0, column=0, sticky="w")
entry_v = ttk.Entry(frame)
entry_v.grid(row=0, column=1)

ttk.Label(frame, text="Reaktionszeit (s):").grid(row=1, column=0, sticky="w")
entry_t_react = ttk.Entry(frame)
entry_t_react.grid(row=1, column=1)

ttk.Label(frame, text="Bremsverzögerung (m/s²):").grid(row=2, column=0, sticky="w")
entry_a_brake = ttk.Entry(frame)
entry_a_brake.grid(row=2, column=1)

ttk.Label(frame, text="Zugangszeit (s):").grid(row=3, column=0, sticky="w")
entry_t_zug = ttk.Entry(frame)
entry_t_zug.grid(row=3, column=1)

ttk.Label(frame, text="Sicherheitszuschlag (m):").grid(row=4, column=0, sticky="w")
entry_s_safety = ttk.Entry(frame)
entry_s_safety.grid(row=4, column=1)

ttk.Button(frame, text="Berechnen & Visualisieren", command=berechnen).grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
