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

def is_num(index):
    if index.isdigit():
        # print(index)
        return True
    elif index == "":
        # print(index)
        return True
    else:
        # print(index)
        return False

main = Tk()
# Configuración ventana principal
main.title("Gestió de restaurant")
main.config(bg="#a30024")
# main.resizable(0,0)
num_vcmd = main.register(is_num)

# Elementos de la ventana principal
top_frame = Frame(main,bg="#a30024")
left_frame = Frame(main,bg="#a30024")
bottom_frame = Frame(left_frame,bg="#a30024")

# Colocación de los elementos de la ventana principal
top_frame.pack(side=TOP)
left_frame.pack(side=LEFT)
bottom_frame.grid(row=1,column=0,columnspan=3)

# Elementos del frame superior
top_frame_lbl = Label(top_frame,font=("Verdana",56),text="Facturació de restaurant",bg="#a30024",fg="White",relief=GROOVE)

# Colocación de los elementos del frame superior
top_frame_lbl.pack()

# Elementos del frame izquierdo
meal_frame = Frame(left_frame,bg="#cf0342")
drink_frame = Frame(left_frame,bg="#cf0342")
dessert_frame = Frame(left_frame,bg="#cf0342")

# Colocación de los elementos del frame izquierdo
meal_frame.grid(row=0,column=0)
drink_frame.grid(row=0,column=1)
dessert_frame.grid(row=0,column=2)

# Elementos del frame de comidas
meal_frame_lbl = LabelFrame(meal_frame,font=("Verdana",24),text="Plats",bg="#cf0342",fg="White",relief=SUNKEN,padx=5)

# Colocación de los elementos del frame de comidas
meal_frame_lbl.pack(side=TOP,padx=5)

# Elementos del frame de bebidas"
drink_frame_lbl = LabelFrame(drink_frame,font=("Verdana",24),text="Begudes",bg="#cf0342",fg="White",relief=SUNKEN,padx=5)

# Colocación de los elementos del frame de bebidas
drink_frame_lbl.pack(side=TOP,padx=5)

# Elementos del frame de postres
dessert_frame_lbl = LabelFrame(dessert_frame,font=("Verdana",24),text="Postres",bg="#cf0342",fg="White",relief=SUNKEN,padx=5)

# Colocación de los elementos del frame de postres
dessert_frame_lbl.pack(side=TOP,padx=5)

# Elementos del frame inferior
meal_price_lbl = Label(bottom_frame,text="Preu menjar €",font=("Verdana",16),bg="#b90133",fg="White")
meal_price = StringVar()
meal_price_entry = Entry(bottom_frame,font=("Verdana",16),width=10,state="readonly",textvariable=meal_price)

drink_price_lbl = Label(bottom_frame,text="Preu beguda €",font=("Verdana",16),bg="#b90133",fg="White")
drink_price = StringVar()
drink_price_entry = Entry(bottom_frame,font=("Verdana",16),width=10,state="readonly",textvariable=drink_price)

dessert_price_lbl = Label(bottom_frame,text="Preu postre €",font=("Verdana",16),bg="#b90133",fg="White")
dessert_price = StringVar()
dessert_price_entry = Entry(bottom_frame,font=("Verdana",16),width=10,state="readonly",textvariable=dessert_price)

taxes_price_lbl = Label(bottom_frame,text="Impostos €",font=("Verdana",16),bg="#b90133",fg="White")
taxes_price = StringVar()
taxes_price_entry = Entry(bottom_frame,font=("Verdana",16),width=10,state="readonly",textvariable=taxes_price)

subtotal_price_lbl = Label(bottom_frame,text="Subtotal €",font=("Verdana",16),bg="#b90133",fg="White")
subtotal_price = StringVar()
subtotal_price_entry = Entry(bottom_frame,font=("Verdana",16),width=10,state="readonly",textvariable=subtotal_price)

