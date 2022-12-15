import tkinter as tk
from cliente.gui_app import Frame, barra_menu

def main():
    # Creamos una interfaz
    root = tk.Tk()
    # Agregamos un titulo
    root.title('Catálogo de Peliculas')
    # Añadico Icono de la app
    root.iconbitmap('img/logo-catalogo.ico')
    # Diseño estable
    root.resizable(0,0)
    
    barra_menu(root)
    app = Frame(root = root)

    #Indica el final de la ejecución
    app.mainloop()
    
if __name__ == '__main__':
    main()