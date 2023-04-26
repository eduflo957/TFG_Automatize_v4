import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("300x200")

# Crear un estilo
estilo = ttk.Style()
estilo.configure('bordeRedondeado', borderwidth=5, relief="solid", background="white", foreground="black", font=("Arial", 12))
estilo.layout('bordeRedondeado', [('Label.border', {'border': '10', 'sticky': 'nswe', 'bordercolor': 'blue'}), ('Label.padding', {'padding': '8 8'})])

# Crear una etiqueta con borde redondeado
etiqueta = ttk.Label(ventana, text="Etiqueta con bordes redondeados", style='bordeRedondeado')
etiqueta.pack(pady=10, padx=10)

ventana.mainloop()
