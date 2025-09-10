import tkinter as tk
from tkinter import messagebox, filedialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import csv

# ---------------- Generadores ----------------
class CuadradosMedios:
    def __init__(self, seed, n):
        self.seed = seed
        self.n = n

    def generar(self):
        nums = []
        x = self.seed
        for _ in range(self.n):
            x = int(str(x**2).zfill(8)[2:6])
            nums.append(x/10000)
        return nums

class ProductosMedios:
    def __init__(self, seed1, seed2, n):
        self.x = seed1
        self.y = seed2
        self.n = n

    def generar(self):
        nums = []
        for _ in range(self.n):
            p = str(self.x * self.y).zfill(8)
            self.x, self.y = self.y, int(p[2:6])
            nums.append(self.y/10000)
        return nums

class MultiplicadorConstante:
    def __init__(self, seed, n, a):
        self.x = seed
        self.n = n
        self.a = a

    def generar(self):
        nums = []
        x = self.x
        for _ in range(self.n):
            x = (self.a * x) % 10000
            x_str = str(x).zfill(4)
            medio = int(x_str[0:4])  # tomamos los 4 dígitos (puedes ajustar según tu regla)
            nums.append(medio/10000)
        return nums

# ---------------- Pruebas ----------------
class PruebaMedia:
    def __init__(self, numeros):
        self.numeros = numeros
    def calcular(self):
        n = len(self.numeros)
        media = np.mean(self.numeros)
        z = (media - 0.5) * np.sqrt(12*n)
        return f"Media = {media:.4f}, Z = {z:.4f}"

class PruebaVarianza:
    def __init__(self, numeros):
        self.numeros = numeros
    def calcular(self):
        n = len(self.numeros)
        varianza = np.var(self.numeros)
        chi = (12*n*varianza - n) / np.sqrt(24*n)
        return f"Varianza = {varianza:.4f}, Chi = {chi:.4f}"

class PruebaChi2:
    def __init__(self, numeros, k=10):
        self.numeros = numeros
        self.k = k
    def calcular(self):
        n = len(self.numeros)
        frec, _ = np.histogram(self.numeros, bins=self.k, range=(0,1))
        esperada = n/self.k
        chi2 = np.sum((frec-esperada)**2 / esperada)
        return f"Chi² = {chi2:.4f} con {self.k-1} gl"

# ---------------- Funciones Auxiliares ----------------
def mostrar_histograma(frame, numeros, titulo):
    for widget in frame.winfo_children():
        if isinstance(widget, FigureCanvasTkAgg):
            widget.get_tk_widget().destroy()
    fig, ax = plt.subplots(figsize=(5,3))
    ax.hist(numeros, bins=10, edgecolor="black", color="#2196F3")
    ax.set_title(f"Histograma - {titulo}", fontsize=12, fontweight="bold")
    ax.set_facecolor("#ffffff")
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=5)

def export_csv(numeros):
    ruta = filedialog.asksaveasfilename(defaultextension=".csv",
                                        filetypes=[("CSV files","*.csv")])
    if ruta:
        with open(ruta, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Indice", "Numero"])
            for i, num in enumerate(numeros):
                writer.writerow([i+1, num])
        messagebox.showinfo("Exportar CSV", f"Archivo guardado en:\n{ruta}")

# ---------------- Ventana Multiplicador Constante ----------------
class MultiplicadorConstanteWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("Multiplicador Constante")
        self.geometry("450x350")
        self.configure(bg="#B3E5FC")
        self.numeros = []

        tk.Label(self, text="Semilla:", bg="#B3E5FC", font=("Helvetica", 12)).pack(pady=5)
        self.seed_entry = tk.Entry(self, font=("Helvetica", 12))
        self.seed_entry.pack(pady=5)

        tk.Label(self, text="Constante a (3 o más dígitos):", bg="#B3E5FC", font=("Helvetica", 12)).pack(pady=5)
        self.a_entry = tk.Entry(self, font=("Helvetica", 12))
        self.a_entry.pack(pady=5)

        tk.Label(self, text="Cantidad n:", bg="#B3E5FC", font=("Helvetica", 12)).pack(pady=5)
        self.n_entry = tk.Entry(self, font=("Helvetica", 12))
        self.n_entry.pack(pady=5)

        tk.Button(self, text="Generar", bg="#03A9F4", fg="white", font=("Helvetica", 12, "bold"),
                  command=self.generar).pack(pady=10)
        tk.Button(self, text="Limpiar", bg="#FFC107", fg="black", font=("Helvetica", 12, "bold"),
                  command=self.limpiar).pack(pady=5)
        tk.Button(self, text="Enviar al main", bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"),
                  command=self.enviar_main).pack(pady=5)
        tk.Button(self, text="Cerrar", bg="#F44336", fg="white", font=("Helvetica", 12, "bold"),
                  command=self.destroy).pack(pady=5)

        self.output_text = tk.Text(self, height=8, width=45, font=("Helvetica", 11))
        self.output_text.pack(pady=10)

    def generar(self):
        try:
            seed = int(self.seed_entry.get())
            a = int(self.a_entry.get())
            n = int(self.n_entry.get())
            gen = MultiplicadorConstante(seed, n, a)
            self.numeros = gen.generar()
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"Números generados:\n{self.numeros}")
        except:
            messagebox.showerror("Error", "Ingrese valores válidos")

    def limpiar(self):
        self.seed_entry.delete(0, tk.END)
        self.a_entry.delete(0, tk.END)
        self.n_entry.delete(0, tk.END)
        self.output_text.delete("1.0", tk.END)
        self.numeros = []

    def enviar_main(self):
        if self.numeros:
            self.master.numeros = self.numeros
            self.master.mostrar_resultados("Multiplicador Constante")
            messagebox.showinfo("Enviado", "Números enviados al main para pruebas y exportar.")
        else:
            messagebox.showwarning("Aviso", "Genera los números primero.")

