import tkinter as tk
from tkinter import ttk, messagebox, BOTTOM
import sys
from UsuarioDAO import UsuarioDAO
from Usuario import Usuario
from ProgramaPrincipal import Programa


class VentanaLogin(tk.Tk):
    def __init__(self):
        super().__init__()
        # Configuracion de la ventana
        self.title("Login")
        self.resizable(0, 0)
        self.iconbitmap("images/login-image.ico")

        # Obtencion de las dimensiones de la pantalla
        self._x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        self._y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        self.geometry("250x250+%d+%d" % (self._x, self._y))

        # Variables
        self._entry_var_usuario = tk.StringVar()
        self._entry_var_contraseña = tk.StringVar()
        self._check_var = tk.IntVar(value=0)

        # Configuracion del grid
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=3)

        # Ventana 2
        self._ventana2 = None

        # Creacion de los componentes
        self._crear_componentes()

    def _crear_componentes(self):
        # Botones
        boton_iniciar_sesion1 = ttk.Button(self, text="Iniciar sesión", width=30,
                                           command=lambda: self._crear_ventana_secundaria(0))
        boton_iniciar_sesion1.pack()
        boton_registrarse1 = ttk.Button(self, text="Registrarse", width=30,
                                        command=lambda: self._crear_ventana_secundaria(1))
        boton_registrarse1.pack()
        boton_eliminar1 = ttk.Button(self, text="Eliminar usuario", width=30,
                                     command=lambda: self._crear_ventana_secundaria(2))
        boton_eliminar1.pack()
        boton_salir = ttk.Button(self, text="Salir", width=30, command=self._salir)
        boton_salir.pack(side=BOTTOM)

    def _crear_ventana_principal(self):
        ventana_principal = Programa()
        ventana_principal._iniciar_programa()

    def _crear_ventana_secundaria(self, num):
        self._ventana2 = tk.Toplevel()
        self._ventana2.geometry("300x130+%d+%d" % (self._x, self._y))
        self._ventana2.resizable(0, 0)
        self._ventana2.iconbitmap("images/login-image.ico")

        self._ventana2.columnconfigure(0, weight=1)
        self._ventana2.columnconfigure(1, weight=1)

        etiqueta_usuario = ttk.Label(self._ventana2, text="Usuario:")
        etiqueta_usuario.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        etiqueta_contraseña = ttk.Label(self._ventana2, text="Contraseña:")
        etiqueta_contraseña.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        caja_texto_usuario = ttk.Entry(self._ventana2, textvariable=self._entry_var_usuario)
        caja_texto_usuario.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        self.caja_texto_contraseña = ttk.Entry(self._ventana2, textvariable=self._entry_var_contraseña, show="*")
        self.caja_texto_contraseña.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        # Mostrar u ocultar contraseña
        check_mostrar_contraseña = tk.Checkbutton(self._ventana2, text="Mostrar contraseña", variable=self._check_var,
                                                  command=self._mostrar_contraseña)
        check_mostrar_contraseña.grid(row=2, column=1)

        if num == 0:
            self._ventana2.title("Iniciar sesion")
            boton_iniciar_sesion = ttk.Button(self._ventana2, text="Iniciar sesion", command=self._iniciar_sesion)
            boton_iniciar_sesion.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        elif num == 1:
            self._ventana2.title("Registrarse")
            boton_registrarse = ttk.Button(self._ventana2, text="Registrarse", command=self._registrarse)
            boton_registrarse.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        elif num == 2:
            self._ventana2.title("Eliminar usuario")
            boton_eliminar = ttk.Button(self._ventana2, text="Eliminar", command=self._eliminar)
            boton_eliminar.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def _iniciar_sesion(self):
        usuario_var = self._entry_var_usuario.get()
        # print(usuario_var)
        contraseña_var = self._entry_var_contraseña.get()
        # print(contraseña_var)
        usuario = Usuario(username=usuario_var, password=contraseña_var)
        var = UsuarioDAO.iniciar_sesion(usuario)
        # print(var)
        if var:
            # print("Existe el usuario, puede ingresar")
            messagebox.showinfo("Iniciar sesion", "Ha iniciado sesion exitosamente")
            self._limpiar_entry()
            self._ventana2.destroy()
            self.quit()
            self.destroy()
            self._crear_ventana_principal()
        else:
            # print("Datos incorrectos, no puede ingresar")
            messagebox.showerror("Iniciar sesion", "Usuario y/o contraseña incorrectos, intente de nuevo")
            self._limpiar_entry()
            self._ventana2.destroy()

    def _registrarse(self):
        usuario_var = self._entry_var_usuario.get()
        # print(usuario_var)
        contraseña_var = self._entry_var_contraseña.get()
        # print(contraseña_var)
        usuario = Usuario(username=usuario_var, password=contraseña_var)
        var = UsuarioDAO.registrar(usuario)
        # print(var)
        if var:
            # print("No existe el usuario, puede registrarse")
            messagebox.showinfo("Registrarse", "Se ha registrado correctamente, por favor inicie sesion")
            self._limpiar_entry()
            self._ventana2.destroy()
        else:
            # print("Ya existe el usuario, no puede registrarse")
            messagebox.showerror("Registrarse", "Datos ya existentes, intente de nuevo con otros datos")
            self._limpiar_entry()
            self._ventana2.destroy()

    def _eliminar(self):
        usuario_var = self._entry_var_usuario.get()
        # print(usuario_var)
        contraseña_var = self._entry_var_contraseña.get()
        # print(contraseña_var)
        usuario = Usuario(username=usuario_var, password=contraseña_var)
        var = UsuarioDAO.eliminar(usuario)
        if var:
            # print("Existe el usuario, puede eliminarse")
            messagebox.showinfo("Eliminar usuario", "Se ha eliminado el usuario correctamente")
            self._limpiar_entry()
            self._ventana2.destroy()
        else:
            # print("No existe el usuario, no puede eliminarse")
            messagebox.showerror("Eliminar usuario",
                                 "No existe el usuario para eliminar, ingrese los datos correspondientes")
            self._limpiar_entry()
            self._ventana2.destroy()

    def _limpiar_entry(self):
        self._entry_var_contraseña.set("")
        self._entry_var_usuario.set("")

    def _mostrar_contraseña(self):
        if self._check_var.get() == 1:
            # print("Mostrar contraseña")
            self.caja_texto_contraseña.config(show="")
        else:
            # print("No mostrar contraseña")
            self.caja_texto_contraseña.config(show="*")

    def _salir(self):
        messagebox.showinfo("Saliendo...", "Saliendo del programa...")
        self.quit()
        self.destroy()
        sys.exit()


ventana = VentanaLogin()
ventana.mainloop()
