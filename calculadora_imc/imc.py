import tkinter as tk
from tkinter import ttk

global colorico
colorico = "#f000"

def umbral(genero, imc):
    if genero == "Hombre":
        if imc < 20:
            return "Desnutricion", "red"
        elif 20 < imc < 24.9:
            return "Un peso normal (Normalidad)", "green"
        elif 24.9 < imc < 29.9:
            return "Sobrepeso", "red"
        elif 29.9 < imc < 40:
            return "Obesidad", "red"
        elif imc > 40:
            return "Obesidad grave", "red"
        else:
            return "Fuera de rango"
    elif genero == "Mujer":
        if imc < 19:
            return "Desnutricion", "red"
        elif 19 < imc < 23:
            return "Un peso normal (Normalidad)", "green"
        elif 24 < imc < 27:
            return "Sobrepeso", "red"
        elif 27 < imc < 32:
            return "Obesidad", "red"
        elif imc > 32:
            return "Obesidad grave", "red"
        else:
            return "Fuera de rango"
    else:
        return "Genero no definido"

def calcIMC():
    peso = float(caja_peso.get().replace(",","."))
    altura = pow(float(caja_altura.get().replace(",",".")), 2)
    imc_form = round(peso/altura, 1)
    genero = cajitaGenero.get()
    estado, colorico = umbral(genero, imc_form)
    etiqueta_imc.config(text=f"Tu IMC es: {imc_form}")
    etiqueta_imc.config(
        text=f"Tu IMC es: {imc_form}")
    etiqueta_umbral.config(text=f"Tienes: {estado}", foreground=colorico)
    


ventana = tk.Tk()
ventana.title("Calculadora IMC")
ventana.config(width=400, height=300)

etiqueta_peso = ttk.Label(text="Tu peso en kilogramos: ")
etiqueta_peso.place(x=20, y=20)
caja_peso = ttk.Entry()

etiqueta_altura = ttk.Label(text="Tu altura en metros: ")
etiqueta_altura.place(x=20, y=60)
caja_altura = ttk.Entry()

cajitaGenero = ttk.Combobox(state="readonly", values=["Hombre", "Mujer"])
cajitaGenero.place(x=180, y=130, width=80)

caja_peso.place(x=180, y=20, width=60)
caja_altura.place(x=180, y=60, width=60)

boton_calcular =  ttk.Button(text="Calcular", command=calcIMC)
boton_calcular.place(x=180, y=100, width=100)

etiqueta_imc = ttk.Label(text="")
etiqueta_imc.place(x=20, y=120)

etiqueta_umbral = ttk.Label(text="")
etiqueta_umbral.place(x=20, y=160)

boton_salir = ttk.Button(text="Salir", command=exit)
boton_salir.place(x=180, y=200, width=100)


ventana.mainloop()