total_price_lbl = Label(bottom_frame,text="Preu total €",font=("Verdana",16),bg="#b90133",fg="White")
total_price = StringVar()
total_price_entry = Entry(bottom_frame,font=("Verdana",16),width=10,state="readonly",textvariable=total_price)

# Colocación de los elementos del frame inferior
meal_price_lbl.grid(row=0,column=0,padx=5,sticky=W+E)
meal_price_entry.grid(row=0,column=1,sticky=W+E)
drink_price_lbl.grid(row=1,column=0,padx=5,sticky=W+E)
drink_price_entry.grid(row=1,column=1,sticky=W+E)
dessert_price_lbl.grid(row=2,column=0,padx=5,sticky=W+E)
dessert_price_entry.grid(row=2,column=1,sticky=W+E)
taxes_price_lbl.grid(row=0,column=2,padx=5,sticky=W+E)
taxes_price_entry.grid(row=0,column=3,sticky=W+E)
subtotal_price_lbl.grid(row=1,column=2,padx=5,sticky=W+E)
subtotal_price_entry.grid(row=1,column=3,sticky=W+E)
total_price_lbl.grid(row=2,column=2,padx=5,sticky=W+E)
total_price_entry.grid(row=2,column=3,sticky=W+E)

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
    Checkbutton(meal_frame_lbl,text=meal,font=("Verdana",18),bg="#cf0342",onvalue=1,offvalue=0,variable=meal_options[cont],command=lambda:activar_entry(0)).grid(row=cont,column=0,sticky=W)
    # Generar Entry para recoger la cantidad
    meal_cont.append(Entry(meal_frame_lbl,font=("Verdana",18),justify=CENTER,bg="#fa0560",fg="White",disabledbackground="#cf0342",width=3,state=DISABLED,validate="key",validatecommand=(num_vcmd,'%P')))
    meal_cont[cont].grid(row=cont,column=1,sticky=W,padx=5)
    # Aumentar contador para la siguiente iteración
    cont += 1

# Generar Checkbuttons para la bebida
drink_options = list()
drink_cont = list()
cont = 0
for drink in drink_list:
    # Añadir variable de control para recoger el valor del elemento Checkbutton
    drink_options.append(IntVar())
    Checkbutton(drink_frame_lbl,text=drink,font=("Verdana",18),bg="#cf0342",onvalue=1,offvalue=0,variable=drink_options[cont],command=lambda:activar_entry(1)).grid(row=cont,column=0,sticky=W)
    # Generar Entry para recoger la cantidad
    drink_cont.append(Entry(drink_frame_lbl,font=("Verdana",18),justify=CENTER,bg="#fa0560",fg="White",disabledbackground="#cf0342",width=3,state=DISABLED,validate="key",validatecommand=(num_vcmd,'%P')))
    drink_cont[cont].grid(row=cont,column=1,sticky=W,padx=5)
    # Aumentar contador para la siguiente iteración
    cont += 1

# Generar Checkbuttons para el postre
dessert_options = list()
dessert_cont = list()
cont = 0
for dessert in dessert_list:
    # Añadir variable de control para recoger el valor del elemento Checkbutton
    dessert_options.append(IntVar())
    Checkbutton(dessert_frame_lbl,text=dessert,font=("Verdana",18),bg="#cf0342",onvalue=1,offvalue=0,variable=dessert_options[cont],command=lambda:activar_entry(2)).grid(row=cont,column=0,sticky=W)
    # Generar Entry para recoger la cantidad
    dessert_cont.append(Entry(dessert_frame_lbl,font=("Verdana",18),justify=CENTER,bg="#fa0560",fg="White",disabledbackground="#cf0342",width=3,state=DISABLED,validate="key",validatecommand=(num_vcmd,'%P')))
    dessert_cont[cont].grid(row=cont,column=1,sticky=W,padx=5)
    # Aumentar contador para la siguiente iteración
    cont += 1

main.mainloop()