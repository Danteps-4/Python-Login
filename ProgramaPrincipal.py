import tkinter as tk
from tkinter import ttk

class Programa(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.title("Programa principal")

        self._crear_componentes()

    def _iniciar_programa(self):
        self.mainloop()

    def _crear_componentes(self):
        etiqueta1 = ttk.Label(text="Programa principal")
        etiqueta1.pack()


if __name__ == "__main__":
    ventana = Programa()
    ventana.mainloop()