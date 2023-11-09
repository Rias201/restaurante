from tkinter import *

def activar_entry(list_n):
    # Enumerar las listas que tenemos guardadas
    options_lists = [meal_options,drink_options,dessert_options]
    cont_lists = [meal_cont,drink_cont,dessert_cont]
    # Mirar cual ha sido el Checkbutton que se ha marcado o desmarcado
    for cont in range(0,len(options_lists[list_n])):
        # Si la casilla está marcada, activa el Entry
        if options_lists[list_n][cont].get() == 1:
            cont_lists[list_n][cont].configure(state=NORMAL)
        # Si no está marcada, desactiva el Entry
        else:
            cont_lists[list_n][cont].delete(0,END)
            cont_lists[list_n][cont].configure(state=DISABLED)

main = Tk()
# Configuración ventana principal
main.title("Gestió de restaurant")
main.config(bg="PapayaWhip")
# main.resizable(0,0)

# Elementos de la ventana principal
top_frame = Frame(main,bd=2,relief=FLAT)
left_frame = Frame(main,bd=1,relief=FLAT)

# Colocación de los elementos de la ventana principal
top_frame.pack(side=TOP)
left_frame.pack(side=LEFT)

# Elementos del frame superior
top_frame_lbl = Label(top_frame,font=("Verdana",78),text="Facturació de restaurant",fg="DarkSlateGray")

# Colocación de los elementos del frame superior
top_frame_lbl.pack()

# Elementos del frame izquierdo
meal_frame_lbl = LabelFrame(left_frame,font=("Verdana",24),text="Plats",fg="Black")
drink_frame_lbl = LabelFrame(left_frame,font=("Verdana",24),text="Begudes",fg="Black")
dessert_frame_lbl = LabelFrame(left_frame,font=("Verdana",24),text="Postres",fg="Black")

# Colocación de los elementos del frame izquierdo
meal_frame_lbl.grid(row=0,column=0,ipadx=2,padx=5)
drink_frame_lbl.grid(row=0,column=1,ipadx=2,padx=5)
dessert_frame_lbl.grid(row=0,column=2,ipadx=2,padx=5)

# Listas de productos
meal_list = ["Amanida", "Canelons", "Paella", "Fideuà", "Entrecot", "Pizza", "Salmó", "Truita"]
drink_list = ["Aigua", "Cola", "Cervesa", "Vi negre", "Vi blanc", "Cava", "Suc", "Gasosa"]
dessert_list = ["Gelat","Café","Cheesecake","Iogurt","Fruita","Tiramisú","Coulant","Profiterols"]

# Generar Checkbuttons para la comida
meal_options = list()
meal_cont = list()
cont = 0
for meal in meal_list:
    # Añadir variable de control para recoger el valor del elemento Checkbutton
    meal_options.append(IntVar())
    Checkbutton(meal_frame_lbl,text=meal,font=("Verdana",18),onvalue=1,offvalue=0,variable=meal_options[cont],command=lambda:activar_entry(0)).grid(row=cont,column=0,sticky=W)
    # Generar Entry para recoger la cantidad
    meal_cont.append(Entry(meal_frame_lbl,font=("Verdana",18),justify=CENTER,bd=1,width=3,state=DISABLED))
    meal_cont[cont].grid(row=cont,column=1,sticky=W)
    # Aumentar contador para la siguiente iteración
    cont += 1

# Generar Checkbuttons para la bebida
drink_options = list()
drink_cont = list()
cont = 0
for drink in drink_list:
    # Añadir variable de control para recoger el valor del elemento Checkbutton
    drink_options.append(IntVar())
    Checkbutton(drink_frame_lbl,text=drink,font=("Verdana",18),onvalue=1,offvalue=0,variable=drink_options[cont],command=lambda:activar_entry(1)).grid(row=cont,column=0,sticky=W)
    # Generar Entry para recoger la cantidad
    drink_cont.append(Entry(drink_frame_lbl,font=("Verdana",18),justify=CENTER,bd=1,width=3,state=DISABLED))
    drink_cont[cont].grid(row=cont,column=1,sticky=W)
    # Aumentar contador para la siguiente iteración
    cont += 1

# Generar Checkbuttons para el postre
dessert_options = list()
dessert_cont = list()
cont = 0
for dessert in dessert_list:
    # Añadir variable de control para recoger el valor del elemento Checkbutton
    dessert_options.append(IntVar())
    Checkbutton(dessert_frame_lbl,text=dessert,font=("Verdana",18),onvalue=1,offvalue=0,variable=dessert_options[cont],command=lambda:activar_entry(2)).grid(row=cont,column=0,sticky=W)
    # Generar Entry para recoger la cantidad
    dessert_cont.append(Entry(dessert_frame_lbl,font=("Verdana",18),justify=CENTER,bd=1,width=3,state=DISABLED))
    dessert_cont[cont].grid(row=cont,column=1,sticky=W)
    # Aumentar contador para la siguiente iteración
    cont += 1

main.mainloop()