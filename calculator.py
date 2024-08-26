from tkinter import *

ventana = Tk()
ventana.title('Calculator')
ventana.geometry('525x700')
ventana.config(bg='grey')
ventana.resizable(False, False)

# Variables globales
operacion = ''
resultado = StringVar()
alto = 3
ancho = 8
historial_operaciones = []

def delete():
    global operacion
    operacion = ""
    pantalla.delete(0, END)

def delete_last():
    global operacion
    operacion = operacion[:-1]  # Elimina el último carácter de la operación
    pantalla.delete(0, END)
    pantalla.insert(END, operacion)

def pulse(valor):
    global operacion
    operacion = operacion + str(valor)
    pantalla.delete(0, END)
    pantalla.insert(END, operacion)

def calcu():
    global operacion
    try:
        resultado_str = str(eval(operacion))  # Evalúa la operación
        pantalla.delete(0, END)
        pantalla.insert(END, resultado_str)
        historial_operaciones.append(f"{operacion} = {resultado_str}")  # Agrega la operación al historial
        operacion = resultado_str  # Almacena el resultado para cálculos adicionales
        actualizar_historial()  # Actualiza el Listbox con el historial
    except:
        pantalla.delete(0, END)
        pantalla.insert(END, "Error")
        operacion = ""

def actualizar_historial():
    # Limpia y actualiza el Listbox con el historial
    listbox_operaciones.delete(0, END)
    for operacion in historial_operaciones:
        listbox_operaciones.insert(END, operacion)

def key_press(event):
    tecla = event.keysym
    if tecla.isdigit() or tecla in ('plus', 'minus', 'asterisk', 'slash', 'period','parenthesis'):
        pulse(event.char)
    elif tecla == 'Return':  # Captura la tecla Enter
        calcu()
    elif tecla == 'BackSpace':  # Captura la tecla Backspace
        delete_last()
    elif tecla == 'Escape':  # Captura la tecla Escape
        delete()
    else:
        return "break"  # Evita que cualquier otra tecla se procese

def validate_input(value_if_allowed):
    valid_chars = '0123456789+-*/.()'
    for char in value_if_allowed:
        if char not in valid_chars:
            return False
    return True

# Configuración del widget Entry con validación
vcmd = (ventana.register(validate_input), '%P')

# Configuración del widget Entry
pantalla = Entry(ventana, font=('Arial', 20), width=29, borderwidth=5, justify='right',validate='key', validatecommand=vcmd)
pantalla.grid(row=0, column=0, columnspan=3, padx=10)

# Botón A/C
ac_b = Button(ventana, width=ancho, height=alto, text='A/C', command=lambda: delete())
ac_b.config(fg='red')
ac_b.grid(row=0, column=3, padx=10, pady=10)

# Fila 1 de botones
b7 = Button(ventana, width=ancho, height=alto, text='7', command=lambda: pulse(7))
b7.grid(row=1, column=0, padx=10, pady=10)
b8 = Button(ventana, width=ancho, height=alto, text='8', command=lambda: pulse(8))
b8.grid(row=1, column=1, padx=10, pady=10)
b9 = Button(ventana, width=ancho, height=alto, text='9', command=lambda: pulse(9))
b9.grid(row=1, column=2, padx=10, pady=10)
b_multiplicacion = Button(ventana, width=ancho, height=alto, text='*', command=lambda: pulse('*'))
b_multiplicacion.grid(row=1, column=3, padx=10, pady=10)
b_multiplicacion.config(highlightbackground='orange', bg='orange')

# Fila 2 de botones
b4 = Button(ventana, width=ancho, height=alto, text='4', command=lambda: pulse(4))
b4.grid(row=2, column=0, padx=10, pady=10)
b5 = Button(ventana, width=ancho, height=alto, text='5', command=lambda: pulse(5))
b5.grid(row=2, column=1, padx=10, pady=10)
b6 = Button(ventana, width=ancho, height=alto, text='6', command=lambda: pulse(6))
b6.grid(row=2, column=2, padx=10, pady=10)
b_resta = Button(ventana, width=ancho, height=alto, text='-', command=lambda: pulse('-'))
b_resta.grid(row=2, column=3, padx=10, pady=10)
b_resta.config(highlightbackground='orange', bg='orange')

# Fila 3 de botones
b1 = Button(ventana, width=ancho, height=alto, text='1', command=lambda: pulse(1))
b1.grid(row=3, column=0, padx=10, pady=10)
b2 = Button(ventana, width=ancho, height=alto, text='2', command=lambda: pulse(2))
b2.grid(row=3, column=1, padx=10, pady=10)
b3 = Button(ventana, width=ancho, height=alto, text='3', command=lambda: pulse(3))
b3.grid(row=3, column=2, padx=10, pady=10)
b_suma = Button(ventana, width=ancho, height=alto, text='+', command=lambda: pulse('+'))
b_suma.grid(row=3, column=3, padx=10, pady=10)
b_suma.config(highlightbackground='orange', bg='orange')

# Fila 4 de botones
b0 = Button(ventana, width=23, height=alto, text='0', command=lambda: pulse(0))
b0.grid(row=4, column=0,columnspan=2,padx=10, pady=10)
b_punto = Button(ventana, width=ancho, height=alto, text='.', command=lambda: pulse('.'))
b_punto.grid(row=4, column=2, padx=10, pady=10)
b_igual = Button(ventana, width=ancho, height=9, text='=', command=lambda: calcu())
b_igual.config(highlightbackground='green', bg='green')
b_igual.grid(row=4, column=3,rowspan=2, padx=10, pady=10)

#Fila 5 de botones
b_parentesis_a = Button(ventana, height=alto, width=ancho, text='(', command=lambda:pulse('('))
b_parentesis_a.grid(row=5, column=0, padx=10, pady=10)
b_parentesis_a.config(highlightbackground='orange', bg='orange')
b_parentesis_b = Button(ventana, height=alto, width=ancho, text=')', command=lambda:pulse(')'))
b_parentesis_b.grid(row=5, column=1, padx=10, pady=10)
b_parentesis_b.config(highlightbackground='orange', bg='orange')
b_division = Button(ventana, width=ancho, height=alto, text='/', command=lambda: pulse('/'))
b_division.grid(row=5, column=2, padx=10, pady=10)
b_division.config(highlightbackground='orange', bg='orange')

# Listbox para el historial de operaciones
listbox_operaciones = Listbox(ventana, height=10, width=50)
listbox_operaciones.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

ventana.bind('<Key>', key_press)

ventana.mainloop()