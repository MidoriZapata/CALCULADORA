# utils.py
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
import csv

def mostrar_histograma(app, numeros, titulo):
    fig, ax = plt.subplots(figsize=(4,3))
    ax.hist(numeros, bins=10, edgecolor="black")
    ax.set_title(f"Histograma - {titulo}")
    canvas = FigureCanvasTkAgg(fig, master=app)
    canvas.draw()
    canvas.get_tk_widget().pack()

def export_csv(numeros):
    ruta = filedialog.asksaveasfilename(defaultextension=".csv",
                                        filetypes=[("CSV files","*.csv")])
    if ruta:
        with open(ruta, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Indice", "Numero"])
            for i, num in enumerate(numeros):
                writer.writerow([i+1, num])
