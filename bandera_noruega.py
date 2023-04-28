 # se importa la libreria tkinter con todoas sus fnciones
from tkinter import *

#-----------------------
# funciones de la app
#-----------------------

#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_pricipal,que aquiere las carateristicas de un objeto TK[]
ventana_principal = Tk () 

# titulo de la ventana
ventana_principal.title ("especialidad en sistemas - guanentá")
# ventana tamaño
ventana_principal.geometry("800x500")
# desabilitar boton de maximizar
ventana_principal.resizable(False,False)
# color de fondo de la ventana
ventana_principal.config(bg="white")
#---------------
# frama rojo
#---------------
frame_amarillo = Frame(ventana_principal)
frame_amarillo.config(bg="red", width=200, height=200)
frame_amarillo.place(x=0, y=0 )

#---------------
# frama amarilla
#---------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="red", width=800, height=200)
frame_azul.place(x=300, y=0 )

#---------------
# frama rojo
#---------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red", width=200, height=200)
frame_rojo.place(x=0, y=300)

#-----------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="red", width=800, height=200)
frame_azul.place(x=300, y=300)

#---------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="blue", width=1000, height=60)
frame_azul.place(x=0, y=218)

#----------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="blue", width=60, height=1000)
frame_azul.place(x=220, y=0)


# run
# se ejecuta el emtodo mainloop()de la clase Tk() a travez de la ventana_principal. este metodo despliega la ventana en pantalla y queda ala espera de lo que el usuario haga (click en un boton,escribir,etc). cada accion del usuario se conoce como un evento. El metodo mainloop() es un bucle infventana_principal.mainloop()es un bucle infinito.
ventana_principal.mainloop()