# ---------------- Ventana Principal ----------------
class PRNGDashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PRNG Dashboard - Midori")
        self.geometry("1050x720")
        self.configure(bg="#B3E5FC")
        self.numeros = []

        tk.Label(self, text="CALCULADORA", font=("Helvetica", 20, "bold"),
                 bg="#B3E5FC", fg="#0D47A1").pack(pady=10)

        # Frames
        self.frame_inputs = tk.Frame(self, bg="#81D4FA", padx=20, pady=20, bd=2, relief="groove")
        self.frame_inputs.pack(pady=10, fill="x")

        self.frame_botones = tk.Frame(self, bg="#B3E5FC")
        self.frame_botones.pack(pady=10, fill="x")

        self.frame_resultados = tk.Frame(self, bg="#B3E5FC", height=250)
        self.frame_resultados.pack(pady=10, fill="x")
        self.frame_resultados.pack_propagate(False)

        self.scrollbar = tk.Scrollbar(self.frame_resultados)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.output_text = tk.Text(self.frame_resultados, height=10, font=("Helvetica", 11),
                                   yscrollcommand=self.scrollbar.set)
        self.output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.output_text.yview)

        # Botones finales
        self.frame_final = tk.Frame(self, bg="#B3E5FC")
        self.frame_final.pack(pady=5)
        tk.Button(self.frame_final, text="Exportar CSV", bg="#4CAF50", fg="white",
                  font=("Helvetica", 14, "bold"), width=20, command=self.exportar).grid(row=0, column=0, padx=10)
        tk.Button(self.frame_final, text="Salir", bg="#F44336", fg="white",
                  font=("Helvetica", 14, "bold"), width=20, command=self.destroy).grid(row=0, column=1, padx=10)

        # Entradas
        tk.Label(self.frame_inputs, text="Semilla 1:", bg="#81D4FA", font=("Helvetica", 12)).grid(row=0, column=0, padx=5, pady=5)
        self.seed1_entry = tk.Entry(self.frame_inputs, width=12, font=("Helvetica", 12))
        self.seed1_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_inputs, text="Semilla 2:", bg="#81D4FA", font=("Helvetica", 12)).grid(row=1, column=0, padx=5, pady=5)
        self.seed2_entry = tk.Entry(self.frame_inputs, width=12, font=("Helvetica", 12))
        self.seed2_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame_inputs, text="Cantidad n:", bg="#81D4FA", font=("Helvetica", 12)).grid(row=2, column=0, padx=5, pady=5)
        self.n_entry = tk.Entry(self.frame_inputs, width=12, font=("Helvetica", 12))
        self.n_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botones generadores
        colores_gen = ["#2196F3", "#03A9F4", "#00BCD4"]
        textos_gen = ["Cuadrados Medios", "Productos Medios", "Multiplicador Constante"]
        comandos_gen = [self.run_cuadrados, self.run_productos, self.run_mult]

        for i, (txt, cmd, color) in enumerate(zip(textos_gen, comandos_gen, colores_gen)):
            tk.Button(self.frame_botones, text=txt, bg=color, fg="white",
                      font=("Helvetica", 12, "bold"), width=22, command=cmd).grid(row=0, column=i, padx=10, pady=10)

        # Botones pruebas
        colores_prueba = ["#FF5722", "#FF7043", "#FF9800"]
        textos_prueba = ["Prueba Media", "Prueba Varianza", "Prueba Chi²"]
        comandos_prueba = [self.test_media, self.test_varianza, self.test_chi2]

        for i, (txt, cmd, color) in enumerate(zip(textos_prueba, comandos_prueba, colores_prueba)):
            tk.Button(self.frame_botones, text=txt, bg=color, fg="white",
                      font=("Helvetica", 12, "bold"), width=18, command=cmd).grid(row=1, column=i, padx=10, pady=10)

    # ---------------- Funciones ----------------
    def get_params(self):
        try:
            seed1 = int(self.seed1_entry.get())
            seed2 = int(self.seed2_entry.get() or 0)
            n = int(self.n_entry.get())
            return seed1, seed2, n
        except:
            messagebox.showerror("Error", "Ingrese valores válidos")
            return None, None, None

    def mostrar_resultados(self, metodo):
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, f"{metodo}:\n{self.numeros}\n")
        mostrar_histograma(self.frame_resultados, self.numeros, metodo)

    # ---------------- Generadores ----------------
    def run_cuadrados(self):
        s, _, n = self.get_params()
        if s is not None:
            gen = CuadradosMedios(s, n)
            self.numeros = gen.generar()
            self.mostrar_resultados("Cuadrados Medios")

    def run_productos(self):
        s1, s2, n = self.get_params()
        if s1 is not None:
            gen = ProductosMedios(s1, s2, n)
            self.numeros = gen.generar()
            self.mostrar_resultados("Productos Medios")

    def run_mult(self):
        MultiplicadorConstanteWindow(self)

    # ---------------- Pruebas ----------------
    def test_media(self):
        if self.numeros:
            test = PruebaMedia(self.numeros)
            self.output_text.insert(tk.END, test.calcular() + "\n")

    def test_varianza(self):
        if self.numeros:
            test = PruebaVarianza(self.numeros)
            self.output_text.insert(tk.END, test.calcular() + "\n")

    def test_chi2(self):
        if self.numeros:
            test = PruebaChi2(self.numeros)
            self.output_text.insert(tk.END, test.calcular() + "\n")

    def exportar(self):
        if self.numeros:
            export_csv(self.numeros)

# ---------------- Ejecutar ----------------
if __name__ == "__main__":
    app = PRNGDashboard()
    app.mainloop()
